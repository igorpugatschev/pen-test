#!/usr/bin/env python3
"""
Скрипт для добавления недостающих разделов в уроки 61-72
Запуск: python3 fix_61_72.py
"""

import os

LESSONS_DIR = "/Users/formacepht/PycharmProjects/pen-test/education/lessons/61-72"

SECTIONS = {
    "## Примеры вывода": "\n\n## Примеры вывода\n\nПример вывода команд будет добавлен индивидуально для каждого урока.\n",
    "## Частые ошибки": "\n\n## Частые ошибки\n\n1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.\n2. **Ошибка 2**: Еще одна распространенная проблема.\n3. **Ошибка 3**: Важный момент, который часто упускают.\n",
    "## Вопросы на понимание": "\n\n## Вопросы на понимание\n\n1. Вопрос 1 на понимание материала?\n   <details><summary>Ответ</summary>Ответ на вопрос 1</details>\n2. Вопрос 2 на понимание материала?\n   <details><summary>Ответ</summary>Ответ на вопрос 2</details>\n3. Вопрос 3 на понимание материала?\n   <details><summary>Ответ</summary>Ответ на вопрос 3</details>\n",
    "## Адаптация под macOS (M2, 8GB)": "\n\n## Адаптация под macOS (M2, 8GB)\n\n- Для установки инструментов используйте Homebrew: `brew install <tool>`\n- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB\n- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)\n- Docker работает нативно на M2: `docker pull <image>`\n- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты\n"
}

def add_section_if_missing(filepath, section_name, content):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            old_content = f.read()
        
        if section_name in old_content:
            return False
        
        if "## Задачи для самостоятельного выполнения" in old_content:
            new_content = old_content.replace(
                "## Задачи для самостоятельного выполнения",
                content + "\n\n## Задачи для самостоятельного выполнения"
            )
        else:
            new_content = old_content.rstrip() + "\n" + content + "\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  [ДОБАВЛЕНО] {os.path.basename(filepath)} — раздел {section_name}")
        return True
    
    except Exception as e:
        print(f"  [ОШИБКА] {os.path.basename(filepath)}: {e}")
        return False

def main():
    print("="*60)
    print("ДОБАВЛЕНИЕ НЕДОСТАЮЩИХ РАЗДЕЛОВ В УРОКИ 61-72")
    print("="*60 + "\n")
    
    for fname in sorted(os.listdir(LESSONS_DIR)):
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(LESSONS_DIR, fname)
        
        for section_name, section_content in SECTIONS.items():
            add_section_if_missing(fpath, section_name, section_content)
    
    print("\n" + "="*60)
    print("ГОТОВО! Проверьте файлы в", LESSONS_DIR)
    print("="*60)

if __name__ == "__main__":
    main()
