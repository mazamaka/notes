---
title: "Telegraph API — полная документация"
description: "Методы, типы, формат контента Telegraph API для публикации статей на telegra.ph"
---

# Telegraph API

Telegra.ph — минималистичный инструмент публикации, позволяющий создавать форматированные посты и публиковать их в один клик. Посты Telegraph также получают Instant View в Telegram.

Бот [@Telegraph](https://t.me/telegraph) предоставляет расширенные возможности: управление статьями на разных устройствах и статистику просмотров.

API открыт для всех разработчиков — можно создавать ботов или standalone-интерфейсы для любой платформы.

---

## Формат запросов

Все запросы через HTTPS:

```
https://api.telegra.ph/{method}
```

Если есть path-параметр:

```
https://api.telegra.ph/{method}/{path}
```

Поддерживаются GET и POST. Ответ — JSON с полем `ok` (Boolean). При `ok: true` результат в `result`, при `ok: false` ошибка в `error`. Все запросы в UTF-8.

---

## Методы

### createAccount

Создание нового аккаунта Telegraph. Возвращает `Account` с дополнительным `access_token`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `short_name` | String (1-32) | да | Имя аккаунта, отображается над кнопкой "Edit/Publish" |
| `author_name` | String (0-128) | нет | Имя автора по умолчанию |
| `author_url` | String (0-512) | нет | Ссылка профиля автора |

```
https://api.telegra.ph/createAccount?short_name=Sandbox&author_name=Anonymous
```

---

### editAccountInfo

Обновление информации аккаунта. Передавать только изменяемые параметры. Возвращает `Account`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |
| `short_name` | String (1-32) | нет | Новое имя аккаунта |
| `author_name` | String (0-128) | нет | Новое имя автора |
| `author_url` | String (0-512) | нет | Новая ссылка профиля |

```
https://api.telegra.ph/editAccountInfo?access_token=<token>&short_name=Sandbox&author_name=Anonymous
```

---

### getAccountInfo

Получение информации об аккаунте. Возвращает `Account`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |
| `fields` | Array of String | нет | Поля для возврата. Default: `["short_name","author_name","author_url"]`. Доступные: `short_name`, `author_name`, `author_url`, `auth_url`, `page_count` |

```
https://api.telegra.ph/getAccountInfo?access_token=<token>&fields=["short_name","page_count"]
```

---

### revokeAccessToken

Отзыв `access_token` и генерация нового. Возвращает `Account` с новыми `access_token` и `auth_url`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |

```
https://api.telegra.ph/revokeAccessToken?access_token=<token>
```

---

### createPage

Создание новой страницы. Возвращает `Page`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |
| `title` | String (1-256) | да | Заголовок страницы |
| `author_name` | String (0-128) | нет | Имя автора |
| `author_url` | String (0-512) | нет | Ссылка профиля автора |
| `content` | Array of Node (до 64 KB) | да | Контент страницы |
| `return_content` | Boolean | нет | Вернуть content в ответе. Default: `false` |

```
https://api.telegra.ph/createPage?access_token=<token>&title=Sample+Page&author_name=Anonymous&content=[{"tag":"p","children":["Hello,+world!"]}]&return_content=true
```

---

### editPage

Редактирование существующей страницы. Возвращает `Page`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |
| `path` | String | да | Путь к странице |
| `title` | String (1-256) | да | Заголовок |
| `content` | Array of Node (до 64 KB) | да | Контент страницы |
| `author_name` | String (0-128) | нет | Имя автора |
| `author_url` | String (0-512) | нет | Ссылка профиля автора |
| `return_content` | Boolean | нет | Вернуть content в ответе. Default: `false` |

```
https://api.telegra.ph/editPage/Sample-Page-12-15?access_token=<token>&title=Sample+Page&author_name=Anonymous&content=[{"tag":"p","children":["Hello,+world!"]}]&return_content=true
```

---

### getPage

Получение страницы. Возвращает `Page`.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `path` | String | да | Путь к странице (формат `Title-12-31` — всё после `http://telegra.ph/`) |
| `return_content` | Boolean | нет | Вернуть content. Default: `false` |

```
https://api.telegra.ph/getPage/Sample-Page-12-15?return_content=true
```

---

### getPageList

Список страниц аккаунта. Возвращает `PageList`, отсортированный по дате создания (новые первые).

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `access_token` | String | да | Токен доступа |
| `offset` | Integer | нет | Смещение. Default: `0` |
| `limit` | Integer (0-200) | нет | Лимит страниц. Default: `50` |

```
https://api.telegra.ph/getPageList?access_token=<token>&limit=3
```

---

### getViews

Статистика просмотров страницы. Возвращает `PageViews`. По умолчанию — общее число просмотров.

| Параметр | Тип | Обязательный | Описание |
|----------|-----|:---:|----------|
| `path` | String | да | Путь к странице |
| `year` | Integer (2000-2100) | условно | Обязателен если передан `month` |
| `month` | Integer (1-12) | условно | Обязателен если передан `day` |
| `day` | Integer (1-31) | условно | Обязателен если передан `hour` |
| `hour` | Integer (0-24) | нет | Просмотры за конкретный час |

```
https://api.telegra.ph/getViews/Sample-Page-12-15?year=2016&month=12
```

---

## Типы

### Account

Аккаунт Telegraph.

| Поле | Тип | Описание |
|------|-----|----------|
| `short_name` | String | Имя аккаунта |
| `author_name` | String | Имя автора по умолчанию |
| `author_url` | String | Ссылка профиля автора |
| `access_token` | String | *Optional.* Только от `createAccount` и `revokeAccessToken` |
| `auth_url` | String | *Optional.* URL авторизации браузера (одноразовый, 5 минут) |
| `page_count` | Integer | *Optional.* Количество страниц аккаунта |

---

### PageList

Список статей аккаунта (новые первые).

| Поле | Тип | Описание |
|------|-----|----------|
| `total_count` | Integer | Общее число страниц |
| `pages` | Array of Page | Запрошенные страницы |

---

### Page

Страница Telegraph.

| Поле | Тип | Описание |
|------|-----|----------|
| `path` | String | Путь к странице |
| `url` | String | URL страницы |
| `title` | String | Заголовок |
| `description` | String | Описание |
| `author_name` | String | *Optional.* Имя автора |
| `author_url` | String | *Optional.* Ссылка профиля автора |
| `image_url` | String | *Optional.* URL изображения страницы |
| `content` | Array of Node | *Optional.* Контент страницы |
| `views` | Integer | Количество просмотров |
| `can_edit` | Boolean | *Optional.* `true` если аккаунт может редактировать страницу |

---

### PageViews

| Поле | Тип | Описание |
|------|-----|----------|
| `views` | Integer | Количество просмотров |

---

### Node

Абстрактный DOM-узел. Может быть `String` (текстовый узел) или объект `NodeElement`.

---

### NodeElement

DOM-элемент.

| Поле | Тип | Описание |
|------|-----|----------|
| `tag` | String | Имя тега. Доступные: `a`, `aside`, `b`, `blockquote`, `br`, `code`, `em`, `figcaption`, `figure`, `h3`, `h4`, `hr`, `i`, `iframe`, `img`, `li`, `ol`, `p`, `pre`, `s`, `strong`, `u`, `ul`, `video` |
| `attrs` | Object | *Optional.* Атрибуты элемента. Доступные: `href`, `src` |
| `children` | Array of Node | *Optional.* Дочерние узлы |

---

## Content format

Telegraph API использует DOM-формат для представления контента. Пример на JavaScript:

### DOM → Node (для отправки в API)

```javascript
function domToNode(domNode) {
  if (domNode.nodeType == domNode.TEXT_NODE) {
    return domNode.data;
  }
  if (domNode.nodeType != domNode.ELEMENT_NODE) {
    return false;
  }
  var nodeElement = {};
  nodeElement.tag = domNode.tagName.toLowerCase();
  for (var i = 0; i < domNode.attributes.length; i++) {
    var attr = domNode.attributes[i];
    if (attr.name == 'href' || attr.name == 'src') {
      if (!nodeElement.attrs) {
        nodeElement.attrs = {};
      }
      nodeElement.attrs[attr.name] = attr.value;
    }
  }
  if (domNode.childNodes.length > 0) {
    nodeElement.children = [];
    for (var i = 0; i < domNode.childNodes.length; i++) {
      var child = domNode.childNodes[i];
      nodeElement.children.push(domToNode(child));
    }
  }
  return nodeElement;
}
```

### Node → DOM (для рендеринга из API)

```javascript
function nodeToDom(node) {
  if (typeof node === 'string' || node instanceof String) {
    return document.createTextNode(node);
  }
  if (node.tag) {
    var domNode = document.createElement(node.tag);
    if (node.attrs) {
      for (var name in node.attrs) {
        var value = node.attrs[name];
        domNode.setAttribute(name, value);
      }
    }
  } else {
    var domNode = document.createDocumentFragment();
  }
  if (node.children) {
    for (var i = 0; i < node.children.length; i++) {
      var child = node.children[i];
      domNode.appendChild(nodeToDom(child));
    }
  }
  return domNode;
}
```

### Пример создания страницы

```javascript
var article = document.getElementById('article');
var content = domToNode(article).children;

$.ajax('https://api.telegra.ph/createPage', {
  data: {
    access_token:   '%access_token%',
    title:          'Title of page',
    content:        JSON.stringify(content),
    return_content: true
  },
  type: 'POST',
  dataType: 'json',
  success: function(data) {
    if (data.content) {
      while (article.firstChild) {
        article.removeChild(article.firstChild);
      }
      article.appendChild(nodeToDom({children: data.content}));
    }
  }
});
```
