# Two-Layer Course Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a required two-layer beginner/deepening teaching frame to every lesson and enforce it with validation.

**Architecture:** Use a small repository tool to insert or refresh a standardized "Учебная рамка" per lesson based on lesson block metadata. Keep lesson content otherwise intact, with targeted cleanup for duplicate or unsafe examples.

**Tech Stack:** Markdown, Bash validator, Python standard library.

---

### Task 1: Course Frame Tool

**Files:**
- Create: `education/tools/add_learning_frames.py`

- [ ] Create a Python script that walks `education/lessons/**/*.md`, parses the first Markdown title, detects the lesson block from the path, and inserts a generated "## Учебная рамка" section after the title.
- [ ] If a lesson already has "## Учебная рамка", replace only that section.
- [ ] Generate block-specific values for safe target and learning paths.
- [ ] Run `python3 education/tools/add_learning_frames.py`.

### Task 2: Validator

**Files:**
- Modify: `education/tools/check_lessons.sh`

- [ ] Add required-methodology-field checks for every lesson.
- [ ] Check for all new field labels under "## Учебная рамка".
- [ ] Preserve existing structural and review checks.
- [ ] Run `bash education/tools/check_lessons.sh`.

### Task 3: Targeted Cleanup

**Files:**
- Modify: `education/lessons/49-60/lesson_49_tryhackme_intro.md`
- Modify: `education/lessons/29-40/lesson_36_hydra_patator.md`
- Modify: Nmap lessons with `192.168.1.1` examples

- [ ] Remove duplicate generated sections from lesson 49.
- [ ] Replace unsafe-looking `192.168.1.1` attack examples with explicit lab placeholders such as `192.168.100.20` and add scope wording where needed.
- [ ] Keep examples concrete enough for beginners to copy only after setting their own lab target.

### Task 4: Verification

**Files:**
- All modified lesson files

- [ ] Run `bash education/tools/check_lessons.sh`.
- [ ] Run `python3 education/tools/final_academic_review.py`, then remove its generated root report if it appears.
- [ ] Inspect a representative lesson from each block.
- [ ] Review `git diff --stat` and summarize the result.
