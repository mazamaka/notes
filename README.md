# Notes

Knowledge base — заметки, разборы, документация для Claude-агентов.

## Подключение к агентам

```
Read tool → /Users/admin/PycharmProjects/notes/docs/<file>.md
```

## docs/ — справочники библиотек и API

| Файл | Описание |
|------|----------|
| [fastapi.md](docs/fastapi.md) | FastAPI — веб-фреймворк |
| [sqlmodel.md](docs/sqlmodel.md) | SQLModel — ORM для FastAPI |
| [sqladmin.md](docs/sqladmin.md) | SQLAdmin — админка для SQLAlchemy |
| [starlette-admin.md](docs/starlette-admin.md) | Starlette-Admin — админ-интерфейс |
| [browser-use.md](docs/browser-use.md) | Browser Use — автоматизация браузера через LLM |
| [octo-browser-api.md](docs/octo-browser-api.md) | Octo Browser — антидетект API |
| [octo-browser-faq.md](docs/octo-browser-faq.md) | Octo Browser — FAQ |
| [smspva-api.md](docs/smspva-api.md) | SMSPVA — SMS-верификация API |
| [soax-proxy-api.md](docs/soax-proxy-api.md) | SOAX — прокси API |
| [telegraph-api.md](docs/telegraph-api.md) | Telegraph — публикация статей API |
| [telegram-instant-view.md](docs/telegram-instant-view.md) | Telegram Instant View — шаблоны |

## apple-farm/ — заметки по проекту

| Файл | Описание |
|------|----------|
| [network-leaks.md](apple-farm/network-leaks.md) | Утечки сети при регистрации Apple аккаунтов |

## Публикация в Telegraph

```bash
python publish_telegraph.py <path_to_md_file>
```
