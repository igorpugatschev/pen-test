# Урок 34: Nuclei — сканирование на уязвимости

## Учебная рамка

**Входные требования:** Умение работать в терминале, понимать IP/порт, scope и базовые юридические ограничения.

**Результат занятия:** Студент запускает инструмент только по разрешенной цели, читает ключевые строки вывода и оформляет результат как находку или наблюдение.

**Наследуемая SDET-компетенция:** tool governance, false-positive triage, безопасный запуск инструментов и оформление результата.

**Security QA-компетенция:** контролируемое применение security-инструментов, scope/rate-limit/stop conditions.

**Связь с книгами:** OWASP/WSTG/PTES как методология инструментов; «PyCharm. Профессиональная работа на Python 2024» — Git, Markdown, отчетность и артефакты.

**Процессный артефакт:** `TOOLING_POLICY.md` и finding/observation по шаблону.

**Безопасная цель:** Только `192.168.100.20`, `target.local`, Metasploitable/VulnHub/THM/HTB/PortSwigger в рамках их правил. Не использовать домашний роутер как цель атаки.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Запустить безопасный минимальный режим инструмента, сохранить команду и объяснить 2-3 ключевых параметра.

**Углубление:** Сравнить два режима инструмента, добавить ограничение скорости/потоков и оформить краткий риск-анализ.

**Минимальная проверка успеха:** Команда выполнена по учебной цели, вывод сохранен, студент отличает обнаружение от подтвержденной уязвимости.

**Эталонный вывод:** В отчете есть target, команда, сокращенный вывод, интерпретация и пометка `разрешенная учебная цель`.

**Критерии сдачи:** Зачет: корректный запуск и интерпретация. Отлично: добавлены ограничения безопасности, rate limit или проверка false positive.

## Теория

Nuclei — современный инструмент для автоматизированного поиска уязвимостей, разработанный ProjectDiscovery. Использует YAML-шаблоны для проверки на известные уязвимости, некорректные конфигурации и экспозицию данных.

Преимущества:
- Огромная база готовых шаблонов (5000+)
- Высокая скорость (написан на Go)
- Поддержка пользовательских шаблонов
- Интеграция в CI/CD

Категории шаблонов:
- **CVE** — проверки на конкретные уязвимости
- **Misconfiguration** — неверные настройки
- **Exposures** — утечки данных (файлы .env, ключи)
- **Vulnerabilities** — общие уязвимости
- **Technologies** — определение технологий

## Практическое занятие

### Установка
```bash
# Kali Linux
sudo apt install nuclei

# macOS (M2, Homebrew)
brew install nuclei

# Через Go
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Проверка
nuclei -version
# Пример вывода:
# nuclei: v3.1.5
# projectdiscovery.io
```

### Обновление шаблонов
```bash
# Обновить шаблоны до последней версии
nuclei -update

# Путь к шаблонам
ls ~/.nuclei/templates/
# Пример вывода:
# cves/  vulnerabilities/  misconfiguration/  exposures/  technologies/  ...
```

### Базовое сканирование
```bash
# Сканирование одного хоста
nuclei -u http://example.com
# Пример вывода:
# [nuclei] Using Nuclei Engine 3.1.5
# [nuclei] Using Nuclei Templates 9.5.4
# [WRN] Found 0 results from 1500 templates

# Сканирование из файла (список URL)
nuclei -l urls.txt

# Использовать конкретные шаблоны
nuclei -u http://example.com -t cves/
nuclei -u http://example.com -t vulnerabilities/
nuclei -u http://example.com -t misconfiguration/

# Сканирование конкретных портов
nuclei -u http://example.com:8080

# Вывод в JSON
nuclei -u http://example.com -json -o results.json
# Пример вывода (JSON):
# {"template-id":"cves/2021/CVE-2021-41773","info":{"name":"...","severity":"critical"},"host":"http://example.com","matched-at":"http://example.com/path"}
```

### Полезные флаги
```bash
# Агрессивный режим (быстрее, но шумнее)
nuclei -u http://example.com -rl 100

# Исключить определенные шаблоны
nuclei -u http://example.com -exclude-severity info,low

# Только высокие и критические
nuclei -u http://example.com -severity critical,high
# Пример вывода:
# [nuclei] Using Nuclei Engine 3.1.5
# [CRITICAL] [http://example.com] [cves/2021/CVE-2021-41773] [...]

# Использовать теги
nuclei -u http://example.com -tags rce,sqli,xss

# Проверка конкретной CVE
nuclei -u http://example.com -t cves/2021/CVE-2021-41773.yaml
```

### Написание своего шаблона
```yaml
# ~/.nuclei/templates/custom/my-check.yaml
id: my-custom-check

info:
  name: My Custom Check
  author: your_name
  severity: medium
  description: Checks for custom header

requests:
  - method: GET
    path:
      - "{{BaseURL}}/"
    matchers:
      - type: word
        words:
          - "X-Custom-Header"
        part: header
```


## Примеры вывода

Минимальный эталонный вывод для сдачи:

```text
$ <команда из практики>
<3-10 строк фактического вывода из разрешенной среды>
```

В отчете студент указывает среду выполнения, безопасную цель, команду или ручные шаги и коротко объясняет, какая строка подтверждает результат.



## Адаптация под macOS (M2, 8GB)

- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Kali/Linux VM запускайте только как углубление и выделяйте не более 3-4GB RAM на MacBook Air M2 (8GB)
- Если нужна Kali/Linux VM на Apple Silicon, используйте ARM64-образ в UTM/VMware Fusion/Parallels; не используйте x86/x64 VM как базовый путь.
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`


## Задачи для самостоятельного выполнения

1. Обновите шаблоны Nuclei. Посчитайте общее количество шаблонов командой `find ~/.nuclei/templates -name "*.yaml" | wc -l`.

2. Запустите Nuclei против тестового сайта (например, `testphp.vulnweb.com`) с флагом `-severity critical,high`. Какие уязвимости удалось найти?

3. Используя тег `-tags xss`, проверьте тестовое приложение DVWA на XSS. Обнаружила ли Nuclei уязвимость?

4. Напишите свой простейший YAML-шаблон, который проверяет наличие заголовка `Server` в ответе веб-сервера. Запустите его против любого сайта.

5. Используйте связку `subfinder | httpx | nuclei` для полного аудита поддоменов. Сохраните результат в markdown-файл.

## Частые ошибки

1. **Команда `-update-templates` устарела** — в новых версиях Nuclei используйте `-update` для обновления шаблонов.

2. **Слишком агрессивное сканирование** — флаг `-rl 100` (rate limit) может быть слишком агрессивным, начинайте с `-rl 10` или `-rl 50`.

3. **Отсутствие шаблонов** — перед первым запуском обязательно выполните `nuclei -update`, иначе шаблоны будут отсутствовать.

4. **Игнорирование severity** — используйте `-severity` для фильтрации, иначе будет много "шума" от информационных находок.

## Вопросы на понимание

1. В чем разница между Nuclei и Nmap NSE по типам проверок?

2. Как написать свой YAML-шаблон для Nuclei и какие обязательные поля он должен содержать?

3. Зачем нужен флаг `-tags` и какие теги чаще всего используются?

4. Почему Nuclei считается "быстрым" инструментом для поиска уязвимостей?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Nuclei controlled use

### Минимум

Не запускайте шаблоны nuclei по Slider AI без согласования; классифицируйте шаблоны по severity/intrusiveness.

### Практика Slider AI

Подберите 3 safe template-кандидата и обоснуйте, почему их можно или нельзя применять.

### Углубление после изучения следующих уроков

После разрешения выполните ограниченный запуск и вручную проверьте каждый результат.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.
