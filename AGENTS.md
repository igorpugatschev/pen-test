# AGENTS.md

- Пиши на русском языке
- Education repo: 72 penetration testing lessons in Markdown
- Lessons: `education/lessons/` organized by blocks (01-08, 09-16, 17-28, 29-40, 41-48, 49-60, 61-72)
- Utility scripts: `education/tools/`
  - `bash check_lessons.sh` — validate lesson structure
  - `python3 final_fix_all.py` — auto-fix lesson errors
- `.venv/` exists but no `requirements.txt` or `pyproject.toml` present
- No build/test/lint config
- `.gitignore` excludes `.venv/`, `.idea/`, `__pycache__/`
