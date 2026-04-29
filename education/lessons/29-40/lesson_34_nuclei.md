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

# Через Go
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

# Проверка
nuclei -version
```

### Обновление шаблонов
```bash
# Обновить шаблоны до последней версии
nuclei -update-templates

# Путь к шаблонам
ls ~/.nuclei/templates/
```

### Базовое сканирование
```bash
# Сканирование одного хоста
nuclei -u http://example.com

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
```

### Полезные флаги
```bash
# Агрессивный режим (быстрее, но шумнее)
nuclei -u http://example.com -rl 100

# Исключить определенные шаблоны
nuclei -u http://example.com -exclude-severity info,low

# Только высокие и критические
nuclei -u http://example.com -severity critical,high

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

## Задачи для самостоятельного выполнения

1. Обновите шаблоны Nuclei. Посчитайте общее количество шаблонов командой `find ~/.nuclei/templates -name "*.yaml" | wc -l`.

2. Запустите Nuclei против тестового сайта (например, `testphp.vulnweb.com`) с флагом `-severity critical,high`. Какие уязвимости удалось найти?

3. Используя тег `-tags xss`, проверьте тестовое приложение DVWA на XSS. Обнаружила ли Nuclei уязвимость?

4. Напишите свой простейший YAML-шаблон, который проверяет наличие заголовка `Server` в ответе веб-сервера. Запустите его против любого сайта.

5. Используйте связку `subfinder | httpx | nuclei` для полного аудита поддоменов. Сохраните результат в markdown-файл.
