# Урок 30: Nmap NSE (Nmap Scripting Engine)

## Теория

NSE (Nmap Scripting Engine) позволяет расширить функционал Nmap с помощью скриптов на Lua. Скрипты делятся на категории:

- **safe** — безопасные, не влияют на цель
- **intrusive** — могут вызвать сбои или нагрузку
- **auth** — обход аутентификации
- **brute** — брутфорс паролей
- **vuln** — проверка на уязвимости
- **exploit** — эксплуатация уязвимостей
- **discovery** — поиск информации о сети
- **version** — определение версий (используется с -sV)
- **malware** — поиск бэкдоров и вредоносов

## Практическое занятие

### Работа со скриптами
```bash
# Путь к скриптам (Kali Linux)
ls /usr/share/nmap/scripts/
# macOS (M2, Homebrew)
ls /opt/homebrew/share/nmap/scripts/

# Информация о конкретном скрипте
nmap --script-help http-enum
# Пример вывода:
# http-enum categories: discovery, safe
# http-enum authors: A. T.
# http-enum ...

nmap --script-help smb-os-discovery

# Запуск конкретного скрипта
nmap --script http-enum 192.168.1.1
# Пример вывода:
# | http-enum:
# |   /admin/: Possible admin folder
# |   /phpMyAdmin/: phpMyAdmin

nmap --script smb-os-discovery 192.168.1.1
# Пример вывода:
# | smb-os-discovery:
# |   OS: Windows 10
# |   Computer name: DESKTOP-ABC123
```

### Полезные скрипты
```bash
# Поиск директорий через HTTP
nmap --script http-enum -p 80 192.168.1.1

# Информация о SMB (Windows shares)
nmap --script smb-os-discovery -p 445 192.168.1.1
nmap --script smb-enum-shares -p 445 192.168.1.1
# Пример вывода:
# | smb-enum-shares:
# |   ADMIN$: READ ONLY
# |   C$: READ ONLY

# Проверка на common vulns
nmap --script vuln 192.168.1.1

# Брутфорс HTTP аутентификации
nmap --script http-brute -p 80 192.168.1.1

# Проверка SSL/TLS
nmap --script ssl-enum-ciphers -p 443 192.168.1.1
# Пример вывода:
# | ssl-enum-ciphers:
# |   TLSv1.2:
# |     ciphers:
# |       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

# DNS информация
nmap --script dns-zone-transfer -p 53 192.168.1.1
```

### Запуск групп скриптов
```bash
# Все скрипты категории safe
nmap --script "safe" 192.168.1.1

# Discovery + version
nmap --script "discovery,version" 192.168.1.1

# Исключить intrusive
nmap --script "not intrusive" 192.168.1.1

# Все, кроме brute
nmap --script "default or safe" 192.168.1.1
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

1. Найдите в /usr/share/nmap/scripts/ скрипт `http-title.nse`. Запустите его против целевого веб-сервера. Какой заголовок страницы?

2. Используйте скрипт `smb-os-discovery` против Windows-машины (или Metasploitable). Какую информацию об ОС удалось получить?

3. Запустите категорию `vuln` против целевого хоста. Сохраните результат. Перечислите найденные уязвимости (если есть).

4. Напишите свой простейший NSE-скрипт, который выводит "Hello from custom script!". Сохраните его как `/usr/share/nmap/scripts/custom-hello.nse` и запустите.

   Подсказка: базовый шаблон:
   ```lua
   description = "My custom script"
   author = "Your Name"
   categories = {"safe"}
   
   action = function(host, port)
     return "Hello from custom script!"
   end
   ```

5. Используйте скрипт `http-methods` для проверки разрешенных HTTP методов (PUT, DELETE и др.). Является ли это уязвимостью, если разрешен PUT?

## Частые ошибки

1. **Запуск intrusive скриптов без разрешения** — скрипты категории `intrusive` могут вызвать сбои на целевой системе, используйте только с разрешения.

2. **Неправильный путь к скриптам в macOS** — в macOS путь отличается: `/opt/homebrew/share/nmap/scripts/` вместо `/usr/share/nmap/scripts/`.

3. **Забыли указать порт для скрипта** — многие скрипты работают только на конкретных портах (например, smb-* требуют `-p 445`).

4. **Игнорирование зависимостей скриптов** — некоторые скрипты требуют дополнительные аргументы (через `--script-args`).

## Вопросы на понимание

1. В чем разница между категориями `safe` и `intrusive` в NSE?

2. Как узнать, какие аргументы требуются для конкретного NSE-скрипта?

3. Почему скрипты категории `vuln` могут быть опасны для целевой системы?

4. Как написать свой NSE-скрипт и где его сохранить?


