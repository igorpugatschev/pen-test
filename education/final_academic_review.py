#!/usr/bin/env python3
"""
Финальное ревью всех уроков на академичность, полноту и качество.
Запуск: python3 final_academic_review.py
"""

import os
import re
from pathlib import Path

EDUCATION_DIR = "/Users/formacepht/PycharmProjects/pen-test/education/lessons"
REPORT_FILE = "/Users/formacepht/PycharmProjects/pen-test/education/academic_review_report.md"

class LessonReviewer:
    def __init__(self):
        self.results = []
        self.total_score = 0
        self.max_score = 0
    
    def check_file_exists(self, filepath):
        """Проверка существования файла"""
        return os.path.exists(filepath)
    
    def check_encoding(self, filepath):
        """Проверка кодировки (UTF-8)"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                f.read()
            return True, "UTF-8"
        except Exception as e:
            return False, str(e)
    
    def check_structure(self, filepath):
        """Проверка структуры: теория, практика, примеры, ошибки, вопросы, macOS"""
        required_sections = [
            "## Теория",
            "## Практическое занятие",
            "## Примеры вывода",
            "## Частые ошибки",
            "## Вопросы на понимание",
            "## Задачи для самостоятельного выполнения"
        ]
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            missing = []
            for section in required_sections:
                if section not in content:
                    missing.append(section)
            
            # Проверка наличия адаптации под macOS
            has_macos = "## Адаптация под macOS" in content or "macOS" in content
            
            return missing, has_macos
        except Exception as e:
            return [f"Ошибка чтения: {e}"], False
    
    def check_content_quality(self, filepath):
        """Проверка качества контента: академичность, полнота"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            score = 0
            max_score = 0
            issues = []
            
            # 1. Академичность: наличие ссылок на источники
            max_score += 10
            if 'http://' in content or 'https://' in content:
                score += 10
            else:
                issues.append("Нет ссылок на источники")
            
            # 2. Полнота: объем контента (не менее 100 строк)
            max_score += 10
            if len(lines) >= 100:
                score += 10
            elif len(lines) >= 50:
                score += 5
                issues.append(f"Маловато контента: {len(lines)} строк (рекомендуется 100+)")
            else:
                issues.append(f"Критически мало контента: {len(lines)} строк")
            
            # 3. Логичность: наличие примеров кода
            max_score += 10
            if '```' in content:
                score += 10
            else:
                issues.append("Нет примеров кода")
            
            # 4. Доступность: наличие пояснений к коду
            max_score += 10
            # Считаем количество строк с пояснениями (не код)
            code_lines = 0
            explanation_lines = 0
            in_code = False
            for line in lines:
                if line.strip().startswith('```'):
                    in_code = not in_code
                    continue
                if in_code:
                    code_lines += 1
                else:
                    if line.strip() and not line.strip().startswith('#'):
                        explanation_lines += 1
            
            if explanation_lines >= code_lines * 0.5:
                score += 10
            else:
                issues.append(f"Мало пояснений к коду (пояснения: {explanation_lines}, код: {code_lines})")
            
            # 5. Непротиворечивость: проверка на дубликаты команд
            max_score += 10
            cmd_lines = [l for l in lines if 'cmd = [' in l]
            if len(cmd_lines) <= 1:
                score += 10
            else:
                issues.append(f"Дублирование команд: {len(cmd_lines)} раз")
            
            # 6. Проверка на localhost в payload (для веб-уязвимостей)
            max_score += 10
            if 'localhost:4444' in content or 'localhost:80' in content:
                issues.append("Используется localhost в payload (нужно IP хоста)")
                score += 5  # Половинчато
            else:
                score += 10
            
            return score, max_score, issues
        
        except Exception as e:
            return 0, 10, [f"Ошибка проверки: {e}"]
    
    def review_lesson(self, filepath):
        """Ревью одного урока"""
        lesson_name = os.path.basename(filepath)
        result = {
            'name': lesson_name,
            'path': filepath,
            'exists': True,
            'encoding_ok': True,
            'missing_sections': [],
            'has_macos': False,
            'score': 0,
            'max_score': 0,
            'issues': []
        }
        
        # Проверка существования
        if not self.check_file_exists(filepath):
            result['exists'] = False
            return result
        
        # Проверка кодировки
        enc_ok, enc_info = self.check_encoding(filepath)
        result['encoding_ok'] = enc_ok
        if not enc_ok:
            result['issues'].append(f"Проблема с кодировкой: {enc_info}")
        
        # Проверка структуры
        missing, has_macos = self.check_structure(filepath)
        result['missing_sections'] = missing
        result['has_macos'] = has_macos
        
        # Проверка качества контента
        score, max_score, issues = self.check_content_quality(filepath)
        result['score'] = score
        result['max_score'] = max_score
        result['issues'].extend(issues)
        
        # Добавляем информацию о пропущенных разделах
        if missing:
            result['issues'].append(f"Пропущены разделы: {', '.join(missing)}")
        if not has_macos:
            result['issues'].append("Нет адаптации под macOS")
        
        return result
    
    def review_all(self):
        """Ревью всех уроков"""
        print("="*60)
        print("ФИНАЛЬНОЕ РЕВЬЮ ПО АКАДЕМИЧНОСТИ")
        print("="*60 + "\n")
        
        all_files = []
        
        # Собираем все md файлы
        lessons_dir = Path(EDUCATION_DIR)
        for subdir in sorted(lessons_dir.iterdir()):
            if not subdir.is_dir():
                continue
            for md_file in sorted(subdir.glob("lesson_*.md")):
                all_files.append(str(md_file))
        
        print(f"Найдено файлов: {len(all_files)}\n")
        
        total_score = 0
        total_max_score = 0
        all_issues = []
        
        for filepath in all_files:
            result = self.review_lesson(filepath)
            self.results.append(result)
            
            total_score += result['score']
            total_max_score += result['max_score']
            
            if result['issues']:
                all_issues.extend([(result['name'], issue) for issue in result['issues']])
        
        # Генерируем отчет
        self.generate_report(total_score, total_max_score, all_issues)
        
        return total_score, total_max_score
    
    def generate_report(self, total_score, total_max_score, all_issues):
        """Генерация отчета"""
        report_lines = []
        report_lines.append("# Отчет о финальном ревью методических материалов\n")
        report_lines.append(f"**Дата**: 29 апреля 2026\n")
        report_lines.append(f"**Всего уроков**: {len(self.results)}\n")
        
        if total_max_score > 0:
            percentage = (total_score / total_max_score) * 100
        else:
            percentage = 0
        
        report_lines.append(f"## Общая оценка\n")
        report_lines.append(f"**Набранные баллы**: {total_score} из {total_max_score}\n")
        report_lines.append(f"**Процент**: {percentage:.1f}%\n")
        
        if percentage >= 90:
            report_lines.append("**Оценка**: Отлично! ✅\n")
        elif percentage >= 75:
            report_lines.append("**Оценка**: Хорошо 👍\n")
        elif percentage >= 60:
            report_lines.append("**Оценка**: Удовлетворительно ⚠️\n")
        else:
            report_lines.append("**Оценка**: Требует доработки ❌\n")
        
        # Детальный анализ по блокам
        report_lines.append("## Детальный анализ по блокам\n")
        
        blocks = {
            '01-08': 'Linux основы',
            '09-16': 'Сетевые технологии',
            '17-28': 'OWASP Top 10',
            '29-40': 'Инструменты пентеста',
            '41-48': 'Python для пентеста',
            '49-60': 'Практика на площадках',
            '61-72': 'Методология и сертификация'
        }
        
        for block_dir, block_name in blocks.items():
            block_results = [r for r in self.results if f"/{block_dir}/" in r['path']]
            if not block_results:
                continue
            
            report_lines.append(f"### Блок {block_dir}: {block_name}\n")
            
            block_score = sum(r['score'] for r in block_results)
            block_max = sum(r['max_score'] for r in block_results)
            if block_max > 0:
                block_pct = (block_score / block_max) * 100
            else:
                block_pct = 0
            
            report_lines.append(f"**Оценка блока**: {block_pct:.1f}% ({block_score}/{block_max})\n")
            
            # Топ проблем блока
            block_issues = []
            for r in block_results:
                if r['missing_sections']:
                    block_issues.append(f"{r['name']}: пропущены разделы {', '.join(r['missing_sections'])}")
                if not r['has_macos']:
                    block_issues.append(f"{r['name']}: нет адаптации под macOS")
                block_issues.extend([f"{r['name']}: {issue}" for issue in r['issues'] if 'localhost' in issue or 'Дублирование' in issue])
            
            if block_issues:
                report_lines.append("**Основные проблемы блока**:\n")
                for issue in block_issues[:5]:  # Топ-5 проблем
                    report_lines.append(f"- {issue}\n")
            
            report_lines.append("\n")
        
        # Топ-20 проблем по всем урокам
        report_lines.append("## Топ-20 проблем по всем урокам\n")
        issue_count = {}
        for name, issue in all_issues:
            key = issue.split(':')[0] if ':' in issue else issue
            if key not in issue_count:
                issue_count[key] = []
            issue_count[key].append(name)
        
        sorted_issues = sorted(issue_count.items(), key=lambda x: len(x[1]), reverse=True)
        for i, (issue, lessons) in enumerate(sorted_issues[:20], 1):
            report_lines.append(f"{i}. **{issue}** — затронуто уроков: {len(lessons)}\n")
            if len(lessons) <= 3:
                for lesson in lessons:
                    report_lines.append(f"   - {lesson}\n")
        
        # Рекомендации
        report_lines.append("## Рекомендации по улучшению\n")
        report_lines.append("1. **Добавить ссылки на официальную документацию** (OWASP, PTES, Nmap и т.д.)\n")
        report_lines.append("2. **Увеличить объем контента** до 100+ строк для каждого урока\n")
        report_lines.append("3. **Добавить больше пояснений** к примерам кода\n")
        report_lines.append("4. **Исправить оставшиеся ошибки** (localhost, дублирование команд)\n")
        report_lines.append("5. **Добавить академические ссылки** (RFC, официальные стандарты)\n")
        
        # Сохраняем отчет
        report_content = ''.join(report_lines)
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"Отчет сохранен: {REPORT_FILE}\n")
        print(report_content)

def main():
    reviewer = LessonReviewer()
    total_score, total_max_score = reviewer.review_all()
    
    print("="*60)
    print(f"ИТОГО: {total_score}/{total_max_score} баллов")
    if total_max_score > 0:
        print(f"Процент: {(total_score/total_max_score)*100:.1f}%")
    print("="*60)

if __name__ == "__main__":
    main()
