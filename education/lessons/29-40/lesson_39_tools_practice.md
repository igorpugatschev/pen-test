# Урок 39: Итоговая практика с инструментами

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

Этот раздел не является заданием “пойди и найди теорию в книгах”. Книги использованы автором курса для подготовки лекции `Урок 39: Итоговая практика с инструментами`, а студент получает самодостаточное объяснение в разделах `Source-driven theory` и `Теория`.

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

Комплексный пентест требует умения связывать разные инструменты в цепочки (chains). Один инструмент находит поддомены, другой проверяет живые хосты, третий ищет уязвимости.

Типичный workflow пентеста внешнего периметра:
1. **Разведка** (Amass, Subfinder, Shodan) → список поддоменов
2. **Проверка живых хостов** (httpx, httprobe) → активные веб-сервера
3. **Сканирование портов** (Nmap) → открытые сервисы
4. **Поиск директорий** (ffuf, dirsearch) → скрытые пути
5. **Поиск уязвимостей** (Nuclei, Nmap NSE) → известные баги
6. **Эксплуатация** (SearchSploit, ручной анализ)

## Guided practice

1. Опишите режим инструмента: manual, passive, low-rate, lab-only или forbidden.
2. Заполните tool approval card до запуска любой инструментальной проверки.
3. Выполните только безопасный режим или оформите `requires approval`, если проверка выходит за scope.
4. Проведите false-positive review и приложите только sanitized output.

### Эталон самостоятельной работы

К концу guided practice у студента есть короткий Markdown-артефакт: цель проверки, выполненные шаги, sanitized evidence, интерпретация результата, границы применимости и следующий безопасный шаг.

## Практическое занятие

### Цель: разрешенная лаборатория

Основной путь для MacBook Air M2 (8GB): TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или локальный легкий учебный сервис. Локальная Kali ARM64 VM допустима как углубление. Metasploitable2/x86_64 не является базовой целью для Apple Silicon.

### Шаг 1: Разведка
```bash
# Определите IP разрешенной лабораторной цели
sudo nmap -sn 192.168.100.0/24  # Только в изолированной лаборатории
# Пример вывода:
# Nmap scan report for 192.168.100.20
# Host is up (0.00047s latency).

# Предположим, IP = 192.168.100.20
TARGET=192.168.100.20
```

### Шаг 2: Сканирование портов (Nmap)
```bash
# Минимум: ограниченная проверка ожидаемых портов
nmap -sV -p 22,80,443 -oN nmap_minimal_$TARGET.txt $TARGET

# Углубление: полное сканирование допустимо только в изолированной лаборатории или cloud lab
# Укажите окно тестирования, rate limit и stop conditions до запуска.
# sudo nmap -A -p- --max-rate 50 -oA nmap_full $TARGET
# Пример вывода:
# PORT     STATE SERVICE    VERSION
# 21/tcp   open  ftp        vsftpd 2.3.4
# 22/tcp   open  ssh        OpenSSH 4.7p1 Debian
# 23/tcp   open  telnet     Linux telnetd
# 80/tcp   open  http       Apache httpd 2.2.8

# Результат: порты 21, 22, 23, 25, 53, 80, 111, 139, 445, 512, 513, 514, 1099, 1524, 2049, 2121, 3306, 5432, 5900, 6000, 6667, 8009, 8180
```

### Шаг 3: Поиск веб-директорий
```bash
# Поиск на порту 80
ffuf -u http://$TARGET/FUZZ -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt -e .txt,.php,.bak -rate 20
# Пример вывода:
# [Status: 200] [Size: 1234] /index.php
# [Status: 302] [Size: 0] /dvwa
# [Status: 200] /phpMyAdmin

# Результат: /dvwa, /phpMyAdmin, /mutillidae, /cgi-bin/
```

### Шаг 4: Поиск уязвимостей (Nuclei)
```bash
# Сканирование на уязвимости только в lab/cloud и с ограничением скорости
nuclei -u http://$TARGET -severity critical,high -rate-limit 10
# Пример вывода:
# [CRITICAL] [http://$TARGET] [cves/2021/CVE-2021-41773] [...]

# Nmap NSE только по согласованным портам лабораторной цели
nmap --script vuln --max-rate 20 -p 21,22,23,80,445 $TARGET
# Пример вывода:
# |_  smb-vuln-ms08-067: ERROR: Script execution failed
# |  ftp-vsftpd-vuln: VULNERABLE: vsftpd 2.3.4 issue
```

### Шаг 5: Поиск эксплойтов (SearchSploit)
```bash
# Для vsftpd 2.3.4
searchsploit vsftpd 2.3.4
# Пример вывода:
# Exploits: 3
#   |  /usr/share/exploitdb/exploits/unix/remote/17491.rb

# Для Samba
searchsploit samba 3.0
# Пример вывода:
# Exploits: 5
#   |  /usr/share/exploitdb/exploits/linux/remote/10.c
```

### Шаг 6: Автоматизация (Bash скрипт)
Создайте скрипт `auto_scan.sh`:
```bash
#!/bin/bash
TARGET=$1

echo "[*] Starting lab-only scan for $TARGET"
echo "[!] Run only in isolated lab/cloud target with written scope"

echo "[1] Nmap limited scan..."
nmap -sV -p 22,80,443 -oN nmap_$TARGET.txt $TARGET

echo "[2] Directory enumeration (port 80, rate-limited)..."
ffuf -u http://$TARGET/FUZZ -w /opt/homebrew/share/seclists/Discovery/Web-Content/common.txt -rate 20 -o dirs_$TARGET.json -of json

echo "[3] Nuclei vulnerability scan (rate-limited, lab only)..."
nuclei -u http://$TARGET -rate-limit 10 -o nuclei_$TARGET.txt

echo "[4] SearchSploit..."
nmap -sV -p 22,80,443 $TARGET -oX nmap_$TARGET.xml
searchsploit --nmap nmap_$TARGET.xml

echo "[*] Scan complete!"
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

1. **Минимум:** выберите разрешенную учебную цель и выполните только пассивный/мягкий workflow: заголовки, один ограниченный nmap-запуск, ручная проверка веб-страницы.

2. **Углубление:** в cloud lab или ARM64 VM выполните полный workflow по шагам выше. Составьте список найденных уязвимостей и отметьте, какие инструменты были шумными.

3. Напишите скрипт на Python, который связывает Subfinder → httpx → Nuclei, но добавьте allowlist доменов и dry-run режим.

4. Используя Shodan, найдите 5 учебных примеров баннеров, но не подключайтесь к чужим хостам. Анализируйте только публичные метаданные.

5. Изучите логи своей лаборатории во время сканирования. Какие инструменты вызвали подозрение? Как снизить шум легальными способами: rate limit, согласованное окно, точный scope?

## Частые ошибки

1. **Отсутствие прав для SYN-сканирования** — nmap -sS требует sudo, иначе будет использоваться TCP connect.

2. **Слишком агрессивное сканирование** — запуск всех инструментов одновременно может вызвать блокировку или обнаружение.

3. **Неправильный путь к словарям в macOS** — проверьте, что `/opt/homebrew/share/seclists/` или `/usr/share/wordlists/` доступны.

4. **Забыли про проверку живых хостов** — перед сканированием убедитесь, что цель доступна (ping, nmap -sn).

## Вопросы на понимание

1. В каком порядке нужно запускать инструменты для минимизации шума?

2. Какой инструмент дает наиболее полную картину уязвимостей: Nmap NSE, Nuclei или SearchSploit?

3. Почему важно связывать результаты разных инструментов (например, поддомены → живые хосты → уязвимости)?

4. Как автоматизировать весь процесс пентеста одним скриптом?

## Практика на Slider AI

**Цель стенда:** `https://olddev.slider-ai.ru`

**Контекст разрешения:** тестовый стенд проекта Slider AI, доступен QA для обучения и проверки безопасности. Production и любые другие домены не входят в это задание.

**Ограничения безопасности:** соблюдать `education/slider_ai_scope.md`; не выполнять DoS/load-тесты, brute force, destructive payloads, изменение чужих данных, извлечение секретов и действия вне согласованного scope.

**Уровень прогрессии:** Toolchain planning

### Минимум

Соберите безопасный pipeline проверки Slider AI без запуска intrusive инструментов.

### Практика Slider AI

Для каждого инструмента укажите режим: manual/passive/low-rate/forbidden.

### Углубление после изучения следующих уроков

После урока 40 превратите pipeline в отчетный чек-лист с evidence slots.

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
