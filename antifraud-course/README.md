# Курс по антифрод-системам от Вектор Т13

**Транскрибировано:** 2026-02-08
**Количество уроков:** 15
**Общая длительность:** ~8 часов
**LLM Index:** [llms.txt](llms.txt)

---

## Содержание курса

| # | Урок | Длительность | Ключевые темы |
|---|------|--------------|---------------|
| 01 | [Chase Antifraud](01-chase-antifraud.md) | 30 мин | ThreatMetrix, Akamai, HAR-анализ |
| 02 | [DNS Identifier](02-dns-identifier.md) | 56 мин | DNS как fingerprint, M3AAWG, прогрев прокси |
| 03 | [WebGPU New System](03-webgpu-new-system.md) | 18 мин | WebGL deprecated, WebGPU benchmark |
| 04 | [WebGPU Performance](04-webgpu-performance.md) | 13 мин | Atomic Fingerprint, V-Sec 2025 |
| 05 | [WebGL Fingerprint](05-webgl-fingerprint.md) | 25 мин | FPS benchmark, 43-48 = детект |
| 06 | [Browser FM](06-browser-fm.md) | 17 мин | 16000 параметров, Fuzzy Hashing |
| 07 | [WebAssembly Fingerprint](07-webassembly-fingerprint.md) | 13 мин | WASM, 99% точность, Microsoft |
| 08 | [AudioContext](08-audiocontext.md) | 20 мин | CPU fingerprint, не Audio |
| 09 | [Canvas Fake of Fakes](09-canvas-fake-of-fakes.md) | 31 мин | CPU vs GPU Canvas, 10 лет фейка |
| 10 | [M1D и M1D1](10-m1d-m1d1.md) | 43 мин | TCP+UDP+QUIC, SOCKS5 умрёт |
| 11 | [Free Antifraud](11-free-antifraud-system.md) | 8 мин | IPQS Enterprise бесплатно |
| 12 | [VPN Detection & Geolocation](12_VPN_Detection_Geolocation.md) | 60 мин | 10 методов геолокации, Maxmind, ASN |
| 13 | [Anonymity & Deanonymization](13_Anonymity_Deanonymization.md) | 90 мин | Браузеры, TPM, ультразвук, крипто |
| 14 | [Cloud AntiDetect Router](14_Cloud_AntiDetect_Router.md) | 35 мин | OpenWRT на VPS, MTU 1500, QUIC |
| 15 | [VM Detection & Bypass](15_VM_Detection_Bypass.md) | 60 мин | VirtualBox OSE, античиты, CPUID |

---

## Быстрый доступ по темам

### Fingerprinting

| Технология | Урок | Ключевой вывод |
|------------|------|----------------|
| Canvas | [09](09-canvas-fake-of-fakes.md) | CPU Canvas ~400 вариантов, антидетекты не различают |
| WebGL | [05](05-webgl-fingerprint.md) | FPS важнее hash, 43-48 = детект |
| WebGPU | [03](03-webgpu-new-system.md), [04](04-webgpu-performance.md) | Atomic Fingerprint 70%, benchmark |
| Audio | [08](08-audiocontext.md) | Это CPU fingerprint, не audio |
| WASM | [07](07-webassembly-fingerprint.md) | 99% точность, уже используется |
| Browser FM | [06](06-browser-fm.md) | 16000 параметров, 99.7% точность |

### Сетевые отпечатки

| Стек | Урок | Эффективность |
|------|------|---------------|
| TCP (Zardax) | [10](10-m1d-m1d1.md) | 60% идентификация ОС |
| M1D (TCP+UDP) | [10](10-m1d-m1d1.md) | 100% детект SOCKS5 |
| M1D1 (TCP+UDP+QUIC) | [10](10-m1d-m1d1.md) | 95% идентификация пользователя |
| DNS | [02](02-dns-identifier.md) | Шаринг данных между компаниями |

### Антифрод-системы

| Система | Урок | Особенности |
|---------|------|-------------|
| ThreatMetrix | [01](01-chase-antifraud.md), [10](10-m1d-m1d1.md) | TURN протокол, M1D пионер |
| Akamai | [01](01-chase-antifraud.md) | Репутация IP, латентность |
| IP Quality Score | [11](11-free-antifraud-system.md) | Enterprise бесплатно через Indeed |
| CyberSource | [07](07-webassembly-fingerprint.md) | WASM fingerprint |
| PerimeterX | [07](07-webassembly-fingerprint.md) | WASM начальная стадия |

---

## Главные выводы курса

### 1. Benchmark важнее Hash

Подмена hash (Canvas, WebGL, Audio) бесполезна. Антифрод измеряет **производительность**:
- WebGL FPS: 43-48 = VM/VPS/Bot
- Audio: 45-50 мс = VM/VPS
- Canvas: benchmark не детектит VM

### 2. SOCKS5 скоро умрёт

M1D (TCP+UDP) детектит SOCKS5 со 100% вероятностью:
- Нет поддержки UDP
- Нет поддержки QUIC
- Поведение нехарактерное для пользователя

### 3. DNS = такой же идентификатор как IP

Google/Cloudflare шарят данные с банками, Meta, Microsoft через организации:
- M3AAWG
- FS-ISAC
- APWG
- Cyber Threat Alliance

### 4. Публичные чекеры = ханипоты

- BrowserLeaks
- fingerprint.com
- Любые "бесплатные" чекеры

### 5. Прогрев прокси обязателен

1. Установить на всю систему (не только браузер)
2. Генерировать легитимный трафик (YouTube, обновления)
3. Не проверять через чекеры
4. Не использовать публичные DNS

---

## Инструменты

| Инструмент | Назначение | Урок |
|------------|------------|------|
| chrome://net-export | Логирование сетевого трафика | [10](10-m1d-m1d1.md) |
| netlog-viewer | Анализ QUIC/UDP | [10](10-m1d-m1d1.md) |
| TCP Optimizer | Изменение сетевых параметров | [10](10-m1d-m1d1.md) |
| DNS Benchmark | Проверка DNS серверов | [02](02-dns-identifier.md) |
| DetectExpert | Чекеры от автора курса | Все |
| HAR Export | Анализ запросов | [01](01-chase-antifraud.md) |

---

## Транскрипты

Полные транскрипты находятся в `/transcripts/`:
- `.txt` - текст
- `.json` - с таймкодами
- `.srt` / `.vtt` - субтитры

---

## Автор

**Вектор Т13** - разработчик антидетект-систем, исследователь антифрод-технологий.

---

*База знаний создана для Claude агента*
