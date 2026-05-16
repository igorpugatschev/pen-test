#!/usr/bin/env python3
"""Append lesson-specific Slider AI practice tasks and progression matrix."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"
MATRIX = ROOT / "slider_ai_progression_matrix.md"
TARGET = "https://olddev.slider-ai.ru"
HEADER = "## Практика на Slider AI"


COMMON_CONTEXT = (
    "тестовый стенд проекта Slider AI, доступен QA для обучения и проверки "
    "безопасности. Production и любые другие домены не входят в это задание."
)
COMMON_LIMITS = (
    "соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, "
    "brute force, destructive payloads, изменение чужих данных, извлечение "
    "секретов и действия вне согласованного scope."
)


TASKS = {
    "lesson_01_intro_linux.md": {
        "level": "Подготовка среды",
        "minimum": "Создайте локальную структуру `~/slider-ai-pentest/{notes,evidence,screenshots,requests}` и файл `notes/lesson_01.md`.",
        "practice": "Запишите в `lesson_01.md` разрешенную цель `https://olddev.slider-ai.ru`, ссылку на scope и правило: не тестировать production.",
        "deep": "После урока 2 добавьте команды для быстрого перехода по папкам и просмотра артефактов через терминал.",
    },
    "lesson_02_terminal.md": {
        "level": "Базовая работа в терминале",
        "minimum": "Создайте файл `notes/lesson_02_terminal.md`, добавьте дату, цель стенда и список будущих артефактов.",
        "practice": "Через `ls`, `cp`, `mv`, `cat`, `less` проверьте, что структура `slider-ai-pentest` читается и готова для хранения доказательств.",
        "deep": "После урока 6 добавьте поиск по заметкам и быстрый список всех файлов доказательств.",
    },
    "lesson_03_permissions.md": {
        "level": "Безопасное хранение артефактов",
        "minimum": "Проверьте права на папку `~/slider-ai-pentest` и убедитесь, что артефакты не доступны другим пользователям локальной машины.",
        "practice": "Создайте файл `evidence/permissions_check.txt` с выводом `ls -la` и коротким объяснением прав доступа.",
        "deep": "После урока 7 напишите скрипт, который проверяет права на все новые файлы отчета.",
    },
    "lesson_04_processes.md": {
        "level": "Контроль локальных инструментов",
        "minimum": "Запустите браузер и терминал, затем найдите их процессы через `ps` или `top`.",
        "practice": "Зафиксируйте в заметке, какие локальные процессы участвуют в ручной проверке Slider AI и как их безопасно завершить.",
        "deep": "После урока 27 добавьте Burp/ZAP в список контролируемых процессов и опишите, как остановить proxy.",
    },
    "lesson_05_network_linux.md": {
        "level": "Базовая сетевая диагностика",
        "minimum": "Определите локальный IP, DNS-настройки и доступность сети без сканирования стенда.",
        "practice": "Откройте `https://olddev.slider-ai.ru` в браузере и зафиксируйте только факт доступности страницы и время проверки.",
        "deep": "После урока 12 дополните проверку HTTP-заголовками и TLS-наблюдениями.",
    },
    "lesson_06_files_search.md": {
        "level": "Поиск в артефактах",
        "minimum": "Создайте 2-3 учебных файла заметок и найдите в них строку `olddev.slider-ai.ru` через `grep`.",
        "practice": "Соберите команду, которая находит все упоминания Slider AI в папке `notes` и сохраняет список в `evidence/search_index.txt`.",
        "deep": "После урока 40 используйте такой поиск для подготовки приложения к отчету.",
    },
    "lesson_07_bash_scripts.md": {
        "level": "Автоматизация рутины",
        "minimum": "Напишите `new_lesson_note.sh`, который создает Markdown-файл заметки по номеру урока.",
        "practice": "Добавьте в шаблон поля: цель стенда, дата, ручные шаги, результат, риск, рекомендация.",
        "deep": "После урока 12 добавьте в скрипт безопасный `curl -I` для получения заголовков стенда с явным подтверждением пользователя.",
    },
    "lesson_08_linux_summary.md": {
        "level": "Итог Linux-базы",
        "minimum": "Проведите ревизию локальной папки курса: структура есть, права корректны, заметки создаются.",
        "practice": "Оформите чек-лист готовности рабочей станции QA к проверкам Slider AI.",
        "deep": "После урока 16 добавьте в чек-лист сетевую диагностику и правила остановки проверки.",
    },
    "lesson_09_osi_model.md": {
        "level": "Модель OSI в QA-наблюдениях",
        "minimum": "Опишите, какие уровни OSI участвуют при открытии `https://olddev.slider-ai.ru` в браузере.",
        "practice": "Составьте таблицу: DNS, TCP/TLS, HTTP, UI и какие артефакты можно собирать на каждом уровне.",
        "deep": "После урока 13 подтвердите часть наблюдений через Wireshark или DevTools Network.",
    },
    "lesson_10_tcp_ip.md": {
        "level": "TCP/IP без сканирования",
        "minimum": "Проверьте, что стенд открывается по HTTPS, без перебора портов и без `nmap`.",
        "practice": "Зафиксируйте в заметке, какой хост и схема используются, какие сетевые ошибки видны при недоступности.",
        "deep": "После урока 29 выполните только разрешенную мягкую проверку открытого HTTPS-порта.",
    },
    "lesson_11_dns.md": {
        "level": "DNS-наблюдения",
        "minimum": "Определите DNS-записи `olddev.slider-ai.ru` через `dig` или `nslookup`.",
        "practice": "Сохраните A/AAAA/CNAME-результаты и объясните, что они говорят о тестовом стенде.",
        "deep": "После урока 38 сравните DNS с публичной OSINT-информацией без активного сканирования.",
    },
    "lesson_12_http_https.md": {
        "level": "HTTP/HTTPS базовая проверка",
        "minimum": "Получите только заголовки `curl -I https://olddev.slider-ai.ru`.",
        "practice": "Отметьте статус-код, redirects, security headers и cookies без изменения данных.",
        "deep": "После урока 24 оцените, какие заголовки связаны с защитой данных и сессий.",
    },
    "lesson_13_wireshark.md": {
        "level": "Пассивное наблюдение трафика",
        "minimum": "Откройте стенд в браузере и посмотрите запросы в DevTools Network.",
        "practice": "Если используете Wireshark, захватите только свой локальный трафик к стенду и сохраните список доменов/протоколов без payload.",
        "deep": "После урока 27 сравните DevTools и Burp HTTP history.",
    },
    "lesson_14_routing.md": {
        "level": "Маршрут и доступность",
        "minimum": "Проверьте маршрут до стенда через `traceroute`/`tracert` только один раз.",
        "practice": "Сохраните сокращенный вывод и отметьте, где заканчивается зона вашей ответственности как QA.",
        "deep": "После урока 61 перенесите это в раздел ограничений тестирования.",
    },
    "lesson_15_firewall.md": {
        "level": "Фильтрация и симптомы блокировок",
        "minimum": "Опишите, какие признаки в браузере/терминале могут указывать на блокировку или WAF.",
        "practice": "Сделайте одну безопасную проверку доступности страницы и зафиксируйте статус-код/ошибку.",
        "deep": "После урока 58 добавьте гипотезы WAF-поведения без обхода защит.",
    },
    "lesson_16_network_practice.md": {
        "level": "Сетевая практика без перегруза",
        "minimum": "Соберите мини-отчет доступности стенда: DNS, HTTPS-статус, redirect, базовые headers.",
        "practice": "Сравните результат из браузера и `curl -I`, отметьте расхождения в cookies/headers.",
        "deep": "После уроков 29-35 добавьте мягкие инструментальные проверки с rate limit.",
    },
    "lesson_17_owasp_intro.md": {
        "level": "OWASP-карта приложения",
        "minimum": "Составьте список функций Slider AI, которые потенциально относятся к OWASP Top 10.",
        "practice": "Не тестируя payload, отметьте точки ввода, авторизации, загрузки, API и места хранения данных.",
        "deep": "После урока 28 превратите карту в backlog security QA-проверок.",
    },
    "lesson_17b_insecure_design.md": {
        "level": "Insecure Design",
        "minimum": "Выберите один бизнес-сценарий Slider AI и опишите ожидаемые ограничения роли/состояния.",
        "practice": "Проверьте вручную один негативный сценарий без обхода авторизации и без изменения чужих данных.",
        "deep": "После урока 61 оформите этот сценарий как abuse case в RoE/тест-плане.",
    },
    "lesson_17c_security_misconfiguration.md": {
        "level": "Security Misconfiguration",
        "minimum": "Проверьте видимые признаки конфигурации: error pages, debug banners, headers, directory listing.",
        "practice": "Сохраните только неинтрузивные наблюдения из браузера/DevTools/curl.",
        "deep": "После урока 35 проверьте те же признаки passive scan в ZAP.",
    },
    "lesson_17d_vulnerable_components.md": {
        "level": "Компоненты и версии",
        "minimum": "Через DevTools посмотрите публичные JS/CSS-ресурсы и признаки библиотек без скачивания приватных данных.",
        "practice": "Составьте таблицу видимых компонентов, версий если они раскрыты, и уровня уверенности.",
        "deep": "После урока 47 сопоставьте раскрытые версии с CVE/NVD вручную или скриптом.",
    },
    "lesson_17e_software_integrity.md": {
        "level": "Integrity checks",
        "minimum": "Проверьте, загружаются ли внешние скрипты/ресурсы и есть ли SRI там, где это применимо.",
        "practice": "Зафиксируйте URL публичных ресурсов, не скачивая закрытый код и не меняя запросы.",
        "deep": "После урока 42 автоматизируйте проверку SRI/внешних доменов для одной страницы.",
    },
    "lesson_17f_logging_monitoring.md": {
        "level": "Логирование и мониторинг",
        "minimum": "Выполните один безопасный ошибочный сценарий UI и отметьте, получает ли пользователь понятное сообщение.",
        "practice": "Сформулируйте, какое событие должно попасть в серверные логи, не пытаясь читать сами логи без доступа.",
        "deep": "После урока 63 оформите рекомендацию по логированию как finding или observation.",
    },
    "lesson_18_sqli.md": {
        "level": "SQL Injection, только non-destructive",
        "minimum": "Найдите параметры поиска/фильтрации и проверьте один безвредный спецсимвол, наблюдая только ошибку/поведение.",
        "practice": "Зафиксируйте, экранируются ли символы и есть ли различия между нормальным и некорректным вводом без UNION/дампа данных.",
        "deep": "После уроков 27-28 повторите через Burp Repeater и оформите `not reproducible` или finding.",
    },
    "lesson_19_sqli_sqlmap.md": {
        "level": "SQLMap как контролируемый инструмент",
        "minimum": "Не запускайте sqlmap по Slider AI; подготовьте чек-лист условий, при которых его можно согласовать.",
        "practice": "Выберите один запрос-кандидат и сохраните его как sanitized request без cookies/секретов.",
        "deep": "После письменного разрешения и отдельного окна тестирования запланируйте dry-run с безопасными флагами.",
    },
    "lesson_20_xss.md": {
        "level": "Reflected/Stored XSS",
        "minimum": "Найдите текстовое поле и введите безопасный маркер `qa-xss-check-<date>` без script payload.",
        "practice": "Проверьте, как маркер отображается: escaped, sanitized, сохранен или отброшен.",
        "deep": "После урока 27 подтвердите encoding в HTTP-ответе через Burp/DevTools без cookie theft payload.",
    },
    "lesson_21_xss_dom.md": {
        "level": "DOM XSS",
        "minimum": "Проверьте URL-параметры и hash-фрагменты, которые меняют UI на клиенте.",
        "practice": "В DevTools найдите, попадает ли безопасный маркер из URL в DOM как текст или HTML.",
        "deep": "После урока 42 напишите скрипт, который собирает страницы с подозрительными `location`/`innerHTML` паттернами.",
    },
    "lesson_22_csrf.md": {
        "level": "CSRF",
        "minimum": "Для одной формы изменения состояния проверьте наличие CSRF-token или SameSite-cookie в DevTools.",
        "practice": "Опишите, какие условия нужны для CSRF и выполняются ли они в Slider AI.",
        "deep": "После урока 27 проверьте тот же запрос в Burp Repeater без выполнения нежелательного изменения.",
    },
    "lesson_23_broken_auth.md": {
        "level": "Authentication",
        "minimum": "Проверьте UX и сообщения ошибок при обычной неуспешной авторизации без перебора паролей.",
        "practice": "Отметьте, раскрывает ли приложение различия между неверным логином и неверным паролем.",
        "deep": "После отдельного разрешения можно спланировать rate limit test, но не запускать его в рамках урока.",
    },
    "lesson_24_sensitive_data.md": {
        "level": "Sensitive data",
        "minimum": "Через DevTools проверьте, не видны ли токены, персональные данные или секреты в URL и local/session storage.",
        "practice": "Сохраните sanitized-скриншоты без раскрытия реальных токенов и опишите риск.",
        "deep": "После урока 63 оформите finding с маскированными доказательствами.",
    },
    "lesson_25_xxe.md": {
        "level": "XXE",
        "minimum": "Определите, есть ли в Slider AI XML-upload/XML API; если нет, отметьте `not applicable`.",
        "practice": "Если XML есть, проверьте только тип контента и валидацию формата без external entity payload.",
        "deep": "После отдельного разрешения запланируйте безопасный parser-hardening тест на тестовых данных.",
    },
    "lesson_26_ssrf.md": {
        "level": "SSRF",
        "minimum": "Найдите функции, где пользователь задает URL: импорт, preview, webhook, fetch, integration.",
        "practice": "Проверьте только allowlist/validation сообщением с явно некорректным публичным URL, без обращения к внутренним адресам.",
        "deep": "После отдельного разрешения подготовьте SSRF test plan с запрещенными диапазонами и safe callback.",
    },
    "lesson_27_burp_intro.md": {
        "level": "Burp proxy setup",
        "minimum": "Настройте браузер через Burp и откройте только главную страницу Slider AI.",
        "practice": "Сохраните один GET-запрос и один ответ из HTTP history, удалив cookies и токены из артефакта.",
        "deep": "После урока 28 создайте карту основных endpoint без Intruder и без активного сканирования.",
    },
    "lesson_28_burp_practice.md": {
        "level": "Burp ручная проверка",
        "minimum": "Отправьте один безопасный запрос Slider AI в Repeater и повторите его без изменения данных.",
        "practice": "Измените только неопасный параметр отображения/поиска и сравните ответы.",
        "deep": "После урока 40 оформите результаты Repeater как доказательство для отчета.",
    },
    "lesson_29_nmap_basics.md": {
        "level": "Nmap basics",
        "minimum": "Не запускайте широкий scan; проверьте только `-Pn -p 443 --max-rate 1 olddev.slider-ai.ru` при наличии разрешения.",
        "practice": "Сохраните команду, время запуска, лимиты и результат одного HTTPS-порта.",
        "deep": "После урока 30 сравните с безопасным NSE `ssl-cert`/`http-title`, если это разрешено.",
    },
    "lesson_30_nmap_nse.md": {
        "level": "Nmap NSE safe scripts",
        "minimum": "Выберите только safe/default NSE-скрипт, не `vuln` и не intrusive.",
        "practice": "Проверьте один разрешенный скрипт против 443 и объясните, почему он безопасный.",
        "deep": "После урока 40 добавьте результат в инструментальный отчет с caveat о false positive.",
    },
    "lesson_31_amass.md": {
        "level": "Passive subdomain discovery",
        "minimum": "Не запускайте active enumeration; подготовьте список разрешенных доменов из scope.",
        "practice": "Если scope разрешает только `olddev.slider-ai.ru`, зафиксируйте, что расширение доменов не выполняется.",
        "deep": "После письменного расширения scope выполните passive-only сбор и отметьте источники.",
    },
    "lesson_32_subfinder.md": {
        "level": "Subfinder passive",
        "minimum": "Проверьте, применим ли subfinder к текущему scope; если нет, оформите `not applicable`.",
        "practice": "Не добавляйте найденные поддомены в тестирование без явного включения в scope.",
        "deep": "После урока 61 предложите процедуру согласования новых доменов в RoE.",
    },
    "lesson_33_dirsearch_ffuf.md": {
        "level": "Content discovery",
        "minimum": "Не запускайте словари по Slider AI; составьте список публичных путей, уже видимых из навигации.",
        "practice": "Проверьте вручную 3-5 видимых URL на корректные статусы и отсутствие directory listing.",
        "deep": "После отдельного разрешения запланируйте small wordlist run с 1 rps и stop conditions.",
    },
    "lesson_34_nuclei.md": {
        "level": "Nuclei controlled use",
        "minimum": "Не запускайте шаблоны nuclei по Slider AI без согласования; классифицируйте шаблоны по severity/intrusiveness.",
        "practice": "Подберите 3 safe template-кандидата и обоснуйте, почему их можно или нельзя применять.",
        "deep": "После разрешения выполните ограниченный запуск и вручную проверьте каждый результат.",
    },
    "lesson_35_owasp_zap.md": {
        "level": "ZAP passive",
        "minimum": "Откройте Slider AI через ZAP proxy и включите только passive scan.",
        "practice": "Соберите alerts passive scan, удалите cookies/tokens и классифицируйте informational vs finding.",
        "deep": "После урока 40 экспортируйте отчет ZAP и добавьте ручную валидацию.",
    },
    "lesson_36_hydra_patator.md": {
        "level": "Password attack awareness",
        "minimum": "Не запускайте Hydra/Patator по Slider AI; составьте checklist защиты от brute force.",
        "practice": "Проверьте вручную только наличие CAPTCHA/rate-limit/lockout-индикаторов без серии попыток.",
        "deep": "После отдельного письменного разрешения подготовьте план rate-limit test с лимитами и stop conditions.",
    },
    "lesson_37_searchsploit.md": {
        "level": "Exploit-DB research",
        "minimum": "Используйте SearchSploit только для изучения публичных версий компонентов, если версии раскрыты.",
        "practice": "Не применяйте эксплойты; оформите observation о риске раскрытия версии или `not enough data`.",
        "deep": "После урока 47 сопоставьте наблюдение с CVE и рекомендацией обновления.",
    },
    "lesson_38_shodan_censys.md": {
        "level": "OSINT boundaries",
        "minimum": "Проверьте только публичную информацию о `olddev.slider-ai.ru` в браузере, без запуска internet scan.",
        "practice": "Сохраните найденные публичные metadata и отметьте, что не является доказательством уязвимости.",
        "deep": "После урока 61 добавьте OSINT-границы в RoE.",
    },
    "lesson_39_tools_practice.md": {
        "level": "Toolchain planning",
        "minimum": "Соберите безопасный pipeline проверки Slider AI без запуска intrusive инструментов.",
        "practice": "Для каждого инструмента укажите режим: manual/passive/low-rate/forbidden.",
        "deep": "После урока 40 превратите pipeline в отчетный чек-лист с evidence slots.",
    },
    "lesson_40_reporting.md": {
        "level": "First Slider AI report",
        "minimum": "Оформите один informational finding по уже выполненной безопасной проверке.",
        "practice": "Заполните поля: компонент, шаги, фактический результат, риск, рекомендация, retest.",
        "deep": "После урока 64 добавьте CVSS только для подтвержденных уязвимостей, не для observations.",
    },
    "lesson_41_python_sockets.md": {
        "level": "Python sockets safely",
        "minimum": "Запустите сканер только на `127.0.0.1`, не на Slider AI.",
        "practice": "Адаптируйте код так, чтобы он явно отказывался сканировать домены вне allowlist и сохранял предупреждение.",
        "deep": "После урока 44 сравните свой код с результатом одного разрешенного nmap-порта.",
    },
    "lesson_42_python_requests.md": {
        "level": "Python requests",
        "minimum": "Напишите скрипт, который делает один GET/HEAD к Slider AI и печатает status code и выбранные headers.",
        "practice": "Добавьте timeout, user-agent `SliderAI-QA-Learning`, обработку ошибок и сохранение sanitized JSON.",
        "deep": "После урока 46 расширьте скрипт до анализа списка заранее известных URL.",
    },
    "lesson_43_python_poc.md": {
        "level": "PoC ethics",
        "minimum": "Не запускайте SQLi/XSS PoC по Slider AI; создайте безопасный шаблон PoC-отчета.",
        "practice": "Опишите, какие условия должны быть выполнены перед запуском PoC на стенде.",
        "deep": "После finding и разрешения заполните шаблон реальными sanitized доказательствами.",
    },
    "lesson_44_python_nmap.md": {
        "level": "Parsing nmap",
        "minimum": "Возьмите учебный XML nmap из лаборатории, не сканируя Slider AI.",
        "practice": "Напишите парсер, который превращает результат одного HTTPS-порта в Markdown observation.",
        "deep": "После согласованного nmap-safe запуска примените парсер к реальному разрешенному выводу.",
    },
    "lesson_45_python_subdomain.md": {
        "level": "Subdomain script boundaries",
        "minimum": "Добавьте в скрипт запрет активного перебора для `slider-ai.ru` без отдельного флага `--i-have-written-approval`.",
        "practice": "Проверьте, что скрипт завершает работу с понятным сообщением для Slider AI scope.",
        "deep": "После расширения scope используйте только малый словарь и сохраните rate limit.",
    },
    "lesson_46_python_dir_brute.md": {
        "level": "Directory script boundaries",
        "minimum": "Добавьте allowlist домена и дефолтный rate limit 1 rps в учебный скрипт.",
        "practice": "На Slider AI не запускайте перебор; проверьте только один явно известный URL из навигации.",
        "deep": "После отдельного разрешения выполните small wordlist dry-run и остановитесь при первых 5xx.",
    },
    "lesson_47_python_cve_parser.md": {
        "level": "CVE research automation",
        "minimum": "Используйте скрипт только для публично раскрытых версий компонентов, найденных ранее.",
        "practice": "Сформируйте таблицу `component/version/source/CVE candidates/confidence`.",
        "deep": "После ручной проверки добавьте remediation-рекомендации для подтвержденных совпадений.",
    },
    "lesson_48_python_final.md": {
        "level": "Safe QA helper",
        "minimum": "Соберите мини-инструмент, который делает только headers/status/link inventory для Slider AI.",
        "practice": "Добавьте allowlist, timeout, rate limit, JSON/Markdown output и маскирование cookies/tokens.",
        "deep": "После урока 63 используйте вывод инструмента как приложение к отчету.",
    },
    "lesson_49_tryhackme_intro.md": {
        "level": "Transfer from THM",
        "minimum": "После комнаты THM выпишите 3 приема, которые безопасно применимы к Slider AI, и 3 запрещенных.",
        "practice": "Сделайте чек-лист ручной проверки стенда на основе безопасных приемов.",
        "deep": "После урока 59 включите чек-лист в полный pentest workflow.",
    },
    "lesson_50_tryhackme_jr.md": {
        "level": "Junior path transfer",
        "minimum": "Свяжите каждую пройденную комнату Jr Pentester с одним QA-навыком для Slider AI.",
        "practice": "Выберите один навык и выполните его как безопасную ручную проверку стенда.",
        "deep": "После урока 56 оформите результат как мини-write-up.",
    },
    "lesson_51_htb_starting.md": {
        "level": "HTB discipline",
        "minimum": "Перенесите из HTB только дисциплину заметок: enumeration, evidence, hypothesis, result.",
        "practice": "Создайте заметку Slider AI в таком формате без запуска атакующих техник.",
        "deep": "После урока 59 используйте формат для end-to-end проверки.",
    },
    "lesson_52_htb_easy.md": {
        "level": "Attack path thinking",
        "minimum": "Опишите возможный attack path для Slider AI как гипотезу, без эксплуатации.",
        "practice": "Разбейте гипотезу на проверяемые QA-кейсы с безопасными шагами.",
        "deep": "После подтвержденных findings обновите attack path фактами.",
    },
    "lesson_53_htb_ad.md": {
        "level": "AD relevance check",
        "minimum": "Определите, есть ли у Slider AI проверяемые AD/SSO-интеграции в вашем QA scope.",
        "practice": "Если нет, оформите `not applicable`; если да, составьте вопросы для владельца системы без атаки.",
        "deep": "После отдельного scope расширения добавьте SSO/AD checks в RoE.",
    },
    "lesson_54_portswigger.md": {
        "level": "PortSwigger to product QA",
        "minimum": "Выберите одну пройденную PortSwigger lab и выпишите защитное ожидание для Slider AI.",
        "practice": "Проверьте это ожидание безопасным вводом или просмотром headers/DOM.",
        "deep": "После уроков OWASP добавьте lab-to-product traceability matrix.",
    },
    "lesson_55_linux_privesc.md": {
        "level": "Privilege escalation boundaries",
        "minimum": "Не выполнять privesc на Slider AI; описать, какие артефакты инфраструктуры были бы нужны и почему они вне scope.",
        "practice": "Проверьте только клиентскую роль/права в UI, доступные вашей QA-учетной записи.",
        "deep": "После разрешения от владельца окружения подготовьте вопросы по hardening, не команды privesc.",
    },
    "lesson_56_practice_reports.md": {
        "level": "Write-up practice",
        "minimum": "Возьмите одно безопасное наблюдение по Slider AI и оформите его как write-up без секретов.",
        "practice": "Добавьте шаги воспроизведения, ожидаемый/фактический результат и рекомендацию.",
        "deep": "После урока 63 разделите write-up на executive и technical части.",
    },
    "lesson_57_osint_practice.md": {
        "level": "OSINT for own product",
        "minimum": "Соберите только публичные сведения о разрешенном домене и не проверяйте найденные внешние активы.",
        "practice": "Классифицируйте сведения: полезно для QA, требует scope, не относится к тесту.",
        "deep": "После урока 61 предложите обновление scope на основе OSINT-наблюдений.",
    },
    "lesson_58_waf_bypass.md": {
        "level": "WAF behavior, no bypass",
        "minimum": "Не обходить WAF; описать признаки, по которым можно понять, что защита сработала.",
        "practice": "Проверьте один безопасный некорректный ввод и зафиксируйте статус/сообщение без bypass payload.",
        "deep": "После письменного разрешения подготовьте план тестирования WAF-правил без обхода production-защит.",
    },
    "lesson_59_full_pentest.md": {
        "level": "Full safe assessment",
        "minimum": "Соберите scope, checklist и артефакты предыдущих Slider AI уроков в единый план.",
        "practice": "Выполните только безопасные проверки из плана и отметьте пропуски как `requires approval`.",
        "deep": "После урока 72 превратите это в финальный отчет по стенду.",
    },
    "lesson_60_ejpt_prep.md": {
        "level": "Exam skills to QA",
        "minimum": "Составьте таблицу навыков eJPT и отметьте, какие применимы к Slider AI, а какие запрещены scope.",
        "practice": "Выполните один применимый безопасный навык и добавьте evidence.",
        "deep": "После финального проекта добавьте gap analysis своего QA security роста.",
    },
    "lesson_61_ptes.md": {
        "level": "PTES scope",
        "minimum": "Оформите mini-RoE для Slider AI на основе `education/slider_ai_scope.md`.",
        "practice": "Добавьте in-scope, out-of-scope, контакты, stop conditions и формат evidence.",
        "deep": "После урока 72 приложите RoE к финальному отчету.",
    },
    "lesson_62_owasp_testing.md": {
        "level": "OWASP checklist",
        "minimum": "Создайте OWASP WSTG чек-лист только для функций Slider AI, доступных QA.",
        "practice": "Пометьте каждый пункт: tested, not tested, not applicable, requires approval.",
        "deep": "После нескольких findings обновите checklist приоритетами риска.",
    },
    "lesson_63_writing_reports.md": {
        "level": "Report writing",
        "minimum": "Оформите один подтвержденный Slider AI результат в формате finding/observation.",
        "practice": "Добавьте executive summary на 3-5 предложений и технические детали.",
        "deep": "После урока 64 добавьте CVSS или объясните, почему CVSS не применим.",
    },
    "lesson_64_cvss.md": {
        "level": "Risk scoring",
        "minimum": "Выберите один подтвержденный finding или observation и решите, применим ли CVSS.",
        "practice": "Если применим, рассчитайте CVSS; если нет, используйте QA severity с обоснованием.",
        "deep": "После retest обновите score/status и объясните изменение риска.",
    },
    "lesson_65_commercial_scanners.md": {
        "level": "Commercial scanner governance",
        "minimum": "Не запускать Nessus/Qualys/Rapid7 по Slider AI без отдельного окна и разрешения.",
        "practice": "Подготовьте scanner policy: safe checks, excluded checks, credentials, rate, stop conditions.",
        "deep": "После разрешения сравните scanner output с ручными findings.",
    },
    "lesson_66_qualys_rapid7.md": {
        "level": "Enterprise VM process",
        "minimum": "Составьте вопросы к владельцам инфраструктуры Slider AI для подключения коммерческого VM-процесса.",
        "practice": "Опишите workflow: asset approval, scan window, triage, false positive review, retest.",
        "deep": "После появления отчета сканера сопоставьте его с manual QA evidence.",
    },
    "lesson_67_ejpt_prep.md": {
        "level": "eJPT readiness for QA",
        "minimum": "Отметьте, какие eJPT-навыки уже применялись в Slider AI-практике.",
        "practice": "Составьте личный план добора навыков без расширения scope стенда.",
        "deep": "После экзамена обновите курс: какие навыки реально помогли в QA.",
    },
    "lesson_68_ejpt_exam.md": {
        "level": "Mock exam discipline",
        "minimum": "Проведите таймбоксированную безопасную проверку Slider AI на 60 минут по заранее утвержденному чек-листу.",
        "practice": "Зафиксируйте timeline, evidence и нерешенные вопросы как на экзамене.",
        "deep": "После урока 72 включите timeline в итоговый отчет.",
    },
    "lesson_69_oscp_basics.md": {
        "level": "OSCP mindset safely",
        "minimum": "Выделите из OSCP-подхода только persistence in note-taking: enumerate, verify, document.",
        "practice": "Примените этот цикл к одному безопасному Slider AI наблюдению.",
        "deep": "После финального проекта сравните OSCP-style notes и QA bug report.",
    },
    "lesson_70_ad_attacks.md": {
        "level": "AD attacks as theory for QA",
        "minimum": "Не применять AD-атаки к Slider AI; определить, есть ли SSO/AD как область вопросов к владельцам.",
        "practice": "Составьте defensive checklist: MFA, service accounts, logs, least privilege, owner.",
        "deep": "После отдельного AD scope используйте только лабораторные техники, не продуктовый стенд.",
    },
    "lesson_71_post_exploitation.md": {
        "level": "Post-exploitation boundaries",
        "minimum": "Не выполнять post-exploitation на Slider AI; описать, какие действия запрещены и почему.",
        "practice": "Составьте evidence handling checklist: что собирать до эксплуатации, чтобы не углублять атаку.",
        "deep": "После урока 72 добавьте раздел `Limitations` в итоговый отчет.",
    },
    "lesson_72_final_project.md": {
        "level": "Final Slider AI assessment",
        "minimum": "Соберите все артефакты Slider AI в один индекс: scope, checklist, observations, findings, retest items.",
        "practice": "Подготовьте финальный отчет по стенду `olddev.slider-ai.ru` с executive summary и technical findings.",
        "deep": "После обсуждения с командой добавьте remediation backlog и план повторной проверки.",
    },
}


def lesson_key(path: Path) -> str:
    return path.name


def section_for(path: Path) -> str:
    data = TASKS[lesson_key(path)]
    return f"""## Практика на Slider AI

**Цель стенда:** `{TARGET}`

**Контекст разрешения:** {COMMON_CONTEXT}

**Ограничения безопасности:** {COMMON_LIMITS}

**Уровень прогрессии:** {data["level"]}

### Минимум

{data["minimum"]}

### Практика Slider AI

{data["practice"]}

### Углубление после изучения следующих уроков

{data["deep"]}

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
"""


def strip_existing(text: str) -> str:
    start = text.find(f"\n{HEADER}")
    if start == -1:
        if text.startswith(HEADER):
            return ""
        return text.rstrip()
    return text[:start].rstrip()


def lesson_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def write_matrix(paths: list[Path]) -> None:
    lines = [
        "# Матрица прогрессии Slider AI",
        "",
        "Цель матрицы — сделать практику на `https://olddev.slider-ai.ru` постепенной: сначала подготовка и наблюдение, затем безопасная ручная проверка, затем инструменты и отчетность.",
        "",
        "| Урок | Уровень | Минимум | Практика Slider AI | Углубление после следующих уроков |",
        "|------|---------|---------|--------------------|-----------------------------------|",
    ]
    for path in paths:
        data = TASKS[lesson_key(path)]
        title = lesson_title(path).replace("|", "\\|")
        lines.append(
            f"| {title} | {data['level']} | {data['minimum']} | {data['practice']} | {data['deep']} |"
        )
    MATRIX.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    changed = 0
    paths = sorted(LESSONS.glob("*/*.md"))
    missing = [path.name for path in paths if path.name not in TASKS]
    extra = [key for key in TASKS if not any(path.name == key for path in paths)]
    if missing or extra:
        raise SystemExit(f"TASKS mismatch. Missing: {missing}; extra: {extra}")

    for path in paths:
        original = path.read_text(encoding="utf-8")
        updated = strip_existing(original) + "\n\n" + section_for(path).rstrip() + "\n"
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1

    before = MATRIX.read_text(encoding="utf-8") if MATRIX.exists() else ""
    write_matrix(paths)
    matrix_changed = before != MATRIX.read_text(encoding="utf-8")
    print(f"Updated Slider AI practice sections: {changed}")
    print(f"Updated progression matrix: {int(matrix_changed)}")


if __name__ == "__main__":
    main()
