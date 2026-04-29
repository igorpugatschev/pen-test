# Урок 34: Nuclei — сканирование на уязвимости

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

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
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
