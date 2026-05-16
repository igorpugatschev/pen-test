# Slider AI Practice Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add mandatory Slider AI test-stand practice to every lesson.

**Architecture:** Add one scope document and one idempotent generator for final lesson sections. Update the existing lesson validator so future course edits preserve the Slider AI practice requirement.

**Tech Stack:** Markdown, Python standard library, Bash.

---

### Task 1: Scope Document

**Files:**
- Create: `education/slider_ai_scope.md`

- [ ] Write the authorized target, allowed test types, prohibited actions, evidence rules, and reporting format.

### Task 2: Practice Generator

**Files:**
- Create: `education/tools/add_slider_ai_practice.py`

- [ ] Walk every lesson in `education/lessons/**/*.md`.
- [ ] Remove any existing `## Практика на Slider AI` section.
- [ ] Append a fresh block-specific Slider AI practice section as the final lesson section.
- [ ] Keep the script idempotent.

### Task 3: Validator Update

**Files:**
- Modify: `education/tools/check_lessons.sh`

- [ ] Require `## Практика на Slider AI` in every lesson.
- [ ] Require `https://olddev.slider-ai.ru` in every lesson.
- [ ] Preserve existing checks.

### Task 4: Verification

**Files:**
- All lessons

- [ ] Run `python3 education/tools/add_slider_ai_practice.py`.
- [ ] Run `bash education/tools/check_lessons.sh`.
- [ ] Run `python3 education/tools/final_academic_review.py`, then remove its generated root report.
- [ ] Inspect representative lessons from at least three blocks.
