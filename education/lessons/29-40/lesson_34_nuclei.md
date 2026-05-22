# Урок 34: Nuclei — сканирование на уязвимости

## Учебная рамка

**Входные требования:** Умение работать в терминале, понимать IP/порт, scope и базовые юридические ограничения.

**Результат занятия:** Студент запускает инструмент только по разрешенной цели, читает ключевые строки вывода и оформляет результат как находку или наблюдение.

**Наследуемая SDET-компетенция:** tool governance, false-positive triage, безопасный запуск инструментов и оформление результата.

**Security QA-компетенция:** контролируемое применение security-инструментов, scope/rate-limit/stop conditions.

**Связь с книгами:** OWASP/WSTG/PTES как методология инструментов; «PyCharm. Профессиональная работа на Python 2024» — Git, Markdown, отчетность и артефакты.

**Основной источник:** «PyCharm. Профессиональная работа на Python 2024» и «Паттерны разработки на Python».

**Дополнительные источники:** `Black Hat Python` только для понимания lab-only техник и defensive boundaries.

**Что берем из источника:** tool governance, false-positive review, structured output, границы ручного/passive/low-rate режима.

**Как это превращается в SDET/Security QA навык:** превратить инструменты в управляемый QA-процесс с approval, stop conditions и evidence policy.

**Что нельзя переносить на Slider AI без отдельного разрешения:** не запускать aggressive scan, brute force, wordlists или intrusive templates по Slider AI без отдельного письменного разрешения.


**Процессный артефакт:** `TOOLING_POLICY.md` и finding/observation по шаблону.

**Безопасная цель:** Только `192.168.100.20`, `target.local`, Metasploitable/VulnHub/THM/HTB/PortSwigger в рамках их правил. Не использовать домашний роутер как цель атаки.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Запустить безопасный минимальный режим инструмента, сохранить команду и объяснить 2-3 ключевых параметра.

**Углубление:** Сравнить два режима инструмента, добавить ограничение скорости/потоков и оформить краткий риск-анализ.

**Минимальная проверка успеха:** Команда выполнена по учебной цели, вывод сохранен, студент отличает обнаружение от подтвержденной уязвимости.

**Эталонный вывод:** В отчете есть target, команда, сокращенный вывод, интерпретация и пометка `разрешенная учебная цель`.

**Критерии сдачи:** Зачет: корректный запуск и интерпретация. Отлично: добавлены ограничения безопасности, rate limit или проверка false positive.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 34: Nuclei — сканирование на уязвимости`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/pycharm-professional-python-2024-pages/`
- `docs/socraticode/architecture-patterns-python-pages/`

Конкретные страницы для этого блока: `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`; `architecture-patterns-python-pages/page-038.md`-`page-069.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: tool governance, false-positive review, structured output, границы ручного/passive/low-rate режима. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: не запускать aggressive scan, brute force, wordlists или intrusive templates по Slider AI без отдельного письменного разрешения. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

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

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

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

### Базовое сканирование только в local lab
```bash
# Сканирование одного локального учебного хоста
nuclei -u http://127.0.0.1:8080
# Пример вывода:
# [nuclei] Using Nuclei Engine 3.1.5
# [nuclei] Using Nuclei Templates 9.5.4
# [WRN] Found 0 results from 1500 templates

# Сканирование из файла допускается только для заранее разрешенного lab-списка
nuclei -l urls.txt

# Использовать конкретные безопасные шаблоны в lab
nuclei -u http://127.0.0.1:8080 -t http/technologies/
nuclei -u http://127.0.0.1:8080 -t http/misconfiguration/

# Сканирование конкретного локального порта
nuclei -u http://127.0.0.1:8080

# Вывод в JSON
nuclei -u http://127.0.0.1:8080 -json -o results.json
# Пример вывода (JSON):
# {"template-id":"http/missing-security-headers","info":{"name":"...","severity":"info"},"host":"http://127.0.0.1:8080","matched-at":"http://127.0.0.1:8080/"}
```

### Полезные флаги
```bash
# Антипример: агрессивный режим запрещен для Slider AI и публичных целей без approval
# nuclei -u https://any-real-target.example -rl 100

# Исключить определенные шаблоны в lab
nuclei -u http://127.0.0.1:8080 -exclude-severity info,low

# Только высокие и критические
nuclei -u http://127.0.0.1:8080 -severity critical,high
# Пример вывода:
# [nuclei] Using Nuclei Engine 3.1.5
# [INF] No results found. Treat scanner output as candidate evidence, not as a finding.

# Использовать теги
nuclei -u http://127.0.0.1:8080 -tags tech

# Проверка конкретной CVE выполняется только в lab, где эта CVE намеренно воспроизводится
nuclei -u http://127.0.0.1:8080 -t cves/2021/CVE-2021-41773.yaml
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

Минимальный эталонный артефакт для сдачи:

```markdown
Environment: macOS native / Kali ARM64 VM / cloud lab / Slider AI olddev
Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>
Action: <выполненная безопасная команда или ручной шаг>
Evidence: <санитизированный фрагмент вывода, скриншота или HTTP history>
Result status: finding / observation / not reproducible / not applicable / requires approval
Next step: <retest, remediation, approval request или lab-only follow-up>
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

2. Запустите Nuclei против локального учебного приложения `http://127.0.0.1:8080` или THM/HTB lab, где сканирование явно разрешено. Сохраните output как candidate observation, а не как подтвержденный finding.

3. Используя безопасные `technologies`/`misconfiguration` шаблоны, проверьте local lab. Если нужны XSS/CVE templates, оформите это как lab-only extension и объясните, почему такие шаблоны не запускаются по Slider AI без approval.

4. Напишите простейший YAML-шаблон, который проверяет наличие заголовка `Server` в ответе веб-сервера. Запустите его только против local lab или заранее разрешенной цели.

5. Заполните `Tool approval card` для связки `subfinder | httpx | nuclei`. Не запускайте pipeline без расширенного scope; в markdown-файле укажите режим `requires approval`.

## Частые ошибки

1. **Команда `-update-templates` устарела** — в новых версиях Nuclei используйте `-update` для обновления шаблонов.

2. **Слишком агрессивное сканирование** — флаг `-rl 100` является антипримером для рабочих стендов. Для Slider AI без отдельного approval не запускайте Nuclei; после approval начинайте с 1 rps или медленнее и stop conditions.

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

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Tool Governance Report`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
