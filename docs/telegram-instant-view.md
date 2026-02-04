---
title: "Telegram Instant View — полная документация"
description: "Формат IV, типы правил, XPath, условия, функции, блочные функции, встроенные элементы"
---

# Telegram Instant View — Manual

## Содержание

- [Как работает IV](#как-работает-iv)
- [Последние изменения](#последние-изменения)
- [Instant View Format](#instant-view-format)
- [Поддерживаемые типы](#поддерживаемые-типы)
- [Типы правил](#типы-правил)
- [Extended XPath](#extended-xpath)
- [Условия (Conditions)](#условия-conditions)
- [Опции (Options)](#опции-options)
- [Функции (Functions)](#функции-functions)
- [Блочные функции (Block Functions)](#блочные-функции-block-functions)
- [Встроенные элементы (Embeds)](#встроенные-элементы-embeds)
- [Обработка страниц](#обработка-страниц)

---

## Как работает IV

1. Telegram проверяет, существует ли IV-шаблон для домена ссылки
2. Если шаблон есть — IV Bot загружает страницу (только `text/html`)
3. Бот применяет правила шаблона (XPath 1.0) для извлечения контента
4. Создаётся Instant View страница для отображения пользователю

---

## Последние изменения

### Сентябрь 2020

- Новая опция `~allowed_origin`
- Новая функция `@load`
- `@inline` поддерживает параметр `silent`

### Март 2019 — Version 2.1

- Поддержка `srcset` в Image и Icon (авто-выбор разрешения до 2560px)
- `@match` возвращает только совпавшие ноды
- `@replace` возвращает только изменённые ноды
- `@inline` больше не следует каноническим редиректам
- Новая функция `@split_parent`

### Декабрь 2018 — Version 2.0

**Новые свойства:** `kicker`, `site_name`

**Новые типы:** Map, Table, Details, RelatedArticles, Marked, Subscript, Superscript, Icon, PhoneLink, Reference

**Новые типы правил:** Options, Block functions

**Новые функции:** `@wrap_inner`, `@style_to_attrs`

**Другое:**
- XPath результаты можно добавлять в переменные через `+`
- Новая XPath функция `ends-with`
- Списки могут содержать блочные элементы (параграфы, вложенные списки, таблицы)
- Поддержка `<cite>` в медиа-подписях
- Поддержка ссылок на изображениях (`href` атрибут)
- Улучшенная функция `@simplify`

---

## Instant View Format

IV страница — объект со следующими свойствами:

| Свойство | Тип | Описание |
|----------|-----|----------|
| **title** (обяз.) | RichText | Заголовок страницы |
| subtitle | RichText | Подзаголовок |
| kicker | RichText | Кикер |
| author | String | Имя автора |
| author_url | Url | Ссылка на автора |
| published_date | Unixtime | Дата публикации |
| description | String | Краткое описание (для превью) |
| image_url | Url | Фото для превью |
| document_url | Url | Документ для превью |
| site_name | String | Название сайта (для превью) |
| channel | String | Telegram-канал автора (@username) |
| cover | Media | Обложка страницы |
| **body** (обяз.) | Article | Контент страницы |

### RTL поддержка

Если `<html>` или элемент `body` имеет атрибут `dir="rtl"`, страница отмечается как RTL:

```
@set_attr(dir, "rtl"): $body
@set_attr(dir, "rtl"): /html
```

---

## Поддерживаемые типы

### Основные блоки

| Тип | HTML-аналог | Описание |
|-----|-------------|----------|
| Article | `<article>` | Контент страницы |
| Header | `<h1>`–`<h4>` (верхний уровень) | Основной заголовок |
| Subheader | `<h5>`–`<h6>` и оставшиеся `<h1>`–`<h4>` | Подзаголовок |
| Paragraph | `<p>` | Параграф |
| Preformatted | `<pre>` + опц. `data-language` | Форматированный текст |
| Anchor | `<anchor name="...">` | Якорь |
| Divider | `<hr>` | Разделитель |
| List | `<ul>`, `<ol>` | Список |
| ListItem | `<li>` | Элемент списка (в v2.0 может содержать блоки) |
| Blockquote | `<blockquote>` | Цитата |
| Pullquote | `<aside>` | Выделенная цитата |
| Footer | `<footer>` | Подвал |

### Медиа

| Тип | HTML-аналог | Описание |
|-----|-------------|----------|
| Media | `<figure>` | Медиа-контейнер |
| Image | `<img src="...">` | Изображение (GIF, JPG, PNG). Поддержка `srcset` в v2.1 |
| Video | `<video src="...">` | Видео |
| Audio | `<audio src="...">` | Аудио (ogg, mpeg, mp4) |
| Embed | `<iframe src="...">` | Встроенный элемент |
| Map | `<img>`/`<iframe>` с Google/Yandex Maps | Карта |
| Slideshow | `<slideshow>` | Слайдшоу |
| MediaCaption | `<figcaption>` | Подпись медиа (+ `<cite>` в v2.0) |

### Таблицы (v2.0+)

| Тип | HTML-аналог | Описание |
|-----|-------------|----------|
| Table | `<table>` | Таблица |
| TableCaption | `<caption>` | Подпись таблицы |
| TableRow | `<tr>` | Строка (опц. `align`, `valign`, обёртка `<thead>`/`<tbody>`/`<tfoot>`) |
| TableCell | `<td>`, `<th>` | Ячейка (опц. `align`, `valign`, `colspan`, `rowspan`) |

### Details (v2.0+)

| Тип | HTML-аналог | Описание |
|-----|-------------|----------|
| Details | `<details>` | Сворачиваемый блок (опц. `open`) |
| DetailsHeader | `<summary>` | Заголовок сворачиваемого блока |

### RelatedArticles

`<related>` — содержит `<h1>`–`<h6>` заголовок и `<a href="...">` ссылки. Отображаются только статьи с IV.

### Форматирование текста (RichText)

| Тип | HTML-аналог |
|-----|-------------|
| Bold | `<b>`, `<strong>` |
| Italic | `<i>`, `<em>` |
| Underline | `<u>`, `<ins>` |
| Strike | `<s>`, `<del>`, `<strike>` |
| Fixed | `<code>`, `<kbd>`, `<samp>`, `<tt>` |
| Marked | `<mark>` |
| Subscript | `<sub>` |
| Superscript | `<sup>` |
| Icon | `<pic src="..." width="..." height="...">` |
| Link | `<a href="...">` |
| EmailLink | `<a href="mailto:...">` |
| PhoneLink | `<a href="tel:...">` |
| Reference | `<reference name="...">` |
| LineBreak | `<br>` |

> **Подсветка кода:** Telegram пока не поддерживает подсветку, но планирует. Рекомендуется указывать `data-language` для `<pre>` блоков.

---

## Типы правил

### Условия (Conditions)

Начинаются с `?` или `!`. `?`-правила — логика OR, `!`-правила — логика AND:

```
?condition:  xpath_query   # условие
!condition:  regexp        # параметр зависит от типа
?condition                 # некоторые без параметров
```

Блоки условий разделяют набор правил на группы:

```
?exists: //article
?exists: //div[@id="article"]
!exists: //meta[@property="og:title"]
# Правила выполнятся если <article> ИЛИ <div id="article"> найдены
# И при этом <meta property="og:title"> должен быть
```

### Свойства (Properties)

```
property:   xpath_query    # первый совпавший нод
property!:  xpath_query    # перезаписать если не пусто
property!!: xpath_query    # перезаписать даже если пусто
property:   "Some string"  # строковое значение
property!!: null            # обнулить
```

> `title` и `body` — обязательные свойства.

### Переменные (Variables)

```
$variable:  xpath_query    # список нодов
$variable?: xpath_query    # присвоить только если пусто
$variable+: xpath_query    # добавить к существующим
$variable:  "Some text"
$variable:  null
```

### Опции (Options)

```
~option: "value"           # JSON-формат значений
~option: true
```

### Функции (Functions)

```
@function:           xpath_query
@function(param):    xpath_query
@function(p1, p2):   xpath_query
@function:           "Some text"
```

### Блочные функции (Block Functions)

```
@function(xpath_query) {
  # блок правил
}
```

### Специальные переменные

- `$` — результат последнего XPath-запроса
- `$@` — результат последней выполненной функции

```
@wrap(<figure>): //img[@id="cover"]
cover:           $@
```

---

## Extended XPath

### Контекст

```
$headers:      //h1              # все <h1> на странице
article:       //article         # первый <article>
$art_headers:  $article//h1      # все <h1> внутри article
```

### Выборка конкретного нода

```
$header2:    (//h1)[2]               # второй <h1>
$last_link:  ($header2//a)[last()]   # последняя ссылка
```

### has-class

Алиас для `contains(concat(" ", normalize-space(@class), " "), " class ")`:

```
<h1>: //div[has-class("header")]
```

### ends-with

Алиас для проверки окончания строки:

```
@debug: //img[ends-with(@src, ".jpg")]
```

### prev-sibling / next-sibling

```
<figcaption>: //div[./prev-sibling::img]
@combine(<br>): //p/next-sibling::p
```

---

## Условия (Conditions)

| Условие | Формат | Описание |
|---------|--------|----------|
| `domain` | `regexp` | Домен совпадает с regex |
| `domain_not` | `regexp` | Домен НЕ совпадает |
| `path` | `regexp` | Путь совпадает с regex |
| `path_not` | `regexp` | Путь НЕ совпадает |
| `exists` | `xpath_query` | Ноды существуют |
| `not_exists` | `xpath_query` | Ноды НЕ существуют |
| `true` | — | Всегда истина |
| `false` | — | Всегда ложь |

---

## Опции (Options)

| Опция | Значение | Описание |
|-------|----------|----------|
| `~version` | `"1.0"`, `"2.0"`, `"2.1"` | Версия IV (рекомендуется 2.1) |
| `~allowed_origin` | String или Array | Разрешённые origin для `@load` и `@inline` |

```
~version: "2.1"
~allowed_origin: "https://api.example.com"
```

---

## Функции (Functions)

### Управление элементами

| Функция | Описание |
|---------|----------|
| `@remove` | Удалить ноды |
| `@replace_tag(<tag>)` или `<tag>:` | Заменить тег |
| `@wrap(<tag>)` | Обернуть в тег |
| `@wrap_inner(<tag>)` | Обернуть содержимое в тег |
| `@clone` | Копировать ноды |
| `@detach` | Отделить от родителя |
| `@split_parent` | Разбить родительский тег |

### Вставка контента

| Функция | Описание |
|---------|----------|
| `@append("text")` / `@append(<tag>)` | Добавить в конец |
| `@prepend("text")` / `@prepend(<tag>)` | Добавить в начало |
| `@after("text")` / `@after(<tag>)` | Вставить после |
| `@before("text")` / `@before(<tag>)` | Вставить перед |
| `@append_to($var)` | Переместить в конец элемента |
| `@prepend_to($var)` | Переместить в начало элемента |
| `@after_el($var)` | Переместить после элемента |
| `@before_el($var)` | Переместить перед элементом |

### Атрибуты

| Функция | Описание |
|---------|----------|
| `@set_attr(attr, value)` | Установить атрибут |
| `@set_attrs(attr, val, ...)` | Установить несколько атрибутов |
| `@style_to_attrs(css, attr)` | CSS-свойство → атрибут |

### Текст и поиск

| Функция | Описание |
|---------|----------|
| `@match(regexp)` | Поиск по regex, замена содержимого совпадением |
| `@replace(regexp, repl)` | Поиск и замена по regex |
| `@combine` / `@combine(<br>)` | Объединить с предыдущим нодом |
| `@datetime(-2)` | Текст → unixtime |

### Кодирование

| Функция | Описание |
|---------|----------|
| `@urlencode` | URL-кодирование |
| `@urldecode` | URL-декодирование |
| `@htmlencode` | HTML-кодирование спецсимволов |
| `@htmldecode` | HTML-декодирование |

### Преобразование

| Функция | Описание |
|---------|----------|
| `@background_to_image` | CSS background → `<img>` |
| `@json_to_xml` | JSON → XML |
| `@html_to_dom` | HTML-строка → DOM |
| `@pre` | Пометить текст как форматированный |
| `@inline` / `@inline(silent)` | Загрузить содержимое iframe или раскрыть HTML-комментарий |
| `@load` / `@load(silent)` | Загрузить контент по URL |

### Специальные

| Функция | Описание |
|---------|----------|
| `@debug` | Лог элементов в консоль |
| `@simplify` | Привести к IV-формату (сервисная) |
| `@unsupported` | Пометить как неподдерживаемый контент |

---

## Блочные функции (Block Functions)

### @if / @if_not

```
@if( //div[has-class("blockquote")] ) {
  <blockquote>: $@
  <cite>: $@//div[has-class("author")]
}

@if_not( $body//footer ) {
  @append(<footer>): $body
}
```

### @map

Выполняет блок для каждого нода. Переменные: `$@` (текущий), `$index`, `$first`, `$middle`, `$last`:

```
@map( //div[@id="list"]/p ) {
  $p: $@
  @prepend_to($p): ". "
  @prepend_to($p): $index
}
```

> `@map` медленнее обычных функций. Используйте только если нужен `$index`.

### @repeat

Выполняет блок N раз:

```
@repeat( 5 ) {
  @append_to($body): $index
  @if_not( $last ) {
    @append_to($body): ", "
  }
}
```

### @while / @while_not

```
@while( //iframe ) {
  @inline: $@
}

@while_not( //video ) {
  @inline: //iframe
}
```

> Есть лимит на общее количество итераций `map`, `repeat`, `while`, `while_not`.

---

## Встроенные элементы (Embeds)

IV автоматически распознаёт виджеты в iframe:

- YouTube
- Vimeo
- Twitter (посты и видео)
- Facebook (посты и видео)
- Instagram
- Giphy
- SoundCloud
- GitHub Gist
- Aparat
- VK.com Videos

---

## Обработка страниц

Порядок применения правил:

```
# URL: http://example.com/some_page.html
+ example.com
?true
+ ..after
```

Для поддоменов (от полного к верхнему уровню):

```
# URL: http://some.subdomain.example.com/some_page.html
+ some.subdomain.example.com
?not_exists: $body
+ subdomain.example.com
?not_exists: $body
+ example.com
?true
+ ..after
```

`..after` — специальный блок, применяемый ко всем страницам независимо от домена.

### Работа с поддоменами

В IV-редакторе можно выбрать уровень домена для шаблона через меню в левом верхнем углу. Выбирайте уровень со страницами одинаковой структуры.

> Пример: для `https://en.wikipedia.org/wiki/...` используйте `wikipedia.org`, т.к. структура не зависит от языка.
