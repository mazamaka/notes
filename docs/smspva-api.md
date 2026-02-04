---
title: "SMSPVA API -- документация"
description: "API для получения виртуальных номеров и SMS-верификации (Activation + Rental)"
source: "https://smspva.com"
---

# SMSPVA API Documentation

> API для получения виртуальных номеров и SMS-верификации

**Base URL:** `https://api.smspva.com` (Activation API v2)
**Rental URL:** `https://smspva.com/api/rent.php`

## Rate Limits

- До 50 подключений в секунду
- Интервал между запросами: 4-5 секунд
- SMS приходит в течение 10 минут (580 секунд)

---

## Activation API v2

### Авторизация

Все запросы требуют header `apikey`:
```
apikey: YOUR_API_KEY
```

### Get Number

Получить номер для активации.

```http
GET /activation/number/{country}/{service}
```

| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| country | string | Да | ISO 3166-2 код страны (например: `US`, `UK`, `KZ`) |
| service | string | Да | Код сервиса (например: `opt131` для Apple) |
| operator | string | Нет | Оператор (если не указан -- выбирается случайно) |

**Пример:**
```bash
curl -X GET "https://api.smspva.com/activation/number/US/opt131" \
  -H "apikey: YOUR_API_KEY"
```

**Ответ (200):**
```json
{
  "statusCode": 200,
  "data": {
    "orderId": 123456,
    "phoneNumber": 9876544321,
    "countryCode": "US",
    "orderExpireIn": 600
  }
}
```

### Receive SMS

Получить SMS с кодом активации.

```http
GET /activation/sms/{orderId}
```

| Параметр | Тип | Обязательный | Описание |
|----------|-----|--------------|----------|
| orderId | integer | Да | ID заказа из ответа get number |

**Ответ (200) - SMS получено:**
```json
{
  "statusCode": 200,
  "data": {
    "sms": {
      "code": "1234",
      "fullText": "Your activation code is 1234"
    },
    "orderId": "123456",
    "orderExpireIn": 600
  }
}
```

**Ответ (202) - SMS ещё не пришло:**
```json
{
  "statusCode": 202,
  "data": {
    "orderId": "123456",
    "orderExpireIn": 580
  }
}
```

### Get Balance

```http
GET /activation/balance
```

### Get User Info

```http
GET /activation/userinfo
```

### Get Service Price

```http
GET /activation/serviceprice/{country}/{service}
```

### Clear SMS (для повторного получения)

```http
PUT /activation/clearsms/{orderId}
```

Удаляет текущее SMS для получения нового на тот же номер.

### Cancel Order

```http
PUT /activation/cancelorder/{orderId}
```

Отмена заказа (возврат средств).

### Block Number

```http
PUT /activation/blocknumber/{orderId}
```

Пометить номер как нерабочий (возврат средств).

### Get Current Orders

```http
GET /activation/orders
```

---

## Rental API (Аренда номеров)

### Create Rent Order

```http
GET /api/rent.php?method=create&apikey={key}&dtype={type}&dcount={count}&country={country}&service={service}
```

| Параметр | Тип | Описание |
|----------|-----|----------|
| method | string | `create` |
| apikey | string | API ключ |
| dtype | string | Период: `week` или `month` |
| dcount | integer | Количество периодов |
| country | string | Код страны |
| service | string | Код сервиса |
| provider | string | Провайдер (опционально) |

**Пример:**
```bash
curl "https://smspva.com/api/rent.php?method=create&apikey=YOUR_KEY&dtype=week&dcount=1&country=US&service=opt131"
```

**Ответ:**
```json
{
  "status": 1,
  "data": [
    {
      "id": 12345,
      "number": "19876543210",
      "expireAt": "2025-01-31 12:00:00"
    }
  ]
}
```

### Activate Number (перед получением SMS)

```http
GET /api/rent.php?method=activate&apikey={key}&id={orderId}
```

### Get SMS (Rental)

```http
GET /api/rent.php?method=sms&apikey={key}&id={orderId}
```

### Get Orders List

```http
GET /api/rent.php?method=orders&apikey={key}
```

### Prolong Order

```http
GET /api/rent.php?method=prolong&apikey={key}&id={orderId}&dtype=week&dcount=1
```

### Delete Order

```http
GET /api/rent.php?method=delete&apikey={key}&id={orderId}
```

### Get Rental History

```http
GET /api/rent.php?method=get_rent_history&apikey={key}&skip=0&take=10
```

---

## Status Codes

### Activation API v2

| Code | Описание |
|------|----------|
| 200 | Успех |
| 202 | SMS ещё не пришло (продолжайте опрос) |
| 404 | Заказ не найден |
| 405 | Неверный запрос |
| 406 | Ошибка авторизации |
| 407 | Номера недоступны |
| 410 | Заказ истёк |
| 411 | Сервис недоступен |
| 500 | Внутренняя ошибка сервера |
| 501 | Недостаточно средств |
| 502 | Лимит превышен |
| 503 | Сервис временно недоступен |

### Rental API

| status | Описание |
|--------|----------|
| 1 | Успех |
| 0 | Ошибка (см. поле `msg`) |

---

## Коды сервисов (важные)

| Сервис | Код | Описание |
|--------|-----|----------|
| Apple | `opt131` | Apple ID регистрация |
| Google | `opt1` | Gmail, YouTube |
| WhatsApp | `opt20` | - |
| Telegram | `opt29` | - |
| Facebook | `opt2` | - |
| Instagram | `opt16` | + Threads |
| Microsoft | `opt15` | Azure, Bing, Skype |
| Discord | `opt45` | - |
| TikTok | `opt104` | - |
| Twitter/X | `opt41` | - |
| OpenAI | `opt132` | ChatGPT, DALL-E |
| Claude | `opt196` | Anthropic |
| Steam | `opt58` | - |
| OTHER | `opt19` | Без гарантии |

Полный список: 250+ сервисов

---

## Коды стран (ISO 3166-2)

| Страна | Код |
|--------|-----|
| United States | US |
| United Kingdom | UK |
| Germany | DE |
| France | FR |
| Italy | IT |
| Spain | ES |
| Netherlands | NL |
| Poland | PL |
| Canada | CA |
| Australia | AU |
| Kazakhstan | KZ |
| Ukraine | UA |
| Russia | RU |
| Indonesia | ID |
| Philippines | PH |
| Vietnam | VN |
| Thailand | TH |
| Malaysia | MY |
| Bangladesh | BD |

Полный список: 67 стран

---

## Deprecated API v1 (priemnik.php)

> Устаревший API, использовать только для совместимости

### Get Number

```http
GET /priemnik.php?metod=get_number&apikey={key}&country={country}&service={service}
```

**Ответ:**
```json
{
  "response": "1",
  "number": "9871234567",
  "id": "25623"
}
```

### Get SMS

```http
GET /priemnik.php?metod=get_sms&apikey={key}&country={country}&service={service}&id={orderId}
```

**Коды ответа:**
- `"response": "1"` -- SMS получено
- `"response": "2"` -- SMS ещё не пришло
- `"response": "3"` -- Заказ не найден
- `"response": "4"` -- Повторный просмотр SMS

---

## Alternative API (handler_api.php)

> Совместимость с SMS-Activate API

### Get Number

```http
GET /stubs/handler_api.php?action=getNumber&api_key={key}&country=0&service=go
```

**Ответ:**
```
ACCESS_NUMBER:123456:9876543210
```

### Get Status (SMS)

```http
GET /stubs/handler_api.php?action=getstatus&api_key={key}&id=123456
```

### Cancel Order

```http
GET /stubs/handler_api.php?action=setstatus&api_key={key}&id=123456&status=-1
```

---

## Workflow: Получение нескольких SMS

1. **Получить номер** -> `GET /activation/number/{country}/{service}`
2. **Опрашивать SMS** -> `GET /activation/sms/{orderId}` (каждые 5 сек)
3. **После получения SMS** -> `PUT /activation/clearsms/{orderId}`
4. **Повторить опрос** -> `GET /activation/sms/{orderId}`
5. **Завершить** или **Заблокировать номер** если SMS не пришло

---

## Best Practices

1. **Интервал запросов:** 4-5 секунд между запросами
2. **Timeout:** 10 минут (580 сек) на получение SMS
3. **Блокировка:** Если SMS не пришло за 9:40 -- заблокируйте номер
4. **Rate limit:** При ошибке `TOO MANY REQUESTS` -- уменьшите частоту
5. **Выбор оператора:** Не указывайте для автоматического выбора дешёвого
