# Занятие 64. CVSS калькулятор: оценка уязвимостей v3.1

## Теория

CVSS (Common Vulnerability Scoring System) — открытый стандарт для оценки серьезности уязвимостей. Версия 3.1 используется с 2019 года.

### Структура CVSS v3.1

CVSS состоит из трех групп метрик:

**1. Base Score (Базовый показатель)** — характеристики уязвимости, не меняющиеся со временем
- Exploitability Metrics (Возможность эксплуатации)
- Impact Metrics (Влияние)

**2. Temporal Score (Временной показатель)** — характеристики, меняющиеся со временем
- Зрелость кода эксплойта
- Доступность исправления
- Уровень уверенности в отчете

**3. Environmental Score (Средовой показатель)** — специфичные для среды заказчика
- Требования к безопасности (CIA — Confidentiality, Integrity, Availability)

### Base Metrics (Базовые метрики)

#### Exploitability Metrics (Возможность эксплуатации)

| Метрика | Значения | Описание |
|---------|----------|----------|
| **Attack Vector (AV)** | Network (N), Adjacent (A), Local (L), Physical (P) | Откуда можно эксплуатировать |
| **Attack Complexity (AC)** | Low (L), High (H) | Насколько сложно эксплуатировать |
| **Privileges Required (PR)** | None (N), Low (L), High (H) | Какие права нужны |
| **User Interaction (UI)** | None (N), Required (R) | Нужно ли участие пользователя |
| **Scope (S)** | Unchanged (U), Changed (C) | Меняется ли область безопасности |

#### Impact Metrics (Влияние)

| Метрика | Значения | Описание |
|---------|----------|----------|
| **Confidentiality (C)** | None (N), Low (L), High (H) | Влияние на конфиденциальность |
| **Integrity (I)** | None (N), Low (L), High (H) | Влияние на целостность |
| **Availability (A)** | None (N), Low (L), High (H) | Влияние на доступность |

### Формула расчета Base Score

```
Base Score = Roundup(Minimum(
    Impact + Exploitability,
    10
))

Exploitability = 8.22 × AV × AC × PR × UI × S

Impact = 6.42 × Scope × (C + I + A)
```

### Шкала оценок

| Score Range | Severity | Русский перевод | Действия |
|-------------|----------|-----------------|----------|
| 0.0 | None | Отсутствует | Информирование |
| 0.1 - 3.9 | Low | Низкая | Плановое исправление |
| 4.0 - 6.9 | Medium | Средняя | Исправление в течение 90 дней |
| 7.0 - 8.9 | High | Высокая | Исправление в течение 30 дней |
| 9.0 - 10.0 | Critical | Критическая | Немедленное исправление |

### Примеры оценок

**SQL Injection в веб-форме (без авторизации)**
- AV: Network (0.85)
- AC: Low (0.77)
- PR: None (0.85)
- UI: None (0.85)
- S: Unchanged (не меняет scope)
- C: High (0.56)
- I: High (0.56)
- A: None (0)
- **Score: 9.1 (Critical)**

**XSS в веб-форме (требует клика пользователя)**
- AV: Network (0.85)
- AC: Low (0.77)
- PR: None (0.85)
- UI: Required (0.62)
- S: Unchanged
- C: Low (0.22)
- I: Low (0.22)
- A: None (0)
- **Score: 6.1 (Medium)**

**Local Privilege Escalation (требует локального доступа)**
- AV: Local (0.55)
- AC: Low (0.77)
- PR: Low (0.62)
- UI: None (0.85)
- S: Unchanged
- C: High (0.56)
- I: High (0.56)
- A: High (0.56)
- **Score: 7.8 (High)**

## Практическое занятие

### Использование CVSS калькулятора

Онлайн-калькуляторы:
- https://www.first.org/cvss/calculator/3.1
- https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator

### Практика: оценка уязвимостей

Создайте таблицу и оцените следующие уязвимости по CVSS v3.1:

```markdown
# Оценка уязвимостей по CVSS v3.1

## Таблица оценок

| № | Уязвимость | AV | AC | PR | UI | S | C | I | A | Score | Severity |
|---|------------|----|----|----|----|----|----|----|----|-------|----------|
| 1 | SQL Injection в поиске | N | L | N | N | U | H | H | N | 9.1 | Critical |
| 2 | Stored XSS в комментариях | N | L | N | R | U | L | L | N | 6.1 | Medium |
| 3 | RCE через загрузку файла | N | L | N | N | U | H | H | H | 9.8 | Critical |
| 4 | Отказ в обслуживании (DoS) | N | L | N | N | U | N | N | H | 7.5 | High |
| 5 | Утечка версии веб-сервера | N | L | N | N | U | L | N | N | 5.3 | Medium |
| 6 | Слабые пароли (брутфорс) | N | L | N | N | U | H | N | N | 7.5 | High |
| 7 | IDOR (доступ к чужим данным) | N | L | L | N | U | L | N | N | 4.3 | Medium |
| 8 | CSRF (смена email) | N | L | N | R | U | N | L | N | 4.3 | Medium |
| 9 | Directory Traversal | N | L | N | N | U | H | N | N | 7.5 | High |
| 10 | SSRF (доступ к внутренним ресурсам) | N | L | N | N | C | L | L | N | 8.6 | High |

## Детальный разбор: Уязвимость #3 (RCE через загрузку)

### Vector String:
```
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
```

### Обоснование:
- **AV:N** — Атака из сети (через интернет)
- **AC:L** — Низкая сложность (загрузка .php файла)
- **PR:N** — Без привилегий (форма доступна всем)
- **UI:N** — Без участия пользователя
- **S:U** — Scope не меняется (влияние на ту же систему)
- **C:H** — Полный доступ к конфиденциальным данным
- **I:H** — Полный контроль над целостностью (можно изменять файлы)
- **A:H** — Полный отказ в доступности (можно удалить всё)

### Бизнес-риск:
Критическая уязвимость позволяет полностью скомпрометировать сервер. Возможна установка вымогателей, кража базы данных, использование сервера для майнинга или атак на другие системы.
```

### Создание своего калькулятора на Python

```python
#!/usr/bin/env python3
"""
Простой калькулятор CVSS v3.1 (упрощенная версия)
"""

# Веса для Exploitability
AV_WEIGHT = {'N': 0.85, 'A': 0.62, 'L': 0.55, 'P': 0.2}
AC_WEIGHT = {'L': 0.77, 'H': 0.44}
PR_WEIGHT = {'N': 0.85, 'L': 0.62, 'H': 0.27}
UI_WEIGHT = {'N': 0.85, 'R': 0.62}
S_SCOPE = {'U': 1, 'C': 1.08}  # Множитель для Scope

# Веса для Impact
CIA_WEIGHT = {'N': 0, 'L': 0.22, 'H': 0.56}

def calculate_cvss(av, ac, pr, ui, s, c, i, a):
    """Расчет CVSS Base Score v3.1"""
    
    # Exploitability
    exploitability = 8.22 * AV_WEIGHT[av] * AC_WEIGHT[ac] * PR_WEIGHT[pr] * UI_WEIGHT[ui] * S_SCOPE[s]
    
    # Impact
    iss = 1 - ((1 - CIA_WEIGHT[c]) * (1 - CIA_WEIGHT[i]) * (1 - CIA_WEIGHT[a]))
    if s == 'U':
        impact = 6.42 * iss
    else:  # Changed scope
        impact = 7.52 * iss - 3.25 * (iss - 0.029) - 3.25
    
    # Base Score
    if impact <= 0:
        base_score = 0
    else:
        base_score = min(impact + exploitability, 10)
    
    # Округление вверх до 1 десятичного знака
    base_score = round(base_score * 10) / 10
    
    # Определение серьезности
    if base_score == 0:
        severity = "None"
    elif base_score < 4.0:
        severity = "Low"
    elif base_score < 7.0:
        severity = "Medium"
    elif base_score < 9.0:
        severity = "High"
    else:
        severity = "Critical"
    
    return base_score, severity

# Пример использования
if __name__ == "__main__":
    # SQL Injection
    score, severity = calculate_cvss('N', 'L', 'N', 'N', 'U', 'H', 'H', 'N')
    print(f"SQL Injection: {score} ({severity})")
    
    # XSS
    score, severity = calculate_cvss('N', 'L', 'N', 'R', 'U', 'L', 'L', 'N')
    print(f"XSS: {score} ({severity})")
    
    # RCE
    score, severity = calculate_cvss('N', 'L', 'N', 'N', 'U', 'H', 'H', 'H')
    print(f"RCE: {score} ({severity})")
```




### CVSS v4.0 (обновлено в 2023)

CVSS v4.0 — последняя версия стандарта, выпущенная в ноябре 2023 года. Основные изменения:

- **Новая метрика: Attack Requirements (AT)** — учитывает условия атаки (present/none)
- **Измененная метрика: User Interaction (UI)** — теперь учитывает авторизованных пользователей
- **Упрощенные значения:** Low/None вместо Multiple/Unknown
- **Новые угрозы:** Supply Chain (цепочка поставок), AI/ML уязвимости

**Пример CVSS v4.0:**
```
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:N/SC:N/SI:N/SA:N
Base Score: 8.8 (High)
```

> **Для M2 8GB:** При расчете CVSS используйте онлайн-калькулятор: https://www.first.org/cvss/calculator/cvss-4.0

## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.




## Адаптация под macOS (M2, 8GB)

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты


## Задачи для самостоятельного выполнения

1. **Оценка 10 уязвимостей**: Оцените по CVSS v3.1 10 уязвимостей из OWASP Top 10 2021. Напишите Vector String и обоснование для каждой.

2. **Сравнение CVSS v2 vs v3**: Возьмите 5 уязвимостей и оцените их по CVSS v2 и v3.1. Найдите различия в оценках и объясните причины.

3. **Environmental Score**: Для уязвимости "Утечка номеров кредитных карт" рассчитайте Environmental Score, учитывая, что для банка Confidentiality и Integrity имеют значение High (CR:H, IR:H, AR:M).

4. **Калькулятор на Python**: Доработайте калькулятор выше, добавив поддержку Temporal Metrics (E, RL, RC) и Environmental Metrics (CR, IR, AR, MAV, MAC, MPR, MUI, MS, MC, MI, MA).

5. **Отчет с CVSS**: Возьмите отчет, написанный на прошлом занятии, и добавьте к каждой уязвимости корректный CVSS v3.1 Vector String и оценку. Проверьте, соответствует ли серьезность бизнес-рискам, описанным в Executive Summary.

## Частые ошибки

1. **Неправильная оценка Scope** — изменение Scope (S) часто упускается, что ведет к неверной оценке.
2. **Игнорирование Temporal Metrics** — для реальных отчетов важно учитывать доступность патчей и зрелость эксплойтов.
3. **Путаница между CVSS v2 и v3** — метрики несовместимы, используйте только v3.1 для современных отчетов.
4. **Завышение оценки** — добавление влияния на Availability без оснований.

## Вопросы на понимание

1. Из каких трех групп состоит CVSS v3.1?
2. Что такое Base Score?
3. Как влияет Scope (S) на итоговую оценку?
4. Какой диапазон оценок считается Critical?
5. Чем CVSS v3.1 отличается от v2?
