#!/usr/bin/env python3
"""Validate that every lesson follows the self-contained course contract."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LESSONS = ROOT / "education" / "lessons"

REQUIRED = [
    "Входные требования",
    "Результат занятия",
    "Наследуемая SDET-компетенция",
    "Security QA-компетенция",
    "Связь с книгами",
    "Основной источник",
    "Что берем из источника",
    "Как это превращается в SDET/Security QA навык",
    "Что нельзя переносить на Slider AI без отдельного разрешения",
    "Reading pack из книг курса",
    "Source-driven theory",
    "Guided practice",
    "Практика на Slider AI",
    "Минимум",
    "Практика Slider AI",
    "Углубление после изучения следующих уроков",
    "Артефакт сдачи",
    "Критерий готовности",
    "Rubric",
    "Self-check",
]

BOOK_HINTS = [
    "Легкий способ выучить Python 3 еще глубже",
    "Объектно-ориентированный Python",
    "Паттерны разработки на Python",
    "PyCharm. Профессиональная работа на Python 2024",
    "Black Hat Python",
]

FORBIDDEN_PATTERNS = [
    "<команда из практики>",
    "<3-10 строк фактического вывода",
    "Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>",
    "Action: <выполненная безопасная проверка>",
    "Evidence: <санитизированный фрагмент>",
    "Next step: <что делать дальше>",
    "Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение.",
    "Книжный материал в уроке используется в трех шагах:",
    "nuclei -u http://example.com",
    "zap-cli active-scan http://example.com",
    "python3 secretsdump.py CORP/Administrator",
    "ticketer.py -domain-sid",
    "crackmapexec smb 192.168.1.0/24",
    "получить хеши через Mimikatz",
]

RISKY_COMMANDS = [
    "nmap -A",
    "nmap -p-",
    "sudo nmap -sS",
    "sudo nmap -O",
    "hydra ",
    "patator ",
    "ffuf ",
    "dirsearch ",
    "sqlmap ",
]

SAFE_CONTEXT = [
    "lab-only",
    "cloud lab",
    "localhost",
    "127.0.0.1",
    "requires approval",
    "не выполнять на Slider AI",
    "не выполняется на Slider AI",
    "только в лаборатории",
    "только для лаборатории",
    "учебная лаборатория",
]


def extract_section(text: str, heading: str) -> str:
    match = re.search(rf"^## {re.escape(heading)}:?\s*$", text, re.M)
    if not match:
        return ""
    start = match.start()
    next_match = re.search(r"^## [^#].*$", text[match.end():], re.M)
    if not next_match:
        return text[start:]
    return text[start: match.end() + next_match.start()]


def word_count(text: str) -> int:
    cleaned = text.replace("`", " ").replace("|", " ")
    return len([word for word in cleaned.split() if word.strip()])


def subsection_count(section: str) -> int:
    return sum(1 for line in section.splitlines() if line.startswith("### "))


def has_safe_context(text: str, index: int) -> bool:
    window = text[max(0, index - 500): index + 500].lower()
    return any(marker.lower() in window for marker in SAFE_CONTEXT)


def main() -> int:
    lessons = sorted(LESSONS.glob("*/*.md"))
    missing: list[str] = []
    weak_sources: list[str] = []
    forbidden: list[str] = []
    weak_quality: list[str] = []
    unsafe_commands: list[str] = []

    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8")
        for pattern in REQUIRED:
            if pattern not in text:
                missing.append(f"{lesson.relative_to(ROOT)}: missing `{pattern}`")
        if not any(book in text for book in BOOK_HINTS):
            weak_sources.append(f"{lesson.relative_to(ROOT)}: no known course book reference")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                forbidden.append(f"{lesson.relative_to(ROOT)}: forbidden pattern `{pattern}`")
        theory = extract_section(text, "Теория")
        if word_count(theory) < 1200:
            weak_quality.append(f"{lesson.relative_to(ROOT)}: theory too short for self-contained lecture")
        if subsection_count(theory) < 3:
            weak_quality.append(f"{lesson.relative_to(ROOT)}: theory has too few subsections")
        source = extract_section(text, "Source-driven theory")
        if word_count(source) < 120:
            weak_quality.append(f"{lesson.relative_to(ROOT)}: source-driven theory too short")
        for command in RISKY_COMMANDS:
            start = 0
            while True:
                index = text.find(command, start)
                if index == -1:
                    break
                if not has_safe_context(text, index):
                    unsafe_commands.append(
                        f"{lesson.relative_to(ROOT)}: risky command `{command.strip()}` lacks nearby safe context"
                    )
                start = index + len(command)

    for item in missing:
        print(f"[MISSING] {item}")
    for item in weak_sources:
        print(f"[SOURCE] {item}")
    for item in forbidden:
        print(f"[FORBIDDEN] {item}")
    for item in weak_quality:
        print(f"[QUALITY] {item}")
    for item in unsafe_commands:
        print(f"[SAFETY] {item}")

    print(f"OK: {len(lessons)} lessons checked")
    print(f"Missing sections: {len(missing)}")
    print(f"Missing book references: {len(weak_sources)}")
    print(f"Forbidden patterns: {len(forbidden)}")
    print(f"Quality problems: {len(weak_quality)}")
    print(f"Unsafe command contexts: {len(unsafe_commands)}")

    return 1 if missing or weak_sources or forbidden or weak_quality or unsafe_commands else 0


if __name__ == "__main__":
    raise SystemExit(main())
