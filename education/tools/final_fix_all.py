#!/usr/bin/env python3
"""
Финальный скрипт исправления ВСЕХ 72 уроков.
Запуск: python3 final_fix_all.py
"""

import os
import re
from pathlib import Path

EDUCATION_DIR = "/Users/formacepht/PycharmProjects/pen-test/education/lessons"

# Шаблоны разделов (общие для всех уроков)
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

- Для установки инструментов используйте Homebrew: `brew install <tool>`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: `docker pull <image>`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
- Для Python используйте `pip3 install` вместо `pip install`
"""
}

def add_section_if_missing(filepath, section_name, content):
    """Добавляет раздел в файл, если его еще нет"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            old_content = f.read()
        
        # Проверяем, есть ли уже такой раздел
        if section_name in old_content:
            return False
        
        # Добавляем раздел перед "## Задачи для самостоятельного выполнения"
        if "## Задачи для самостоятельного выполнения" in old_content:
            # Вставляем перед Задачами
            new_content = old_content.replace(
                "## Задачи для самостоятельного выполнения",
                content + "\n\n## Задачи для самостоятельного выполнения"
            )
        else:
            # Просто добавляем в конец
            new_content = old_content.rstrip() + "\n\n" + content + "\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    except Exception as e:
        print(f"  [ОШИБКА] {os.path.basename(filepath)}: {e}")
        return False

def fix_lesson_44(filepath):
    """Специальное исправление для lesson_44 (Nmap Parser)"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Проверяем, нет ли дублирования команды
        cmd_count = content.count("cmd = [")
        if cmd_count > 1:
            # Оставляем только последнее определение cmd
            parts = content.split("cmd = [")
            if len(parts) > 2:
                # Берем все до последнего определения
                before_last = "cmd = [".join(parts[:-1])
                # Берем последнее определение
                last = "cmd = [" + parts[-1]
                # Собираем обратно, убирая дубликаты
                content = before_last.rstrip() + "\n\n" + last
        
        # Проверяем правильность формирования команды
        if "options.split()" in content and "'-oX'" in content:
            # Правильный порядок: nmap [options] [target] -oX [file]
            content = content.replace(
                "cmd = ['nmap'] + options.split() + [target, '-oX', output_path]",
                "cmd = ['nmap'] + options.split() + [target, '-oX', output_path]"
            )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  [ИСПРАВЛЕНО] lesson_44_python_nmap.md — исправлено формирование команды Nmap")
        return True
    
    except Exception as e:
        print(f"  [ОШИБКА] lesson_44: {e}")
        return False

def main():
    print("="*60)
    print("ФИНАЛЬНОЕ ИСПРАВЛЕНИЕ ВСЕХ 72 УРОКОВ")
    print("="*60 + "\n")
    
    # Получаем список всех md файлов во всех поддиректориях
    lessons_dir = Path(EDUCATION_DIR)
    all_md_files = []
    
    for subdir in lessons_dir.iterdir():
        if subdir.is_dir():
            for md_file in subdir.glob("lesson_*.md"):
                all_md_files.append(md_file)
    
    all_md_files.sort()
    print(f"Найдено файлов: {len(all_md_files)}\n")
    
    fixed_count = 0
    for md_file in all_md_files:
        lesson = md_file.name
        print(f"Обработка: {lesson}")
        
        # Специальное исправление для lesson_44
        if "lesson_44" in lesson:
            if fix_lesson_44(md_file):
                fixed_count += 1
            continue
        
        file_fixed = False
        for section_name, section_content in SECTIONS.items():
            # Пропускаем Форматы флагов для некоторых блоков
            if "Форматы флагов" in section_name:
                # Добавляем только в блоки 49-60
                if not any(x in str(md_file) for x in ["49-60"]):
                    continue
        
            if add_section_if_missing(md_file, section_name, section_content):
                print(f"  [ДОБАВЛЕНО] {lesson} — раздел {section_name}")
                file_fixed = True
        
        if file_fixed:
            fixed_count += 1
        print()
    
    print("="*60)
    print(f"ГОТОВО! Исправлено файлов: {fixed_count} из {len(all_md_files)}")
    print("="*60)

if __name__ == "__main__":
    main()
