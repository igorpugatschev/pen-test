#!/usr/bin/env python3
"""
Скрипт для добавления недостающих разделов во все уроки (49-60).
Запуск: python3 add_sections.py
"""

import os
import re
from pathlib import Path

# Директория с уроками
LESSONS_DIR = "/Users/formacepht/PycharmProjects/pen-test/education/lessons/49-60"

# Шаблоны разделов
SECTIONS = {
    "## Примеры вывода": """
## Примеры вывода

Пример вывода команд будет добавлен индивидуально для каждого урока.
""",
    
    "## Частые ошибки": """
## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.
""",
    
    "## Вопросы на понимание": """
## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>
""",
    
    "## Форматы флагов": """
## Форматы флагов

- **TryHackMe**: `THM{...}`
- **HackTheBox**: `HTB{...}`
- **PortSwigger**: "Lab solved!" (без флагов)
""",
    
    "## Адаптация под macOS (M2, 8GB)": """
## Адаптация под macOS (M2, 8GB)

- Для VPN используйте **Tunnelblick** (бесплатный OpenVPN клиент для macOS): скачайте .ovpn файл и откройте через Tunnelblick
- Виртуалки: используйте **UTM** (бесплатно для M2) или **Parallels** вместо VirtualBox
- "На 8GB RAM выделяйте VM не более 3-4GB"
- Docker работает нативно на M2: `docker pull <image>`
- Для установки инструментов используйте Homebrew: `brew install <tool>`
- Если требуется Python: `pip3 install <package>`
"""
}

def add_section_if_missing(filepath, section_name, content):
    """Добавляет раздел в файл, если его еще нет"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content_old = f.read()
        
        # Проверяем, есть ли уже такой раздел
        if section_name in content_old:
            print(f"  [ПРОПУЩЕНО] {os.path.basename(filepath)} — раздел {section_name} уже есть")
            return False
        
        # Добавляем раздел перед "## Задачи для самостоятельного выполнения"
        if "## Задачи для самостоятельного выполнения" in content_old:
            # Вставляем перед Задачами
            new_content = content_old.replace(
                "## Задачи для самостоятельного выполнения",
                content + "\n\n## Задачи для самостоятельного выполнения"
            )
        else:
            # Просто добавляем в конец
            new_content = content_old.rstrip() + "\n\n" + content + "\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  [ДОБАВЛЕНО] {os.path.basename(filepath)} — раздел {section_name}")
        return True
    
    except Exception as e:
        print(f"  [ОШИБКА] {os.path.basename(filepath)}: {e}")
        return False

def main():
    print("=" * 60)
    print("ДОБАВЛЕНИЕ НЕДОСТАЮЩИХ РАЗДЕЛОВ В УРОКИ 49-60")
    print("=" * 60)
    
    # Получаем список всех md файлов
    lessons_dir = Path(LESSONS_DIR)
    md_files = sorted(lessons_dir.glob("lesson_*.md"))
    
    print(f"\nНайдено файлов: {len(md_files)}\n")
    
    for md_file in md_files:
        print(f"Обработка: {md_file.name}")
        
        # Проверяем и добавляем каждый раздел
        for section_name, section_content in SECTIONS.items():
            add_section_if_missing(md_file, section_name, section_content)
        
        print()
    
    print("=" * 60)
    print("ГОТОВО! Проверьте файлы в", LESSONS_DIR)
    print("=" * 60)

if __name__ == "__main__":
    main()
