#!/bin/bash
# Скрипт проверки уроков на соответствие требованиям
# Запуск: bash check_lessons.sh

LESSONS_DIR="/Users/formacepht/PycharmProjects/pen-test/education/lessons"
ERRORS=0

echo "=========================================="
echo "ПРОВЕРКА УРОКОВ НА СООТВЕТСТВИЕ ТРЕБОВАНИЯМ"
echo "=========================================="
echo ""

# Функция проверки наличия раздела
check_section() {
    local file=$1
    local section=$2
    local lesson=$(basename "$file")
    
    if ! grep -q "$section" "$file" 2>/dev/null; then
        echo "  [ПРОБЛЕМА] $lesson — отсутствует раздел: $section"
        return 1
    fi
    return 0
}

# Функция проверки кодировки
check_encoding() {
    local file=$1
    local lesson=$(basename "$file")
    local encoding=$(file -I "$file" 2>/dev/null | grep -o "charset=.*" | cut -d= -f2)
    
    if [ "$encoding" != "utf-8" ] && [ "$encoding" != "us-ascii" ]; then
        echo "  [ПРОБЛЕМА] $lesson — неверная кодировка: $encoding (должно быть utf-8)"
        return 1
    fi
    return 0
}

# Функция проверки расширения
check_extension() {
    local file=$1
    local lesson=$(basename "$file")
    
    if [[ "$file" != *.md ]]; then
        echo "  [ПРОБЛЕМА] $lesson — неверное расширение (должно быть .md)"
        return 1
    fi
    return 0
}

# Функция проверки имени файла (латиница)
check_filename() {
    local file=$1
    local lesson=$(basename "$file")
    local name_no_ext="${lesson%.*}"
    
    if echo "$name_no_ext" | grep -q "[^a-zA-Z0-9_-]"; then
        echo "  [ПРОБЛЕМА] $lesson — имя файла содержит не-латинские символы"
        return 1
    fi
    return 0
}

# Функция проверки наличия кириллицы в содержании
check_cyrillic() {
    local file=$1
    local lesson=$(basename "$file")
    
    if ! grep -q "[а-яА-Я]" "$file" 2>/dev/null; then
        echo "  [ПРОБЛЕМА] $lesson — отсутствует текст на русском языке"
        return 1
    fi
    return 0
}

# Ожидаемые уроки (1-72)
expected_lessons=()
for i in $(seq -f "%02g" 1 72); do
    # Определяем директорию
    if [ "$i" -ge 1 ] && [ "$i" -le 8 ]; then
        dir="01-08"
    elif [ "$i" -ge 9 ] && [ "$i" -le 16 ]; then
        dir="09-16"
    elif [ "$i" -ge 17 ] && [ "$i" -le 28 ]; then
        dir="17-28"
    elif [ "$i" -ge 29 ] && [ "$i" -le 40 ]; then
        dir="29-40"
    elif [ "$i" -ge 41 ] && [ "$i" -le 48 ]; then
        dir="41-48"
    elif [ "$i" -ge 49 ] && [ "$i" -le 60 ]; then
        dir="49-60"
    elif [ "$i" -ge 61 ] && [ "$i" -le 72 ]; then
        dir="61-72"
    fi
    expected_lessons+=("$LESSONS_DIR/$dir/lesson_${i}_*.md")
done

echo "1. ПРОВЕРКА НАЛИЧИЯ ВСЕХ 72 УРОКОВ"
echo "------------------------------------------"

# Проверяем наличие файлов для каждого урока
missing_count=0
for i in $(seq -f "%02g" 1 72); do
    found=false
    # Определяем директорию
    if [ "$i" -ge 1 ] && [ "$i" -le 8 ]; then
        dir="01-08"
    elif [ "$i" -ge 9 ] && [ "$i" -le 16 ]; then
        dir="09-16"
    elif [ "$i" -ge 17 ] && [ "$i" -le 28 ]; then
        dir="17-28"
    elif [ "$i" -ge 29 ] && [ "$i" -le 40 ]; then
        dir="29-40"
    elif [ "$i" -ge 41 ] && [ "$i" -le 48 ]; then
        dir="41-48"
    elif [ "$i" -ge 49 ] && [ "$i" -le 60 ]; then
        dir="49-60"
    elif [ "$i" -ge 61 ] && [ "$i" -le 72 ]; then
        dir="61-72"
    fi
    
    if ls "$LESSONS_DIR/$dir/lesson_${i}_"*.md 1>/dev/null 2>&1; then
        found=true
    fi
    
    if [ "$found" = false ]; then
        echo "  [ОТСУТСТВУЕТ] Урок $i (ожидается в $dir/)"
        ((missing_count++))
        ((ERRORS++))
    fi
done

echo "  Найдено отсутствующих уроков: $missing_count"
echo ""

echo "2. ПРОВЕРКА СТРУКТУРЫ КАЖДОГО УРОКА"
echo "------------------------------------------"

total_lessons=0
for dir in "$LESSONS_DIR"/*/; do
    for file in "$dir"*.md; do
        [ -f "$file" ] || continue
        ((total_lessons++))
        lesson=$(basename "$file")
        
        echo "  Проверка: $lesson"
        
        # Проверка расширения
        check_extension "$file"
        
        # Проверка имени (латиница)
        check_filename "$file"
        
        # Проверка кодировки
        check_encoding "$file"
        
        # Проверка наличия текста на русском
        check_cyrillic "$file"
        
        # Проверка обязательных разделов
        sections=("## Теория" "## Практическое занятие" "## Примеры вывода" "## Частые ошибки" "## Вопросы на понимание" "## Задачи для самостоятельного выполнения" "## Адаптация под macOS")
        
        for section in "${sections[@]}"; do
            check_section "$file" "$section"
        done
        
        echo ""
    done
done

echo "3. ПРОВЕРКА ИСПРАВЛЕНИЯ ОШИБОК ИЗ РЕВЬЮ"
echo "------------------------------------------"

# Специфические проверки на основе ревью
echo "  Проверка урока 38 (Shodan - приватные IP)..."
if grep -q "192\.168" "$LESSONS_DIR/29-40/lesson_38_shodan_censys.md" 2>/dev/null | grep -v "ПРИМЕЧАНИЕ\|НЕ сканирует"; then
    echo "  [ПРОБЛЕМА] Урок 38 — возможно остались приватные IP для Shodan"
    ((ERRORS++))
fi

echo "  Проверка урока 44 (Python - дублирование команды Nmap)..."
# Проверяем только команды в коде (не в комментариях и не в тексте)
if [ -f "$LESSONS_DIR/41-48/lesson_44_python_nmap.md" ]; then
    # Считаем вхождения в блоках кода (между ```)
    in_code=0
    code_lines=0
    while IFS= read -r line; do
        if [[ "$line" == '```'* ]]; then
            if [ $in_code -eq 1 ]; then
                in_code=0
            else
                in_code=1
            fi
        elif [ $in_code -eq 1 ] && [[ "$line" =~ ^[[:space:]]*cmd[[:space:]]*=[[:space:]]*\[ ]]; then
            ((code_lines++))
        fi
    done < "$LESSONS_DIR/41-48/lesson_44_python_nmap.md"
    
    if [ "$code_lines" -gt 1 ]; then
        echo "  [ПРОБЛЕМА] Урок 44 — дублирование формирования команды Nmap ($code_lines раз)"
        ((ERRORS++))
    fi
fi

echo "  Проверка урока 20 (XSS - localhost в payload)..."
if grep -q "localhost:4444" "$LESSONS_DIR/17-28/lesson_20_xss.md" 2>/dev/null; then
    echo "  [ПРОБЛЕМА] Урок 20 — используется localhost в XSS payload (нужно IP хоста)"
    ((ERRORS++))
fi

echo "  Проверка урока 27 (Burp - установка CA сертификата)..."
if ! grep -q "CA-сертификат\|CA сертификат\|установка.*сертификат" "$LESSONS_DIR/17-28/lesson_27_burp_intro.md" 2>/dev/null; then
    echo "  [ПРОБЛЕМА] Урок 27 — отсутствует раздел установки CA-сертификата Burp"
    ((ERRORS++))
fi

echo "  Проверка урока 18 (SQLi - ORDER BY)..."
if ! grep -q "ORDER BY" "$LESSONS_DIR/17-28/lesson_18_sqli.md" 2>/dev/null; then
    echo "  [ПРОБЛЕМА] Урок 18 — отсутствует ORDER BY для определения числа колонок"
    ((ERRORS++))
fi

echo ""
echo "=========================================="
echo "ИТОГОВЫЙ ОТЧЕТ"
echo "=========================================="
echo "  Всего проверено уроков: $total_lessons из 72"
echo "  Всего проблем: $ERRORS"
echo ""

if [ "$ERRORS" -eq 0 ]; then
    echo "✅ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ УСПЕШНО!"
else
    echo "❌ ОБНАРУЖЕНЫ ПРОБЛЕМЫ: $ERRORS"
    echo "   Исправьте указанные проблемы и запустите проверку снова."
fi

exit $ERRORS
