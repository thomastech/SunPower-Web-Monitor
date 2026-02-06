#!/usr/bin/env python3
# proxy.py  —  Flask proxy + static server for solar_dashboard.html

from flask import Flask, request, Response, send_from_directory
import requests, os, logging
import urllib3

# Ignore insecure HTTPS warnings for self-signed gateway certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__, static_folder='.')

# simple in-memory session storage: ip -> requests.Session()
sessions = {}

# Add CORS headers generally (safe for local LAN). Because we serve dashboard from same origin,
# it isn't strictly necessary, but it's harmless and helps debug other clients.
@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return resp

@app.route('/devices', methods=['GET','OPTIONS'])
def devices():
    if request.method == 'OPTIONS':
        return Response('', status=200)

    ip = request.args.get('ip')
    user = request.args.get('user')
    passwd = request.args.get('pass')

    if not ip:
        return Response("Missing ?ip= parameter", status=400)

    # If username/password provided -> new firmware path (HTTPS login -> cookie -> use cookie)
    if user and passwd:
        sess = sessions.get(ip)
        # login if no session
        if not sess:
            sess = requests.Session()
            try:
                r = sess.get(f"https://{ip}/auth?login", auth=(user, passwd), verify=False, timeout=30)
            except Exception as e:
                return Response(f"Login error: {e}", status=500)
            if r.status_code != 200 or not sess.cookies:
                # Authentication failed
                return Response(f"Authentication failed (HTTP {r.status_code}).", status=403)
            sessions[ip] = sess

        # fetch device list with stored cookie/session
        try:
            r = sessions[ip].get(f"https://{ip}/cgi-bin/dl_cgi/devices/list", verify=False, timeout=30)
        except Exception as e:
            return Response(f"Fetch error: {e}", status=500)

        # If the session is invalid (401/403), try re-login once
        if r.status_code in (401, 403):
            try:
                new_sess = requests.Session()
                r2 = new_sess.get(f"https://{ip}/auth?login", auth=(user, passwd), verify=False, timeout=30)
            except Exception as e:
                return Response(f"Re-login error: {e}", status=500)
            if r2.status_code == 200 and new_sess.cookies:
                sessions[ip] = new_sess
                r = sessions[ip].get(f"https://{ip}/cgi-bin/dl_cgi/devices/list", verify=False, timeout=30)
            else:
                return Response(f"Authentication failed (HTTP {r2.status_code}).", status=403)

        return Response(r.text, mimetype='application/json', status=r.status_code)

    # No credentials provided -> assume older firmware: try HTTP direct (no auth)
    else:
        try:
            r = requests.get(f"http://{ip}/cgi-bin/dl_cgi/devices/list", timeout=30)
        except Exception as e:
            return Response(f"Fetch error: {e}", status=500)

        # If server says 401/403 -> it likely requires authentication
        if r.status_code in (401, 403):
            return Response(f"Gateway requires authentication (HTTP {r.status_code}).", status=403)

        return Response(r.text, mimetype='application/json', status=r.status_code)


# Serve the dashboard HTML file from same directory
@app.route('/solar_dashboard.html')
def dashboard():
    return send_from_directory('.', 'solar_dashboard.html')

# simple root help
@app.route('/')
def root():
    return "Solar proxy running. Visit /solar_dashboard.html"

if __name__ == '__main__':
    # production: use systemd; development: run here
    app.run(host='0.0.0.0', port=5000)
