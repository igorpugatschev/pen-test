#!/usr/bin/env python3
"""Validate that every lesson follows the self-contained course contract."""

from __future__ import annotations

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
    "nuclei -u http://example.com",
    "zap-cli active-scan http://example.com",
    "python3 secretsdump.py CORP/Administrator",
    "ticketer.py -domain-sid",
    "crackmapexec smb 192.168.1.0/24",
    "получить хеши через Mimikatz",
]


def main() -> int:
    lessons = sorted(LESSONS.glob("*/*.md"))
    missing: list[str] = []
    weak_sources: list[str] = []
    forbidden: list[str] = []

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

    for item in missing:
        print(f"[MISSING] {item}")
    for item in weak_sources:
        print(f"[SOURCE] {item}")
    for item in forbidden:
        print(f"[FORBIDDEN] {item}")

    print(f"OK: {len(lessons)} lessons checked")
    print(f"Missing sections: {len(missing)}")
    print(f"Missing book references: {len(weak_sources)}")
    print(f"Forbidden patterns: {len(forbidden)}")

    return 1 if missing or weak_sources or forbidden else 0


if __name__ == "__main__":
    raise SystemExit(main())
