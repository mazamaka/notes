---
title: "Octo Browser API -- документация"
description: "API для управления антидетект-браузером Octo Browser: профили, прокси, теги, автоматизация"
source: "https://documenter.getpostman.com/view/1801428/UVC6i6eA"
---

# Octo Browser API

## General information

### Get API Token

Swagger schemas: https://swagger.octobrowser.net/

### Rate Limits and 429 errors

Please check status codes for 429 code: different teams have different limits that depend on subscription level. All limits are shared within the team.

If you need higher limits, you can upgrade your subscription to a higher level.
If you need higher limits than those available with the Advanced subscription, please contact our Technical Support.

If you get code 429, stop all requests and pause for `retry-after` (from headers) seconds.
Not respecting or ignoring 429 responses may result in us enforcing stricter API limits for your team.

```
Retry-After: 0
X-Ratelimit-Limit: 200            # RPM (requests per minute) limit
X-Ratelimit-Limit-Hour: 3000      # RPH (requests per hour) limit
X-Ratelimit-Remaining: 4          # remaining RPM
X-Ratelimit-Remaining-Hour: 2999  # remaining RPH
X-Ratelimit-Reset: 1671789217     # unix timestamp
```

### Current limits for subscription plans

| Plan | RPM | RPH |
|------|-----|-----|
| Base | 50 | 500 |
| Team | 100 | 1500 |
| Advanced | 200 (expandable up to 1,000) | 3,000 (expandable up to 50,000) |

If you require limits exceeding 1,000 RPM and 50,000 RPH, please contact our Support.

### One-time profiles

Octo has support for one-time profiles that:
- have faster creation/start time
- are removed and not synchronized; they are faster to stop and don't clutter the profile list
- are suitable for certain workloads, such as scraping tasks.

One request POST One-time profile is counted as 4 requests when calculating RPM/RPH limits.

### How to run Octo Browser client in the "headless" mode

**Linux:**
```bash
OCTO_HEADLESS=1 ./OctoBrowser.AppImage
```

**Windows (powershell):**
```powershell
$env:OCTO_HEADLESS = "1"; start 'C:\Program Files\Octo Browser\Octo Browser.exe'
```

**macOS:**
```bash
OCTO_HEADLESS=1 open -a "Octo Browser"
```

### Silent installation

**Windows (Powershell):**
```powershell
& '.\Octo_Browser_latest_win.exe' /qn
```

**macOS:**
```bash
hdiutil attach ./Octo_Browser_latest_mac_arm64.dmg
cp -R /Volumes/Octo\ Browser/Octo\ Browser.app /Applications
hdiutil unmount /Volumes/Octo\ Browser
```

---

## Profiles

### GET - Get Profiles

```
GET https://app.octobrowser.net/api/v2/automation/profiles?page_len=100&page=0&fields=title,description,proxy,start_pages,tags,status,last_active,version,storage_options,created_at,updated_at&ordering=active
```

Note: if a request contains two tags in the `search_tags` field, its result will only show profiles containing both tags.

**Headers:**
```
X-Octo-Api-Token: <GET_TOKEN_IN_CLIENT>
```

**Params:**

| Param | Example | Description |
|-------|---------|-------------|
| search | profile_title | (Optional) search only from the beginning of the title |
| search_tags | tag1,tag2 | (Optional) |
| page_len | 100 | (Optional) |
| page | 0 | (Optional) |
| fields | title,description,proxy,... | (Optional) |
| ordering | active | (Optional) created,-created,active,-active,title,-title |
| status | 1 | (Optional) |
| password | true | (Optional) bool |
| proxies | proxy1,proxy2 | (Optional) list of proxies uuids, also @no-proxies-filter |

### POST - Create Profile

```
POST https://app.octobrowser.net/api/v2/automation/profiles
```

Note: if you don't specify a given parameter, we will generate the best values for it on our servers.

**Cookie formats accepted:** JSON, Mozilla, Netscape

**Headers:**
```
Content-Type: application/json
X-Octo-Api-Token: <GET_TOKEN_IN_CLIENT>
```

**Body example:**

```json
{
  "title": "Test profile from api",
  "description": "test description",
  "start_pages": ["https://fb.com"],
  "password": "password",
  "tags": ["octo"],
  "pinned_tag": "octo",
  "proxy": {
    "type": "socks5",
    "host": "1.1.1.1",
    "port": 5555,
    "login": "",
    "password": ""
  },
  "storage_options": {
    "cookies": true,
    "passwords": true,
    "extensions": true,
    "localstorage": false,
    "history": false,
    "bookmarks": true
  },
  "cookies": [
    {
      "domain": ".google.com",
      "expirationDate": 1639134293.313654,
      "hostOnly": false,
      "httpOnly": false,
      "name": "1P_JAR",
      "path": "/",
      "sameSite": "no_restriction",
      "secure": true,
      "value": "2021-11-10-11"
    }
  ],
  "fingerprint": {
    "os": "mac",
    "os_version": "11",
    "os_arch": "x86",
    "renderer": "AMD Radeon Pro 450",
    "screen": "1920x1080",
    "languages": {"type": "ip"},
    "timezone": {"type": "ip"},
    "geolocation": {"type": "ip"},
    "cpu": 4,
    "ram": 8,
    "noise": {
      "webgl": true,
      "canvas": false,
      "audio": true,
      "client_rects": false
    },
    "webrtc": {"type": "ip"},
    "dns": "1.1.1.1",
    "media_devices": {
      "video_in": 1,
      "audio_in": 1,
      "audio_out": 1
    }
  }
}
```

### WebRTC options

```json
{"webrtc": {"type": "disable_non_proxied_udp", "data": null}}
{"webrtc": {"type": "real", "data": null}}
{"webrtc": {"type": "ip", "data": null}}
```

### Language, timezone and geolocation

```json
{
  "languages": {"type": "manual", "data": ["[ru-RU] Russian (Russia)", "[en-US] English (United States)"]},
  "timezone": {"type": "manual", "data": "America/Detroit"},
  "geolocation": {"type": "manual", "data": {"latitude": 41.40338, "longitude": 2.17403, "accuracy": 10}}
}
```

### Storage Options

```json
{
  "storage_options": {
    "cookies": true,
    "passwords": true,
    "extensions": true,
    "localstorage": false,
    "history": false,
    "bookmarks": true,
    "serviceworkers": false
  }
}
```

### DELETE - Delete Profiles

```
DELETE https://app.octobrowser.net/api/v2/automation/profiles
```

`skip_trash_bin: true` is enabled by default.

```json
{
  "uuids": ["{PROFILE_UUID}"],
  "skip_trash_bin": true
}
```

### GET - Get Profile

```
GET https://app.octobrowser.net/api/v2/automation/profiles/:uuid
```

### PATCH - Update Profile

```
PATCH https://app.octobrowser.net/api/v2/automation/profiles/:uuid
```

Note: It's possible to update running profiles; however, we recommend updating only stopped profiles for synchronization reasons.

### POST - Import Cookies

```
POST https://app.octobrowser.net/api/v2/automation/profiles/:uuid/import_cookies
```

Accepts JSON, Mozilla, and Netscape cookie formats.

### POST - Transfer profiles

```
POST https://app.octobrowser.net/api/v2/automation/profiles/transfer
```

Maximum 100 profiles per request.

```json
{
  "uuids": [""],
  "receiver_email": "{{USER_ACCOUNT}}",
  "transfer_proxy": true
}
```

### POST - Force Stop Profile

```
POST https://app.octobrowser.net/api/v2/automation/profiles/:uuid/force_stop
```

### POST - Mass Force Stop Profile

```
POST https://app.octobrowser.net/api/v2/automation/profiles/force_stop
```

```json
{
  "uuids": ["{PROFILE_UUID}"]
}
```

### GET - Get Export profiles

```
GET https://app.octobrowser.net/api/v2/automation/profiles/export?page=0&page_len=10
```

### POST - Export profiles

```
POST https://app.octobrowser.net/api/v2/automation/profiles/export
```

Up to 100 profiles per request. This is a paid action (0.5 tokens per profile).

### POST - Import profiles

```
POST https://app.octobrowser.net/api/v2/automation/profiles/import
```

Up to 100 profiles per request.

### POST - Set Profiles Password

```
POST https://app.octobrowser.net/api/v2/automation/profiles/set_password
```

```json
{
  "profiles": ["uuid", "uuid"],
  "password": "password",
  "old_password": "old_password"
}
```

### POST - Clear Profile Password

```
POST https://app.octobrowser.net/api/v2/automation/profiles/:uuid/clear_password
```

---

## Tags

### GET - Get Tags

```
GET https://app.octobrowser.net/api/v2/automation/tags
```

### POST - Create Tag

```
POST https://app.octobrowser.net/api/v2/automation/tags
```

Available colors: grey, blue, cyan, orange, green, purple, red, yellow

```json
{
  "name": "supertag",
  "color": "blue"
}
```

### DELETE - Remove Tag

```
DELETE https://app.octobrowser.net/api/v2/automation/tags/:uuid
```

### PATCH - Update Tag

```
PATCH https://app.octobrowser.net/api/v2/automation/tags/:uuid
```

---

## Proxies

### GET - Get Proxies

```
GET https://app.octobrowser.net/api/v2/automation/proxies
```

### POST - Create Proxy

```
POST https://app.octobrowser.net/api/v2/automation/proxies
```

```json
{
  "type": "socks",
  "host": "localhost",
  "port": 1081,
  "login": "user",
  "password": "secret111",
  "title": "super proxy",
  "change_ip_url": "http://example.com",
  "external_id": "12345"
}
```

### DELETE - Remove Proxy

```
DELETE https://app.octobrowser.net/api/v2/automation/proxies/:uuid
```

### PATCH - Update Proxy

```
PATCH https://app.octobrowser.net/api/v2/automation/proxies/:uuid
```

---

## Local client API

The default server port is 58888.
The API URL is `http://localhost:58888`.

### GET - List Active Profiles

```
GET http://localhost:58888/api/profiles/active
```

Shows the list of profiles launched on your device. `webSocketDebuggerUrl` will be shown only for profiles launched in headless mode.

### POST - Start Profile

```
POST http://localhost:58888/api/profiles/start
```

- `debug_port=true` enables the automation port (random free port).
- `debug_port=20000` launches on a specific port (1024-65534).
- `timeout` overrides the default start timeout.
- `flags` allows additional Chromium flags.
- `chromedrivers` allows downloading official chromedrivers.

```json
{
  "uuid": "",
  "headless": false,
  "debug_port": true,
  "only_local": true,
  "flags": [],
  "timeout": 120,
  "password": "password"
}
```

**Start error codes:**

| Error | Code |
|-------|------|
| ComponentNotFoundException | 1 |
| ProfileAlreadyRunningException | 2 |
| ProfileStartFailedException | 3 |
| GetProxyDataFailedException | 4 |
| InvalidProxyDataException | 5 |
| ProfileNotFoundException | 6 |
| NoSubscriptionException | 7 |
| OutdatedVersionException | 8 |
| ProfileVersionConsistencyError | 9 |

### POST - Stop Profile

```
POST http://localhost:58888/api/profiles/stop
```

```json
{"uuid": ""}
```

### POST - Force Stop Profile

```
POST http://localhost:58888/api/profiles/force_stop
```

Requires Octo Browser 1.7 or later.

### POST - Login

```
POST http://localhost:58888/api/auth/login
```

Requires Octo Browser 1.8.0 or later.

```json
{
  "email": "useremail@domain.net",
  "password": "userpassword"
}
```

### POST - Logout

```
POST http://localhost:58888/api/auth/logout
```

### GET - Get Client Version

```
GET http://localhost:58888/api/update
```

### POST - Update Client

```
POST http://localhost:58888/api/update
```

### GET - Username

```
GET http://localhost:58888/api/username
```

### POST - One-time profile

```
POST http://localhost:58888/api/profiles/one_time/start
```

```json
{
  "profile_data": {
    "fingerprint": {
      "os": "win",
      "os_version": "11",
      "screen": "1920x1080",
      "languages": {"type": "ip"},
      "timezone": {"type": "ip"},
      "geolocation": {"type": "ip"},
      "cpu": 4,
      "ram": 8,
      "noise": {"webgl": true, "canvas": false, "audio": true, "client_rects": false},
      "webrtc": {"type": "ip"},
      "dns": "1.1.1.1",
      "media_devices": {"video_in": 1, "audio_in": 1, "audio_out": 1}
    },
    "extensions": ["ewbjmajocgfcbeboaewbfgobmjsjcoja@1.0"],
    "start_pages": ["https://fb.com"],
    "proxy": {"type": "socks5", "host": "1.1.1.1", "port": 5555, "login": "", "password": ""},
    "cookies": []
  },
  "headless": false,
  "debug_port": true,
  "flags": [],
  "timeout": 60
}
```

### POST - Set profile password

```
POST http://localhost:58888/api/profiles/password
```

### DELETE - Delete profile password

```
DELETE http://localhost:58888/api/profiles/password
```

---

## Teams

### GET - Get Extensions

```
GET https://app.octobrowser.net/api/v2/automation/teams/extensions?start=0&limit=25
```

### DELETE - Delete Extensions

```
DELETE https://app.octobrowser.net/api/v2/automation/teams/extensions
```

Maximum UUID batch length is 100.

### GET - Get subaccounts

```
GET https://app.octobrowser.net/api/v2/automation/teams/subaccounts
```

### POST - Create subaccount

```
POST https://app.octobrowser.net/api/v2/automation/teams/subaccounts
```

If a permission is not specified, it will be set as false.

### PATCH - Update subaccount

```
PATCH https://app.octobrowser.net/api/v2/automation/teams/subaccounts
```

### DELETE - Delete subaccount

```
DELETE https://app.octobrowser.net/api/v2/automation/teams/subaccounts
```

---

## Fingerprint

### GET - Get Renderers

```
GET https://app.octobrowser.net/api/v2/automation/fingerprint/renderers?page_len=100&page=0&os=win&os_arch=x86
```

### GET - Get Screens

```
GET https://app.octobrowser.net/api/v2/automation/fingerprint/screens?os=win&os_arch=x86
```

### GET - Get Mobile Device Models

```
GET https://app.octobrowser.net/api/v2/automation/fingerprint/device_models?device_type=phone
```

---

## Docker

### Dockerfile

```dockerfile
FROM ubuntu:22.04
ARG TZ=America/Los_Angeles
ARG DEBIAN_FRONTEND=noninteractive
ENV LANG="C.UTF-8"
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    unzip \
    libgles2 libegl1 xvfb
```

### run.sh

```bash
export EMAIL=your_email
export PASSWORD=your_password
export PROFILE_UUID=PUT_UUID_HERE
docker build -t octobrowser:latest .
docker run --name octo -it --rm \
    --security-opt seccomp:unconfined \
    -v '/srv/docker_octo/cache:/home/octo/.Octo Browser/' \
    -p 58895:58888 \
    octobrowser:latest
# get xh: https://github.com/ducaale/xh/releases
xh POST localhost:58895/api/auth/login email=${EMAIL} password=${PASSWORD}
```

### Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: cloud-instance
        image: {{ .Values.octoImage }}:{{ .Values.tag }}
        securityContext:
          capabilities:
            add: [SYS_ADMIN]
```

---

## Automation Libraries

### Playwright Sync Python

```python
import httpx
from playwright.sync_api import sync_playwright

PROFILE_UUID = "UUID_OF_YOUR_PROFILE"

def main():
    with sync_playwright() as p:
        start_response = httpx.post(
            'http://127.0.0.1:58888/api/profiles/start',
            json={
                'uuid': PROFILE_UUID,
                'headless': False,
                'debug_port': True
            }
        )
```

### Playwright Async Python

```python
import httpx
import asyncio
from playwright.async_api import async_playwright

PROFILE_UUID = "UUID_OF_YOUR_PROFILE"

async def main():
    async with async_playwright() as p:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                'http://127.0.0.1:58888/api/profiles/start',
                json={
                    'uuid': PROFILE_UUID,
                    'headless': False,
                    'debug_port': True
                }
            )
```

### Selenium

NB: By default Selenium is exposed in the browser and can be detected by some sites. Consider using undetected-chromedriver.

```python
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PROFILE_ID = 'PROFILE_UUID'
LOCAL_API = 'http://localhost:58888/api/profiles'

def get_webdriver(port):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
    return webdriver.Chrome(options=chrome_options)
```
