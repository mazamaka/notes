---
title: "Octo Browser API FAQ -- справочник"
description: "Часто задаваемые вопросы по Octo Browser API: лимиты, запуск, массовые операции"
source: "https://documenter.getpostman.com/view/1801428/UVC6i6eA"
---

# Octo Browser API FAQ

Официальная документация: https://documenter.getpostman.com/view/1801428/UVC6i6eA

## Лимиты API

### Rate Limits (по тарифу)
- **RPM** (requests per minute): 500
- **RPH** (requests per hour): 15000

### Заголовки ответа сервера
```
Retry-After: 0                    # Если 0 — можете слать следующий запрос
X-Ratelimit-Limit: 200            # RPM — общий лимит запросов в минуту
X-Ratelimit-Limit-Hour: 3000      # RPH — общий лимит запросов в час
X-Ratelimit-Remaining: 4          # remaining RPM — оставшееся кол-во запросов в минуту
X-Ratelimit-Remaining-Hour: 2999  # remaining RPH — оставшееся кол-во запросов в час
X-Ratelimit-Reset: 1671789217     # unix timestamp — время сброса лимита
```

### Ошибка 429 (Too Many Requests)
Остановите скрипт и приостановите запросы. **ВАЖНО:** Не отправляйте запросы при исчерпанных лимитах — время ограничения будет увеличено и могут быть применены более строгие ограничения.

### Какие запросы расходуют лимиты

**Расходуют лимиты:**
- `Start Profile` — считается как **1 запрос**
- `One-time profile` — считается как **4 запроса**

**НЕ расходуют лимиты:**
- `List Active Profiles`
- `Stop Profile`
- `Force Stop Profile`
- `Login`
- `Logout`
- `Get Client Version`
- `Update Client`
- `Username`
- `Set profile password`
- `Delete profile password`

---

## Local API vs Cloud API

### Local API (http://localhost:58888)
Работает с локальным клиентом Octo Browser. Не требует API токена для большинства операций.

### Cloud API (https://app.octobrowser.net/api/v2)
Работает с облачным хранилищем. Требует X-Octo-Api-Token в заголовках.

---

## Запуск профиля

### Параметры запуска
```json
{
  "uuid": "profile-uuid",
  "headless": false,
  "debug_port": true,
  "timeout": 120,
  "flags": ["--start-maximized", "--disable-backgrounding-occluded-windows"],
  "only_local": true
}
```

### Полезные флаги запуска
- `--start-maximized` — открыть окно на весь экран
- `--disable-backgrounding-occluded-windows` — корректная работа окон в фоне при параллельной автоматизации

---

## Создание профиля через API

```python
body = {
    "title": "profile_title",  # обязательное поле
    "fingerprint": {
        "os": "mac",           # обязательное: "mac" или "win"
        "os_arch": "arm",      # необязательное: "arm" или "x86" (для Intel Mac)
        "os_version": "13"     # необязательное:
                               # win: 10/11
                               # mac arm: 12/13/14/15
                               # mac x86: 12/13/14/15
    }
}
```

Полная структура параметров: POST Create Profile в документации.

---

## Частые вопросы

### Профиль запустился, но интерфейс не отображается
Проверьте параметр `headless` — должен быть `false`.

### Как получить UUID расширений
1. Подключите расширение вручную в профиль
2. Запрос GET Get Profile вернёт UUID в ответе
3. Или GET Get Extensions
4. Или `chrome://extensions/` в профиле -> Сведения -> Источник

### Как получить UUID иконки профиля
1. Сохраните иконку в профиль
2. GET Get Profile — в поле `image` будет UUID

### Как массово добавить стартовые страницы
1. Получить UUID профилей
2. PATCH Update Profile для каждого с нужными страницами

### Можно ли выгрузить куки профиля через API?
Нет, полноценный экспорт куки через API невозможен. Через библиотеки автоматизации можно получить куки только открытой страницы.

### Можно ли запустить куки-робот по API?
Нет. Реализуйте аналогичный функционал через Puppeteer/Playwright/Selenium.

### Какой драйвер для Selenium?
Chromium драйвер с версией, соответствующей ядру Octo. Версию ядра: `chrome://version` в профиле.

### Управление задачами профиля через API?
API не поддерживает методы для управления задачами профилей.

---

## Интеграция с библиотеками автоматизации

Поддерживаемые библиотеки:
- **Python:** Playwright, Pyppeteer, Selenium
- **Node.js:** Puppeteer, Playwright, Selenium

После запуска профиля с `debug_port: true` получите `ws_endpoint` для подключения библиотеки.

---

## Смена IP прокси

Если прокси поддерживает смену IP по ссылке:
```python
import requests
response = requests.get('ссылка на смену IP-адреса')
```

Octo API для этого не требуется.

---

## API эндпоинты для профилей

### Cloud API Base URL
```
https://app.octobrowser.net/api/v2/automation
```

**Заголовок авторизации:** `X-Octo-Api-Token: <your-token>`

### Local API Base URL
```
http://localhost:58888/api
```

---

### GET - Список профилей
```
GET /profiles?page=0&page_len=100&fields=title,uuid
```

**Параметры:**
- `page` — номер страницы (начиная с 0)
- `page_len` — количество профилей на странице (макс 100)
- `search` — поиск по названию
- `search_tags` — фильтр по тегам (через запятую)
- `fields` — какие поля возвращать (title, uuid, и др.)
- `ordering` — сортировка
- `status` — фильтр по статусу
- `proxies` — фильтр по прокси UUID

### GET - Профиль по UUID
```
GET /profiles/{uuid}
```

### POST - Создание профиля
```
POST /profiles
```

### PATCH - Обновление профиля
```
PATCH /profiles/{uuid}
```

### DELETE - Удаление профилей
```
DELETE /profiles
Body: {"uuids": ["uuid1", "uuid2"], "skip_trash_bin": true}
```

---

## Массовые операции (Bulk Operations)

### Проверка наличия профиля по UUID
**Прямой эндпоинт для проверки наличия профиля НЕ существует.**

Варианты реализации:
1. **GET /profiles/{uuid}** — если профиль существует, вернёт данные, иначе ошибку
2. **GET /profiles?search={title}** — поиск по названию

**Пример проверки существования:**
```python
async def profile_exists(uuid: str) -> bool:
    try:
        await octo_client.profiles.get_profile_by_uuid(uuid)
        return True
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return False
        raise
```

### Массовое создание профилей
API не имеет отдельного bulk endpoint для создания. Реализуется через цикл:

```python
async def bulk_create_profiles(profiles_data: List[Dict]) -> List[str]:
    created_uuids = []
    for data in profiles_data:
        result = await octo_client.profiles.create_profile(data)
        created_uuids.append(result["uuid"])
    return created_uuids
```

### Массовое удаление профилей
**Есть bulk endpoint:**
```
DELETE /profiles
Body: {"uuids": ["uuid1", "uuid2", ...], "skip_trash_bin": true}
```

### Массовая принудительная остановка
**Есть bulk endpoint:**
```
POST /profiles/force_stop
Body: {"uuids": ["uuid1", "uuid2", ...]}
```

### Массовый трансфер профилей
**Есть bulk endpoint:**
```
POST /profiles/transfer
Body: {"uuids": [...], "receiver_email": "user@email.com", "transfer_proxy": true}
```

### Массовый экспорт профилей
**Есть bulk endpoint:**
```
POST /profiles/export
Body: {"uuids": [...], "export_proxy": true}
```

---

## Реализованные методы в ProfilesManager

| Метод | Описание | Bulk? |
|-------|----------|-------|
| `get_profiles()` | Получить список профилей с фильтрами | Да |
| `get_profile_by_uuid(uuid)` | Получить профиль по UUID | Нет |
| `create_profile(data)` | Создать профиль | Нет |
| `update_profile(uuid, data)` | Обновить профиль | Нет |
| `delete_profiles(uuids)` | Удалить профили | Да |
| `force_stop_profile(uuid)` | Остановить профиль | Нет |
| `mass_force_stop_profiles(uuids)` | Остановить несколько | Да |
| `transfer_profiles(uuids, email)` | Перенести профили | Да |
| `export_profiles(uuids)` | Экспортировать | Да |
| `import_cookies(uuid, cookies)` | Импорт куки | Нет |

---

## Swagger и дополнительная документация

- **Swagger:** https://swagger.octobrowser.net/
- **Postman:** https://documenter.getpostman.com/view/1801428/UVC6i6eA
- **GitHub:** https://github.com/octobrowser/documentation
