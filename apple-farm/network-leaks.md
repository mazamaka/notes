---
title: "Утечки сети при регистрации Apple аккаунтов через Octo Browser"
description: "DNS, WebRTC, timezone, системные утечки macOS — как Apple определяет реальную сеть и как это исправить"
---

# Утечки сети при регистрации Apple аккаунтов через Octo Browser

## Проблема

При работе на маке в домашней сети — поначалу регистрация проходит, но потом Apple начинает блокировать. Смена WiFi (кафе) помогает временно. Причина — утечки реального IP/сети на системном уровне, несмотря на проксирование трафика браузера через Octo.

---

## Как Apple определяет реальную сеть

### 1. DNS Leaks — главная проблема

macOS отправляет DNS-запросы **напрямую через системный DNS** (роутер/ISP), а не через прокси. Octo проксирует HTTP/SOCKS трафик, но DNS-резолвинг идёт мимо:

- Apple видит: прокси-IP = Бразилия, а DNS-запросы идут через провайдера в твоём городе
- Это мгновенный флаг

**Проверить:** открыть в Octo-профиле `https://browserleaks.com/dns` или `https://ipleak.net` — если там провайдерский DNS, утечка есть.

### 2. WebRTC Leaks

При создании профиля Octo **не указываются WebRTC настройки** (`src/services/octo.py:289`):

```python
payload = {
    "title": name,
    "extensions": [...],
    "fingerprint": self._generate_fingerprint(octo_os, noise),
}
```

Fingerprint содержит только `os` + `noise`, но **нет `webRTC` mode**. По умолчанию Octo может пропускать реальный IP через WebRTC STUN-запросы.

**Проверить:** `https://browserleaks.com/webrtc` в Octo-профиле.

### 3. Timezone Mismatch

В профиле **не задаётся timezone** под геолокацию прокси. Если прокси в Бразилии, а на маке системное время MSK — Apple видит несоответствие.

### 4. Системные утечки macOS

macOS **параллельно с браузером** делает свои запросы к Apple:

- **OCSP проверки сертификатов** (`ocsp.apple.com`) — с реального IP
- **iCloud/Apple ID фоновые синки** — с реального IP
- **mDNS/Bonjour** — broadcast в локальной сети
- **Captive Portal Detection** — при подключении к WiFi

Apple может коррелировать: "сессия регистрации через прокси Бразилии, а 5 минут назад с этого же мака шёл OCSP-запрос с IP домашнего провайдера".

### 5. IP Reputation & Rate Limiting

Домашний IP не меняется. Apple помечает IP после N регистраций. В кафе "работает" потому что свежий IP, но потом тоже банится.

---

## Сводная таблица утечек

| Тип утечки | Риск | Как проверить | Как исправить |
|------------|------|---------------|---------------|
| DNS Leak | Критический | browserleaks.com/dns | Proxifier / DNS-over-HTTPS |
| WebRTC Leak | Высокий | browserleaks.com/webrtc | Настройка webRTC в Octo профиле |
| Timezone Mismatch | Средний | browserleaks.com/javascript | timezone: auto в профиле |
| Системные запросы macOS | Высокий | Little Snitch / Wireshark | Файрвол / VM |
| IPv6 Leak | Средний | ipleak.net | networksetup -setv6off |
| IP Reputation | Высокий | — | Ротация IP / мобильные прокси |

---

## Решения

### A. Фиксы в коде Octo (быстрые)

Добавить в fingerprint при создании профиля (`src/services/octo.py`):

```python
{
    "webRTC": {
        "mode": "altered",        # подменяет IP на IP прокси
        "publicIp": "<proxy_ip>",
        "localIps": ["10.0.0.1"]
    },
    "timezone": {
        "mode": "auto"            # автоматически под геолокацию прокси
    },
    "geolocation": {
        "mode": "auto"            # автоматически под прокси
    }
}
```

### B. Системный уровень (macOS)

1. **Блокировка системных Apple-запросов через файрвол:**
   ```bash
   # Little Snitch или Lulu — блокировать исходящие на *.apple.com кроме браузера
   # Или через pf firewall
   ```

2. **DNS на системном уровне через прокси:**
   ```bash
   # DNS-over-HTTPS через прокси
   # Или Proxifier/Proxychains для проксирования ВСЕГО трафика мака
   ```

3. **Отключить IPv6** на сетевом интерфейсе:
   ```bash
   sudo networksetup -setv6off Wi-Fi
   ```

### C. Правильная архитектура (надёжный вариант)

Запускать Octo внутри VM или контейнера, где ВЕСЬ трафик (включая DNS, системные запросы) идёт через VPN/прокси той же страны что и профиль:

1. **VM (Parallels/UTM)** с macOS или Windows → внутри VPN в стране прокси → внутри Octo
2. **Proxifier** на хостовом маке — завернуть весь трафик Octo + системных процессов через SOCKS-прокси
3. **Разные реальные IP для каждой сессии** — мобильный хотспот с ротацией IP

### D. Почему кафе работает (временно)

- Свежий, небанённый IP
- Другой DNS-провайдер
- Apple не видел с него массовых регистраций
- Но тоже быстро помечается после нескольких регистраций

---

## Чеклист проверки перед регистрацией

1. [ ] Открыть `https://browserleaks.com/webrtc` — реальный IP не должен светиться
2. [ ] Открыть `https://browserleaks.com/dns` — DNS сервера должны быть из страны прокси
3. [ ] Открыть `https://ipleak.net` — проверить IP, DNS, WebRTC, IPv6
4. [ ] Проверить timezone в `https://browserleaks.com/javascript` — должен соответствовать стране прокси
5. [ ] Убедиться что IPv6 отключён (`sudo networksetup -setv6off Wi-Fi`)
6. [ ] Убедиться что Proxifier/VPN заворачивает системный трафик
