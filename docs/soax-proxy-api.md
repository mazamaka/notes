---
title: "SOAX Proxy API -- документация"
description: "API для управления прокси-сервисом SOAX: Geo Data API, Partner API (Whitelist), таргетинг"
source: "https://helpcenter.soax.com/"
---

# SOAX Proxy API Documentation

API для управления прокси-сервисом SOAX (Residential & Mobile Proxies).

## Credentials

| Параметр | Значение |
|----------|----------|
| API Key | `7ootC1ngSfH-08xI` |
| Dashboard | https://soax.com/dashboard |
| Help Center | https://helpcenter.soax.com/ |

---

## Базовые URL

| Тип API | Base URL |
|---------|----------|
| Geo Data API | `https://api.soax.com/api/` |
| Partner API | `https://partner.api.soax.com/v1/` |

---

## Аутентификация

### Geo Data API
Передается через query-параметр `api_key`:
```
?api_key=7ootC1ngSfH-08xI
```

### Partner API
Передается через HTTP заголовок:
```
api-key: 7ootC1ngSfH-08xI
```

---

## Geo Data API

### Общие параметры

| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| `api_key` | string | Да | API ключ из Dashboard |
| `package_key` | string | Да | Логин (ключ) пакета |
| `country_iso` | string | Да | ISO код страны (lowercase: `us`, `de`, `ru`) |
| `conn_type` | string | Да* | Тип подключения: `wifi` или `mobile` |

> *`conn_type` обязателен для endpoints городов и регионов

---

### GET /get-country-regions

Получение списка доступных регионов страны.

**URL:** `https://api.soax.com/api/get-country-regions`

**Параметры:**

| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| `api_key` | string | Да | API ключ |
| `package_key` | string | Да | Ключ пакета |
| `country_iso` | string | Да | ISO код страны (lowercase) |
| `conn_type` | string | Да | `wifi` для residential, `mobile` для мобильных |
| `provider` | string | Нет | Фильтр по провайдеру |

**Пример запроса:**
```bash
curl "https://api.soax.com/api/get-country-regions?api_key=7ootC1ngSfH-08xI&package_key=YOUR_PACKAGE_KEY&country_iso=us&conn_type=wifi"
```

**Пример ответа:**
```json
{
  "success": true,
  "data": [
    {"name": "California", "code": "CA"},
    {"name": "Texas", "code": "TX"},
    {"name": "New York", "code": "NY"}
  ]
}
```

---

### GET /get-country-cities

Получение списка доступных городов.

**URL:** `https://api.soax.com/api/get-country-cities`

**Параметры:**

| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| `api_key` | string | Да | API ключ |
| `package_key` | string | Да | Ключ пакета |
| `country_iso` | string | Да | ISO код страны (lowercase) |
| `conn_type` | string | Да | `wifi` для residential, `mobile` для мобильных |
| `provider` | string | Нет | Фильтр по провайдеру |
| `region` | string | Нет | Фильтр по региону |

**Пример ответа:**
```json
{
  "success": true,
  "data": [
    {"name": "Los Angeles"},
    {"name": "San Francisco"},
    {"name": "San Diego"}
  ]
}
```

---

### GET /get-country-operators

Получение списка мобильных операторов.

> **Только для Mobile пакетов!**

**URL:** `https://api.soax.com/api/get-country-operators`

---

### GET /get-country-isp

Получение списка WiFi ISP (Интернет-провайдеров).

> **Только для Wi-Fi (residential) пакетов!**

**URL:** `https://api.soax.com/api/get-country-isp`

---

## Partner API (Whitelist Management)

API для управления IP Whitelist в пакетах.

> **Важно:** Whitelist IP требуется для IP-авторизации. При использовании login/password авторизации whitelist не обязателен (включается режим "Any IP").

### Аутентификация

Все запросы требуют заголовок:
```
api-key: 7ootC1ngSfH-08xI
```

---

### GET /v1/account/package/{package_key}/ip-list

Получение информации о всех IP слотах в пакете.

**Пример ответа:**
```json
{
  "success": true,
  "data": [
    {"ip": "192.168.1.100", "comment": "Main server", "slot": 1},
    {"ip": "192.168.1.101", "comment": "Backup server", "slot": 2},
    {"ip": null, "comment": "", "slot": 3}
  ]
}
```

---

### POST /v1/account/package/{package_key}/update-ip

Добавление или обновление IP в слоте Whitelist.

**Body (JSON array):**
```json
[
  {
    "ip": "192.168.1.100",
    "slot": 1,
    "comment": "Production server"
  }
]
```

---

### POST /v1/account/package/{package_key}/detach-ip

Удаление IP из слота (слот остается пустым, не удаляется).

**Вариант 1: Удаление по номеру слота**
```json
[{"slot": 1}]
```

**Вариант 2: Удаление по IP адресу**
```json
[{"ip": "192.168.1.100"}]
```

---

## Использование прокси

### Формат прокси

```
proxy.soax.com:PORT:USERNAME:PASSWORD
```

или с таргетингом:

```
proxy.soax.com:PORT:USERNAME_country-US_state-California_city-LosAngeles:PASSWORD
```

### Параметры таргетинга в username

| Параметр | Формат | Пример |
|----------|--------|--------|
| Страна | `country-XX` | `country-US` |
| Штат/Регион | `state-Name` | `state-California` |
| Город | `city-Name` | `city-LosAngeles` |
| ISP | `isp-Name` | `isp-Comcast` |
| Оператор (mobile) | `operator-Name` | `operator-ATT` |
| Session ID | `sessid-XXX` | `sessid-abc123` |
| Session time | `sesstime-XXX` | `sesstime-600` |

**Пример полного username:**
```
package12345_country-US_state-California_city-LosAngeles_sessid-mysession_sesstime-600
```

---

## Python Client Example

```python
import httpx
from typing import Optional, List, Dict, Any

class SoaxClient:
    """SOAX Proxy API Client"""

    GEO_API_URL = "https://api.soax.com/api"
    PARTNER_API_URL = "https://partner.api.soax.com/v1"

    def __init__(self, api_key: str, package_key: str):
        self.api_key = api_key
        self.package_key = package_key
        self._client = httpx.AsyncClient(timeout=30.0)

    async def close(self):
        await self._client.aclose()

    async def get_regions(
        self,
        country_iso: str,
        conn_type: str = "wifi",
        provider: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get available regions for a country."""
        params = {
            "api_key": self.api_key,
            "package_key": self.package_key,
            "country_iso": country_iso.lower(),
            "conn_type": conn_type,
        }
        if provider:
            params["provider"] = provider
        resp = await self._client.get(f"{self.GEO_API_URL}/get-country-regions", params=params)
        resp.raise_for_status()
        return resp.json().get("data", [])

    async def get_cities(
        self,
        country_iso: str,
        conn_type: str = "wifi",
        region: Optional[str] = None,
        provider: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get available cities for a country."""
        params = {
            "api_key": self.api_key,
            "package_key": self.package_key,
            "country_iso": country_iso.lower(),
            "conn_type": conn_type,
        }
        if region:
            params["region"] = region
        if provider:
            params["provider"] = provider
        resp = await self._client.get(f"{self.GEO_API_URL}/get-country-cities", params=params)
        resp.raise_for_status()
        return resp.json().get("data", [])

    async def get_operators(
        self,
        country_iso: str,
        region: Optional[str] = None,
        city: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get available mobile operators (Mobile packages only)."""
        params = {
            "api_key": self.api_key,
            "package_key": self.package_key,
            "country_iso": country_iso.lower(),
        }
        if region:
            params["region"] = region
        if city:
            params["city"] = city
        resp = await self._client.get(f"{self.GEO_API_URL}/get-country-operators", params=params)
        resp.raise_for_status()
        return resp.json().get("data", [])

    async def get_isps(
        self,
        country_iso: str,
        region: Optional[str] = None,
        city: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get available ISPs (WiFi/Residential packages only)."""
        params = {
            "api_key": self.api_key,
            "package_key": self.package_key,
            "country_iso": country_iso.lower(),
        }
        if region:
            params["region"] = region
        if city:
            params["city"] = city
        resp = await self._client.get(f"{self.GEO_API_URL}/get-country-isp", params=params)
        resp.raise_for_status()
        return resp.json().get("data", [])

    async def get_ip_list(self) -> List[Dict[str, Any]]:
        """Get all IP slots in the package whitelist."""
        resp = await self._client.get(
            f"{self.PARTNER_API_URL}/account/package/{self.package_key}/ip-list",
            headers={"api-key": self.api_key}
        )
        resp.raise_for_status()
        return resp.json().get("data", [])

    async def update_ip(
        self,
        ip: str,
        slot: int,
        comment: Optional[str] = None
    ) -> Dict[str, Any]:
        """Add or update IP in a whitelist slot."""
        payload = [{"ip": ip, "slot": slot}]
        if comment:
            payload[0]["comment"] = comment
        resp = await self._client.post(
            f"{self.PARTNER_API_URL}/account/package/{self.package_key}/update-ip",
            headers={"api-key": self.api_key, "Content-Type": "application/json"},
            json=payload
        )
        resp.raise_for_status()
        return resp.json()

    async def detach_ip_by_slot(self, slot: int) -> Dict[str, Any]:
        """Remove IP from whitelist by slot number."""
        resp = await self._client.post(
            f"{self.PARTNER_API_URL}/account/package/{self.package_key}/detach-ip",
            headers={"api-key": self.api_key, "Content-Type": "application/json"},
            json=[{"slot": slot}]
        )
        resp.raise_for_status()
        return resp.json()

    async def detach_ip_by_address(self, ip: str) -> Dict[str, Any]:
        """Remove IP from whitelist by IP address."""
        resp = await self._client.post(
            f"{self.PARTNER_API_URL}/account/package/{self.package_key}/detach-ip",
            headers={"api-key": self.api_key, "Content-Type": "application/json"},
            json=[{"ip": ip}]
        )
        resp.raise_for_status()
        return resp.json()


# Usage example
async def main():
    client = SoaxClient(
        api_key="7ootC1ngSfH-08xI",
        package_key="your_package_key"
    )

    try:
        regions = await client.get_regions("us", "wifi")
        print("Regions:", regions)

        cities = await client.get_cities("us", "wifi", region="California")
        print("Cities:", cities)

        ip_list = await client.get_ip_list()
        print("Whitelist:", ip_list)

        result = await client.update_ip("192.168.1.100", slot=1, comment="My server")
        print("Update result:", result)
    finally:
        await client.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Error Handling

### Типичные ошибки

| HTTP Code | Описание | Решение |
|-----------|----------|---------|
| 401 | Invalid API key | Проверьте `api_key` |
| 403 | Access denied | Проверьте права на пакет |
| 404 | Package not found | Проверьте `package_key` |
| 422 | Validation error | Проверьте параметры запроса |
| 429 | Rate limit exceeded | Уменьшите частоту запросов |
| 500 | Server error | Повторите запрос позже |

### Пример обработки ошибок

```python
try:
    regions = await client.get_regions("us", "wifi")
except httpx.HTTPStatusError as e:
    if e.response.status_code == 401:
        print("Invalid API key")
    elif e.response.status_code == 404:
        print("Package not found")
    else:
        print(f"API error: {e.response.status_code}")
except httpx.RequestError as e:
    print(f"Network error: {e}")
```

---

## Notes

1. **ISO коды стран** - всегда в lowercase (`us`, `de`, `ru`, `ua`)
2. **conn_type** - зависит от типа пакета:
   - Wi-Fi (Residential) пакеты: только `wifi`
   - Mobile пакеты: только `mobile`
3. **Whitelist** - требуется для IP-авторизации. При login/password авторизации можно не использовать (режим "Any IP")
4. **Rate limits** - не документированы, но рекомендуется не более 10 запросов/сек
5. **Session management** - используйте `sessid` и `sesstime` для sticky sessions

---

## Links

- Dashboard: https://soax.com/dashboard
- Help Center: https://helpcenter.soax.com/
- Postman Collection: https://helpcenter.soax.com/ (в разделе API)
