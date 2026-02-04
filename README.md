# Notes

Knowledge base — документация которой НЕТ в Context7.

Для популярных библиотек (FastAPI, SQLModel, Playwright и т.д.) используй Context7.
Здесь только уникальные доки по нишевым API и сервисам.

## Подключение к агентам

```
Glob("*.md", path="/Users/admin/PycharmProjects/notes/docs/")
Read tool → /Users/admin/PycharmProjects/notes/docs/<file>.md
```

## docs/ — уникальные API и сервисы

| Файл | Описание |
|------|----------|
| [octo-browser-api.md](docs/octo-browser-api.md) | Octo Browser — антидетект браузер API |
| [octo-browser-faq.md](docs/octo-browser-faq.md) | Octo Browser — FAQ |
| [smspva-api.md](docs/smspva-api.md) | SMSPVA — SMS-верификация API |
| [soax-proxy-api.md](docs/soax-proxy-api.md) | SOAX — прокси API |
| [telegraph-api.md](docs/telegraph-api.md) | Telegraph — публикация статей API |
| [telegram-instant-view.md](docs/telegram-instant-view.md) | Telegram Instant View — шаблоны |

## apple-farm/

| Файл | Описание |
|------|----------|
| [network-leaks.md](apple-farm/network-leaks.md) | Утечки сети при регистрации Apple аккаунтов |

## Скрипты

```bash
python publish_telegraph.py <file.md>  # опубликовать в Telegraph
```
