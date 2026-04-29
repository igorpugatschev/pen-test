# Pen-Test Learning Program

Программа обучения пентесту (penetration testing) из 72 уроков, адаптированная для MacBook Air M2 (8GB RAM).

## 📋 Содержание

Программа рассчитана на **3 занятия в неделю по 1-2 часа** и охватывает полный путь от основ Linux до получения сертификации EJPT/OSCP.

### Структура курса

| Блок | Уроки | Тема |
|------|-------|------|
| [01-08](education/lessons/01-08/) | 1-8 | Linux основы |
| [09-16](education/lessons/09-16/) | 9-16 | Сетевые технологии |
| [17-28](education/lessons/17-28/) | 17-28 | OWASP Top 10 (A01-A10 + доп. категории) |
| [29-40](education/lessons/29-40/) | 29-40 | Инструменты пентеста |
| [41-48](education/lessons/41-48/) | 41-48 | Python для пентеста |
| [49-60](education/lessons/49-60/) | 49-60 | Практика на площадках |
| [61-72](education/lessons/61-72/) | 61-72 | Методология и сертификация |

**Итого: 72 урока + 5 дополнительных (17b-17f)**

## 🎯 Особенности

- **Адаптация под macOS (M2, 8GB)**: каждый урок содержит раздел с заменой `apt install` на `brew install`
- **Структура каждого урока**:
  - Теория
  - Практическое занятие
  - Примеры вывода
  - Частые ошибки
  - Вопросы на понимание
  - Задачи для самостоятельного выполнения
  - Адаптация под macOS (M2, 8GB)

## 📚 Методология

Курс базируется на:
- **OWASP Testing Guide v4.2** — стандарт тестирования веб-приложений
- **PTES (Penetration Testing Execution Standard)** — полный цикл пентеста
- **NIST SP 800-115** — техническое руководство по тестированию безопасности

## 🛠 Используемые инструменты

- **Recon**: Nmap, Amass, Subfinder, DNSx, httpx
- **Vulnerability Scanning**: Nuclei, OWASP ZAP, Burp Suite
- **Exploitation**: SQLmap, Metasploit (в планах автоматизации)
- **Password Attacks**: Hydra, Patator
- **Web Testing**: Dirsearch, FFuf, Burp Suite
- **OSINT**: Shodan, Censys, Amass
- **Reporting**: CVSS v3.1, стандарты отчетности

## 🚀 Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/igorpugatschev/pen-test.git
cd pen-test
```

2. Начните с первого урока:
```bash
cat education/lessons/01-08/lesson_01_intro_linux.md
```

3. Для проверки всех уроков используйте скрипт:
```bash
cd education/tools
bash check_lessons.sh
```

## 📖 Полная программа

Подробное описание всех 72 уроков: [education/pentest_learning_program.md](education/pentest_learning_program.md)

## 🖥 Требования

- **macOS** (рекомендуется M2/M3) или Linux
- **8GB RAM** (минимум, для MacBook Air M2)
- **Homebrew** (для macOS): `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- **Виртуализация** (опционально): UTM или Parallels Desktop для запуска Kali Linux

### Рекомендации для MacBook Air M2 (8GB):
- Используйте **AttackBox** (TryHackMe) или **Tunnelblick** (VPN) вместо локальных VM
- Kali Linux через UTM выделяйте не более 3-4GB RAM
- Приоритет облачным площадкам: TryHackMe, HackTheBox, PortSwigger Academy

## 🔧 Вспомогательные инструменты

Скрипты для проверки и исправления уроков находятся в папке `education/tools/`:
- `check_lessons.sh` — проверка структуры и критических ошибок
- `final_fix_all.py` — автоисправление всех уроков
- `academic_review_report.md` — отчет о качестве материалов (90.0%)

## ⚠️ Юридический дисклеймер

Все материалы предназначены **исключительно для обучения** и легального тестирования безопасности:
- ✓ TryHackMe, HackTheBox, PortSwigger Academy
- ✓ Bug Bounty программы с явным разрешением
- ✓ Собственные системы или системы с письменным разрешением

**Несанкционированный доступ к компьютерным системам незаконен** (УК РФ ст. 272, CFAA в США, Computer Misuse Act в UK).

## 📊 Статус проекта

- ✅ Созданы все 72 урока
- ✅ Добавлены 5 дополнительных уроков OWASP
- ✅ Исправлены критические ошибки (localhost в payload, дублирование кода)
- ✅ Все уроки прошли валидацию
- ✅ Академическое ревью: 90.0% (4160/4620 баллов)

## 📄 Лицензия

Материалы доступны под лицензией MIT. Смотрите файл [LICENSE](LICENSE) (если добавите).

## 🤝 Вклад в проект

Pull Request'ы приветствуются! Особенно:
- Исправление ошибок в уроках
- Добавление новых примеров
- Адаптация под другие платформы (Windows, Linux)
- Перевод на другие языки

## 📧 Контакты

- GitHub: [@igorpugatschev](https://github.com/igorpugatschev)
- Репозиторий: https://github.com/igorpugatschev/pen-test

---

**Примечание**: Курс постоянно обновляется. Следите за [commits](https://github.com/igorpugatschev/pen-test/commits/main).
