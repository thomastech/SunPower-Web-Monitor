# SunPower Web Monitor — Docker

Containerized deployment of the [SunPower Web Monitor](https://github.com/thomastech/SunPower-Web-Monitor) proxy + dashboard.

## Quick Start

```bash
docker compose up -d --build
```

Then open in your browser:

- **New firmware** (with auth):
  `http://localhost:8080/solar_dashboard.html?ip=YOUR_PVS_IP&user=YOUR_USER&pass=YOUR_PASS`

- **Old firmware** (no auth):
  `http://localhost:8080/solar_dashboard.html?ip=YOUR_PVS_IP`

## Configuration

The dashboard is served on **port 8080** by default (port 5000 conflicts with macOS AirPlay Receiver).

To use a different host port, override via `.env` file or inline:

```bash
HOST_PORT=9090 docker compose up -d --build
```

## Networking (macOS)

Docker Desktop for Mac routes container outbound traffic through the host network stack. The container can reach your PVS gateway on the LAN without any special networking configuration — standard port mapping is all that's needed.

## Logs

```bash
docker compose logs -f solar-monitor
```

## Stop

```bash
docker compose down
```
