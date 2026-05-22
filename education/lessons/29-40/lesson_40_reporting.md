# Урок 40: Документация и отчеты

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 40: Документация и отчеты`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Отчет о пентесте — важнейшая часть работы. Хороший отчет должен быть понятен как техническим специалистам, так и менеджменту.

Структура профессионального отчета:
1. **Executive Summary** — краткое резюме для руководства (бизнес-риски)
2. **Introduction** — цели, scope, methodology
3. **Findings** — найденные уязвимости (с описанием, доказательствами, CVSS)
4. **Recommendations** — рекомендации по исправлению
5. **Appendices** — логи, скрипты, дополнительная информация

Каждый finding должен содержать:
- Название уязвимости
- Severity (Critical/High/Medium/Low/Info)
- CVSS Score (0-10)
- Описание
- Proof of Concept (скриншоты, запросы/ответы)
- Impact (влияние)
- Recommendation (как исправить)

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Шаблон отчета (Markdown)

```markdown
# Report: Pentest of [Target]

## Executive Summary

Цель: Проведение пентеста внешнего периметра [Target].
Период: [Даты]
Ключевые риски: Обнаружено 3 критических уязвимости, позволяющих удаленное выполнение кода.

## Introduction

- **Client**: [Имя]
- **Scope**: [IP/домены]
- **Methodology**: OWASP, PTES
- **Tools**: Nmap, Burp Suite, Nuclei, Metasploit

## Findings

### Finding 1: SQL Injection in Login Form

- **Severity**: Critical
- **CVSS**: 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
- **Description**: The login form is vulnerable to SQL injection...
- **Proof of Concept**:
  ```http
  POST /login.php HTTP/1.1
  Host: target.com
  
  user=admin' OR '1'='1&pass=test
  ```
  Response: "Welcome, admin!"
- **Impact**: Атакующий может обойти аутентификацию, получить доступ к данным.
- **Recommendation**: Использовать подготовленные выражения (prepared statements).

### Finding 2: ...

## Conclusion

Рекомендуется устранить критические уязвимости в приоритетном порядке.

## Appendices

- Nmap scan results
- Screenshots
```

### Инструменты для создания отчетов

```bash
# Serpico (автоматизация отчетов)
git clone https://github.com/SerpicoProject/Serpico.git
cd Serpico
bundle install
ruby serpico.rb

# Dradis (collaboration и reporting)
# Доступен в Kali: Applications -> 04 - Reporting Tools -> dradis

# WriteHat (современный инструмент)
git clone https://github.com/blacklanternsecurity/writehat.git
cd writehat
pip install -r requirements.txt
python3 writehat.py

# macOS (M2, Homebrew) — установка доп. инструментов
brew install pandoc  # Для конвертации Markdown в PDF/Word
brew install mactex  # Для создания LaTeX отчетов (опционально)
```

### CVSS Калькулятор

Пример расчета CVSS 3.1:
- **Attack Vector (AV)**: Network (N) — удаленно
- **Attack Complexity (AC)**: Low (L) — не требует специальных условий
- **Privileges Required (PR)**: None (N) — не требует прав
- **User Interaction (UI)**: None (N) — не требует действий пользователя
- **Scope (S)**: Unchanged (U)
- **Confidentiality (C)**: High (H) — полный доступ к данным
- **Integrity (I)**: High (H)
- **Availability (A)**: High (H)

Итог: CVSS 9.8 (Critical)

Онлайн калькулятор: https://www.first.org/cvss/calculator/3.1


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

1. Проведите пентест DVWA (уровень Low). Напишите отчет по шаблону выше. Минимум 3 findings (SQLi, XSS, Bruteforce).

2. Используя онлайн калькулятор CVSS 3.1, оцените уязвимость "Remote Code Execution через небезопасную десериализацию". Какой балл?

3. Установите Serpico или WriteHat. Создайте отчет через эти инструменты. Какие преимущества перед ручным написанием?

4. Напишите Executive Summary (на русском) для отчета о пентесте интернет-магазина, где найдены SQL-инъекции и XSS. Текст должен быть понятен директору (без технических деталей).

5. Создайте шаблон отчета в LaTeX или Markdown, который можно переиспользовать для будущих пентестов. Включите все обязательные разделы.

## Частые ошибки

1. **Слишком технический язык для Executive Summary** — руководству нужны бизнес-риски, а не детали эксплуатации.

2. **Отсутствие Proof of Concept** — каждый finding должен содержать доказательства (скриншоты, запросы), иначе это "голословные утверждения".

3. **Неправильная оценка CVSS** — внимательно оценивайте все метрики (AV, AC, PR, UI, S, C, I, A), подставляя реальные значения.

4. **Забыли про рекомендации по исправлению** — отчет без конкретных шагов по устранению уязвимостей бесполезен для клиента.

## Вопросы на понимание

1. Какие разделы отчета предназначены для технических специалистов, а какие для менеджмента?

2. Почему CVSS Score важен при приоритизации исправления уязвимостей?

3. Что должно быть в разделе "Proof of Concept" для SQL-инъекции?

4. Как автоматизировать создание отчетов с помощью инструментов (Serpico, WriteHat)?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** First Slider AI report

### Минимум

Оформите один informational finding по уже выполненной безопасной проверке.

### Практика Slider AI

Заполните поля: компонент, шаги, фактический результат, риск, рекомендация, retest.

### Углубление после изучения следующих уроков

После урока 64 добавьте CVSS только для подтвержденных уязвимостей, не для observations.

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
