# Урок 40: Документация и отчеты

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

Пример вывода команд будет добавлен индивидуально для каждого урока.



## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
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
