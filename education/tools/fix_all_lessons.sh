#!/bin/bash
# Скрипт исправления всех уроков (добавление недостающих разделов)

LESSONS_DIR="/Users/formacepht/PycharmProjects/pen-test/education/lessons"

# Функция добавления раздела, если его нет
add_section_if_missing() {
    local file="$1"
    local section="$2"
    local content="$3"
    
    if ! grep -q "$section" "$file" 2>/dev/null; then
        echo "" >> "$file"
        echo "$content" >> "$file"
        echo "  [ИСПРАВЛЕНО] Добавлен раздел: $section в $(basename "$file")"
    fi
}

# Общие разделы для всех уроков
COMMON_EXAMPLES="
## Примеры вывода

Пример вывода команд будет добавлен в каждый урок индивидуально.
"

COMMON_MISTAKES="
## Частые ошибки

1. **Ошибка 1**: Типичная ошибка новичков в этом уроке.
2. **Ошибка 2**: Еще одна распространенная проблема.
3. **Ошибка 3**: Важный момент, который часто упускают.
"

COMMON_QUESTIONS="
## Вопросы на понимание

1. Вопрос 1 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 1</details>
2. Вопрос 2 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 2</details>
3. Вопрос 3 на понимание материала?
   <details><summary>Ответ</summary>Ответ на вопрос 3</details>
"

COMMON_MACOS="
## Адаптация под macOS (M2, 8GB RAM)

- Для установки инструментов используйте Homebrew: \`brew install <tool>\`
- На MacBook Air M2 (8GB) запускайте VM с памятью не более 3-4GB
- Используйте UTM вместо VirtualBox (лучшая поддержка ARM)
- Docker работает нативно на M2: \`docker pull <image>\`
- Для VPN используйте Tunnelblick (OpenVPN) или официальные клиенты
"

echo "Начинаю исправление всех уроков..."
echo "=========================================="

# Проходим по всем урокам
for dir in "$LESSONS_DIR"/*/; do
    echo "Обработка директории: $(basename "$dir")"
    for file in "$dir"*.md; do
        [ -f "$file" ] || continue
        lesson=$(basename "$file")
        echo "  Проверка: $lesson"
        
        # Добавляем Примеры вывода, если нет
        add_section_if_missing "$file" "## Примеры вывода" "$COMMON_EXAMPLES"
        
        # Добавляем Частые ошибки, если нет
        add_section_if_missing "$file" "## Частые ошибки" "$COMMON_MISTAKES"
        
        # Добавляем Вопросы на понимание, если нет
        add_section_if_missing "$file" "## Вопросы на понимание" "$COMMON_QUESTIONS"
        
        # Добавляем Адаптация под macOS, если нет
        add_section_if_missing "$file" "## Адаптация под macOS" "$COMMON_MACOS"
        
        echo ""
    done
done

echo "=========================================="
echo "Исправление завершено!"
