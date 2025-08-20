# PVS6 API Command Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| /dl_cgi/cert/mqtt | POST | Renew MQTT certificate |
| /dl_cgi/network/interfaceConfig/dhcp/{networkType} | GET | Renew DHCP lease (eth, wifi, plc) |
| /dl_cgi/network/interfaceConfig/dhcp/{networkType} | DELETE | Release DHCP lease |
| /dl_cgi/network/interfaceConfig/{networkType} | GET | Get interface configuration |
| /dl_cgi/network/interfaceConfig/{networkType} | POST | Update interface configuration |
| /dl_cgi/network/interfaces | GET | List network interfaces |
| /dl_cgi/network/settings | GET | Get general network settings |
| /dl_cgi/network/settings | POST | Update general network settings |
| /dl_cgi/network/firewallSettings | GET | Get firewall settings |
| /dl_cgi/network/firewallSettings | POST | Update firewall settings |
| /dl_cgi/network/getPingableDevices | GET | Get pingable devices |
| /dl_cgi/network/ping | GET | Get ping status |
| /dl_cgi/network/ping | POST | Start ping |
| /dl_cgi/network/traceroute | GET | Get traceroute status |
| /dl_cgi/network/traceroute | POST | Start traceroute |
| /dl_cgi/network/tunnel | GET | Get SSH tunnel status |
| /dl_cgi/network/tunnel | POST | Start SSH tunnel |
| /dl_cgi/network/tunnel | DELETE | Delete all SSH tunnels |
| /dl_cgi/network/whitelist | GET | Get whitelist entries |
| /dl_cgi/network/whitelist | POST | Add whitelist entry |
| /dl_cgi/network/checkCellPrimary | POST | Start check if cellular can be primary |
| /dl_cgi/network/powerProduction | GET | Get solar power production status |
| /dl_cgi/network/powerProduction | POST | Enable/disable power production |
| /dl_cgi/devices/list | GET | Get device list |
| /dl_cgi/devices | GET | Get claim status |
| /dl_cgi/devices | POST | Add/remove devices (claim) |
| /dl_cgi/devices/replace | POST | Replace devices list |
| /dl_cgi/candidates | GET | Get candidate devices |
| /dl_cgi/candidates | POST | Add candidate devices |
| /dl_cgi/devices/met/calibration | POST | Set met station calibration |
| /dl_cgi/devices/meter/parameters | POST | Configure meter parameters |
| /dl_cgi/panels/layout | GET | Get panel layout |
| /dl_cgi/panels/layout | POST | Set panel layout |
| /dl_cgi/firmware/upgrade | GET | Get firmware upgrade status |
| /dl_cgi/firmware/upgrade | POST | Start firmware upgrade |
| /dl_cgi/firmware/upgrade | DELETE | Cancel firmware upgrade |
| /dl_cgi/firmware/new_version | GET | Check for new firmware version |
| /upload_firmware | POST | Upload firmware image |
| /upload-grid-profiles | POST | Upload grid profiles |
| /upgrade-packages | POST | Upload signed upgrade bundle |
| /dl_cgi/grid/voltage | GET | Get grid voltage setting (208/240V) |
| /dl_cgi/grid/voltage | POST | Set grid voltage |
| /dl_cgi/grid/export_limit | GET | Get export limit |
| /dl_cgi/grid/export_limit | POST | Set export limit |
| /dl_cgi/grid/profiles | GET | Get available grid profiles |
| /dl_cgi/grid/profiles | POST | Refresh grid profiles |
| /dl_cgi/grid/profile | GET | Get current grid profile (v1) |
| /dl_cgi/grid/profile | POST | Set grid profile (v1) |
| /dl_cgi/grid/v2/profile | GET | Get current grid profile (v2) |
| /dl_cgi/grid/v2/profile | POST | Set grid profile (v2) |
| /dl_cgi/grid/zero_export_meter | POST | Set zero-export meter type |
| /dl_cgi/commissioning/start | POST | Start commissioning |
| /dl_cgi/commissioning/stop | POST | Stop commissioning |
| /dl_cgi/commission/config | POST | Send configuration to EDP |
| /dl_cgi/commission/decommission | POST | Decommission PVS from EDP |
| /dl_cgi/supervisor/info | GET | Get supervisor info (model, version, etc.) |
| /dl_cgi/supervisor/serial_number | POST | Set supervisor serial number |
| /dl_cgi/meta | POST | Set metadata (site key, timezone, devices) |
| /dl_cgi/communication/AP/enable | POST | Enable WiFi AP mode |
| /dl_cgi/communication/AP/disable | POST | Disable WiFi AP mode |
| /dl_cgi/communication/ap | GET | Get available APs (legacy) |
| /dl_cgi/communication/ap | POST | Connect to AP (legacy) |
| /dl_cgi/communication/sta | GET | Get available APs (modern) |
| /dl_cgi/communication/sta | POST | Connect to AP (modern) |
| /dl_cgi/communication/sta/disconnect | POST | Disconnect WiFi station |
| /dl_cgi/communication/cellular/primary | GET | Is cellular primary |
| /dl_cgi/communication/cellular/primary | POST | Set cellular primary |
| /dl_cgi/communication/cellular/primary | DELETE | Unset cellular primary |
| /dl_cgi/communication/cellular/purchased | GET | Is cellular service purchased |
| /dl_cgi/communication/cellular/purchased | POST | Set purchased flag |
| /dl_cgi/communication/cellular/purchased | DELETE | Unset purchased flag |
| /dl_cgi/communication/plc/pair | POST | Pair PLC |

---
<br>
<br>

# ⚡ Sending Commands from Windows PC

## Using curl (built into Windows 10+)

Example: Get power production
curl -X GET "http://172.27.153.1/cgi-bin/dl_cgi/network/powerProduction"

Example: Set grid voltage to 240V
curl -X POST "http://172.27.153.1/cgi-bin/dl_cgi/grid/voltage" ^
     -H "Content-Type: application/json" ^
     -d "{\"grid_voltage\": 240}"

<br>

## Using PowerShell Invoke-RestMethod

Example: Get device list
Invoke-RestMethod -Uri "http://172.27.153.1/cgi-bin/dl_cgi/devices/list" -Method GET

Example: Start commissioning
Invoke-RestMethod -Uri "http://172.27.153.1/cgi-bin/dl_cgi/commissioning/start" `
  -Method POST -ContentType "application/json"

<br>

## Using Postman (GUI)

Import swagger.json directly into Postman.

All endpoints will be preloaded with parameters. Good for testing before writing scripts.