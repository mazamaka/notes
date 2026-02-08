# Antifraud Knowledge Base

## Как использовать эту базу знаний

При работе с антифрод/антидетект кодом используй материалы из этой папки.

### Быстрый поиск по темам

| Тема | Файл |
|------|------|
| Canvas/WebGL fingerprint | `05-webgl-fingerprint.md`, `09-canvas-fake-of-fakes.md` |
| WebGPU | `03-webgpu-new-system.md`, `04-webgpu-performance.md` |
| Audio fingerprint | `08-audiocontext.md` |
| WASM fingerprint | `07-webassembly-fingerprint.md` |
| DNS как идентификатор | `02-dns-identifier.md` |
| Сетевые отпечатки TCP/UDP/QUIC | `10-m1d-m1d1.md` |
| VPN/Proxy детект | `12_VPN_Detection_Geolocation.md` |
| Анонимность браузера | `13_Anonymity_Deanonymization.md` |
| Виртуальные машины | `15_VM_Detection_Bypass.md` |
| OpenWRT роутер | `14_Cloud_AntiDetect_Router.md` |

### Ключевые выводы (запомни!)

1. **Benchmark важнее Hash** — антифрод измеряет производительность, не хеши
2. **SOCKS5 умирает** — M1D детектит 100%, нужна полная поддержка UDP/QUIC
3. **DNS = fingerprint** — данные шарятся между Google, банками, Meta
4. **Публичные чекеры = ханипоты** — BrowserLeaks, fingerprint.com собирают данные
5. **VirtualBox OSE** — единственный гипервизор с открытым кодом для маскировки

### Для веб-доступа (после настройки GitHub Pages)

```
WebFetch("https://mazamaka.github.io/notes/antifraud-course/llms.txt")
```

### Полные транскрипты

В папке `transcripts/` — .txt, .json, .srt файлы с полным текстом вебинаров.
