# Course Self-Contained Rewrite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Превратить курс Pen-Test Learning Program из структурно валидного набора материалов в самодостаточный учебный курс для SDET, переходящего в Security QA / pentest role.

**Architecture:** Работа идет в два потока: сначала усиливаются автоматические проверки качества лекций, затем уроки переписываются блоками с опорой на 5 книг из `docs/socraticode/` и требования из `education/lecture_requirements.md`. Каждый блок завершается локальной проверкой, методическим ревью и отдельным коммитом.

**Tech Stack:** Markdown, Bash, Python 3, SocratiCode indexes, existing scripts in `education/tools/`, course files in `education/lessons/`.

---

## Files And Responsibilities

- Modify: `education/lecture_requirements.md`  
  Уточнить измеримые критерии готовности лекции: глубина теории, запрет boilerplate, требования к эталонному выводу, безопасным target и книге как источнику.

- Modify: `education/tools/check_course_completeness.py`  
  Добавить проверки методического качества: короткая теория, шаблонные source-блоки, placeholder output, опасные команды без lab/scope-контекста, смешение macOS/Linux.

- Modify: `education/tools/check_lessons.sh`  
  Подключить усиленную проверку и сделать вывод пригодным для автора курса.

- Modify: `education/lessons/01-08/*.md`  
  Довести Linux/CLI-блок до эталона самодостаточных лекций.

- Modify: `education/lessons/09-16/*.md`  
  Переписать сетевой блок: OSI/TCP/IP/DNS/HTTP/TLS/Wireshark/routing/firewall как самостоятельную базу перед web security.

- Modify: `education/lessons/17-28/*.md`  
  Переписать OWASP-блок: каждая уязвимость должна объяснять модель, безопасный пример, evidence, scope, Slider AI-перенос.

- Modify: `education/lessons/29-40/*.md`  
  Переписать инструментальный блок: nmap, amass, subfinder, ffuf, nuclei, ZAP, hydra, searchsploit, Shodan/Censys только с clear RoE, lab-first и безопасной прогрессией.

- Modify: `education/lessons/41-48/*.md`  
  Переписать Python-блок под SDET ownership: безопасные helpers, allowlist, dry-run, tests, structured output, reports.

- Modify: `education/lessons/49-60/*.md`  
  Переписать lab/certification-блок: TryHackMe/HTB/PortSwigger как controlled training, без подмены лекции внешними платформами.

- Modify: `education/lessons/61-72/*.md`  
  Переписать process/certification/final-блок: PTES, OWASP WSTG, reports, CVSS, scanners, EJPT/OSCP, final project как система работы SDET Security Owner.

- Modify: `education/book_usage_map.md`  
  Сделать карту использования книг операционной: какой блок курса какие идеи берет из каких книг.

- Modify: `education/security_process_templates.md`  
  Добавить шаблоны evidence, RoE, test case, finding, retest, security regression, final report.

---

## Task 1: Freeze The Quality Contract

**Files:**
- Modify: `education/lecture_requirements.md`

- [ ] **Step 1: Add measurable readiness gates**

Add a section named `## 13. Измеримые критерии редакторской проверки` with these checks:

```markdown
## 13. Измеримые критерии редакторской проверки

Для авторской проверки каждая лекция должна пройти не только структурный валидатор, но и ручной методический gate:

- `Source-driven theory` содержит индивидуальное объяснение источников урока, а не повторяемый boilerplate.
- `Теория` содержит не менее 6 содержательных подразделов для фундаментальных тем и не менее 3 для обзорных/итоговых тем.
- Практика не использует термин, команду, флаг или инструмент, который не объяснен выше в этом же уроке или явно указан как знание из входных требований.
- В `Примеры вывода` есть конкретный эталонный вывод без placeholder-строк вида `<разрешенная цель>`, `<команда>`, `<вывод>`.
- Каждая команда помечена средой выполнения, если команда отличается между macOS, Kali/Linux или cloud lab.
- Каждое потенциально intrusive-действие имеет ограничение `lab-only`, `cloud lab`, `localhost` или `requires approval`.
- Slider AI используется только как `https://olddev.slider-ai.ru` и только в рамках `education/slider_ai_scope.md`.
```

- [ ] **Step 2: Run no-op validation**

Run:

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
```

Expected:

```text
Existing checks still pass, but the new quality contract is now documented.
```

- [ ] **Step 3: Commit**

```bash
git add education/lecture_requirements.md
git commit -m "docs: define measurable lecture quality gates"
```

---

## Task 2: Strengthen Automated Course Checks

**Files:**
- Modify: `education/tools/check_course_completeness.py`
- Modify: `education/tools/check_lessons.sh`

- [ ] **Step 1: Add checks for boilerplate source blocks**

In `check_course_completeness.py`, add forbidden or warning patterns for repeated source boilerplate:

```python
QUALITY_FORBIDDEN_PATTERNS = [
    "Этот урок опирается на книжные источники курса как на базу, а не как на факультативное чтение.",
    "Книжный материал в уроке используется в трех шагах:",
    "Target: <разрешенная учебная цель или https://olddev.slider-ai.ru>",
    "Action: <выполненная безопасная проверка>",
    "Evidence: <санитизированный фрагмент>",
    "Next step: <что делать дальше>",
]
```

- [ ] **Step 2: Add section-depth checks**

Add parser logic:

```python
def extract_section(text: str, heading: str) -> str:
    start = text.find(f"## {heading}")
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + 1)
    return text[start: next_start if next_start != -1 else len(text)]

def word_count(text: str) -> int:
    return len([w for w in text.replace("`", " ").split() if w.strip()])

def subsection_count(section: str) -> int:
    return sum(1 for line in section.splitlines() if line.startswith("### "))
```

Check:

```python
theory = extract_section(text, "Теория")
if word_count(theory) < 1200:
    problems.append(f"{path}: theory too short for self-contained lecture")
if subsection_count(theory) < 3:
    problems.append(f"{path}: theory has too few subsections")
```

- [ ] **Step 3: Add risky-command checks**

Add warnings for:

```python
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
```

For every match, require nearby context containing one of:

```python
SAFE_CONTEXT = ["lab-only", "cloud lab", "localhost", "127.0.0.1", "requires approval", "не выполнять на Slider AI"]
```

- [ ] **Step 4: Wire the check into `check_lessons.sh`**

Ensure `check_lessons.sh` calls:

```bash
python3 education/tools/check_course_completeness.py
```

and exits non-zero if it fails.

- [ ] **Step 5: Run validation and expect failures**

Run:

```bash
python3 education/tools/check_course_completeness.py
```

Expected:

```text
The command reports current quality failures. This is expected before rewriting lessons.
```

- [ ] **Step 6: Commit**

```bash
git add education/tools/check_course_completeness.py education/tools/check_lessons.sh
git commit -m "test: enforce self-contained lecture quality gates"
```

---

## Task 3: Build The Source Extraction Workflow

**Files:**
- Modify: `education/book_usage_map.md`
- Modify: `education/security_process_templates.md`

- [ ] **Step 1: Define book-to-course mapping**

Update `education/book_usage_map.md` so each course block has this structure:

```markdown
## Block 09-16: Networks For Security QA

Primary source ideas:
- Network model, addressing, DNS, HTTP/TLS evidence.
- How observable network behavior becomes a reproducible QA artifact.

Books used:
- Black Hat Python: socket/network thinking, safe adaptation only.
- PyCharm Professional Python: reproducible developer workstation.
- Learn More Python 3: scripts, CLI habits, structured notes where applicable.

Course transformation:
- The student does not read the books to learn TCP/IP.
- The lecture explains TCP/IP directly, using the books as author sources.
- Practice stays on macOS native, browser DevTools, local commands and allowed targets.
```

- [ ] **Step 2: Define reusable process templates**

Add or update templates in `education/security_process_templates.md`:

```markdown
## Evidence Record

- Environment:
- Target:
- Scope status:
- Action:
- Command or browser path:
- Observed result:
- Interpretation:
- Risk status: observation / finding / not reproducible / not applicable / requires approval
- Sanitization notes:

## Safe Test Case

- Objective:
- Preconditions:
- Allowed target:
- Steps:
- Expected safe result:
- Stop condition:
- Evidence:
- Pass criteria:

## Finding Draft

- Title:
- Severity:
- Affected area:
- Evidence:
- Business impact:
- Reproduction steps:
- Recommended remediation:
- Retest plan:
```

- [ ] **Step 3: Commit**

```bash
git add education/book_usage_map.md education/security_process_templates.md
git commit -m "docs: map books to course blocks and process templates"
```

---

## Task 4: Rewrite Block 01-08 As The Baseline

**Files:**
- Modify: `education/lessons/01-08/*.md`

- [ ] **Step 1: Use lesson 01 as the model**

Compare every lesson in `01-08` against `lesson_01_intro_linux.md`.

For each lesson, ensure:

```text
Source-driven theory: individual, not boilerplate.
Theory: explains model, terms, examples, outputs, mistakes, boundaries.
Practice: macOS native first.
Examples: concrete output, no placeholders.
Slider AI: evidence/scope only unless the lesson has enough theory for site interaction.
```

- [ ] **Step 2: Rewrite lessons 02-08**

For each file:

```text
lesson_02_terminal.md
lesson_03_permissions.md
lesson_04_processes.md
lesson_05_network_linux.md
lesson_06_files_search.md
lesson_07_bash_scripts.md
lesson_08_linux_summary.md
```

Replace generic source blocks and short theory with complete lecture content.

- [ ] **Step 3: Validate block**

Run:

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
```

Expected:

```text
No failures for lessons 01-08.
Other blocks may still fail until rewritten.
```

- [ ] **Step 4: Commit**

```bash
git add education/lessons/01-08
git commit -m "docs: rewrite linux basics as self-contained lectures"
```

---

## Task 5: Rewrite Block 09-16 Networks

**Files:**
- Modify: `education/lessons/09-16/*.md`

- [ ] **Step 1: Fix heading consistency**

Replace headings like:

```markdown
## Теория:
```

with:

```markdown
## Теория
```

- [ ] **Step 2: Rewrite network theory**

Each lesson must explain its own model:

```text
09 OSI: layers, encapsulation, where evidence appears.
10 TCP/IP: IP, ports, TCP/UDP, subnet basics, safe local checks.
11 DNS: resolver flow, records, TTL, CNAME, NXDOMAIN, evidence.
12 HTTP/HTTPS: request/response, headers, cookies, TLS boundary, DevTools.
13 Wireshark: capture model, filters, legal boundaries, local/lab-only traffic.
14 Routing: gateway, traceroute, NAT, VPN impact.
15 Firewall: allow/deny, local firewall, product symptoms.
16 Network practice: integrated safe diagnosis workflow.
```

- [ ] **Step 3: Make macOS native primary**

Use macOS commands first:

```bash
ifconfig
ipconfig getifaddr en0
scutil --dns
dig olddev.slider-ai.ru
curl -I https://olddev.slider-ai.ru
traceroute olddev.slider-ai.ru
```

Linux/Kali commands such as `ip addr show` must be marked as:

```text
Среда: Kali/Linux углубление.
```

- [ ] **Step 4: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/09-16
git commit -m "docs: rewrite network block as self-contained lectures"
```

---

## Task 6: Rewrite Block 17-28 OWASP

**Files:**
- Modify: `education/lessons/17-28/*.md`

- [ ] **Step 1: Apply one vulnerability template to every lesson**

Each lesson must contain:

```text
1. What the vulnerability is.
2. Why it happens.
3. Data flow or request flow.
4. Safe lab example.
5. What is forbidden on Slider AI.
6. How SDET turns it into a test case.
7. Evidence and report language.
8. Retest criteria.
```

- [ ] **Step 2: Separate lab payloads from Slider AI checks**

For SQLi/XSS/SSRF/XXE/auth lessons:

```text
Lab-only: exploit payloads and destructive/intrusive probes.
Slider AI: safe observation, form behavior, headers, validation, error handling, no destructive payloads.
Requires approval: anything that can modify data, enumerate accounts, brute force or extract secrets.
```

- [ ] **Step 3: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/17-28
git commit -m "docs: rewrite owasp block for security qa learning"
```

---

## Task 7: Rewrite Block 29-40 Tools

**Files:**
- Modify: `education/lessons/29-40/*.md`

- [ ] **Step 1: Rebuild Nmap lessons first**

For `lesson_29_nmap_basics.md` and `lesson_30_nmap_nse.md`:

```text
Start with localhost and one explicitly allowed lab host.
Move subnet scans, SYN scan, OS detection, -A, -p-, vuln scripts to lab-only/deepening.
Explain every flag before use.
Replace x86_64 macOS output with Apple Silicon-compatible output.
```

- [ ] **Step 2: Rebuild enumeration tools**

For amass/subfinder/ffuf/dirsearch/nuclei/ZAP:

```text
Passive before active.
Rate limits explained.
No production.
No brute force against Slider AI.
Structured JSON/Markdown evidence.
False positive review required.
```

- [ ] **Step 3: Rebuild high-risk lessons**

For hydra/patator/searchsploit/Shodan/Censys:

```text
Hydra/patator: lab-only.
Searchsploit: research and patch-awareness first, exploitation only lab-only.
Shodan/Censys: passive OSINT only, no probing third-party assets.
```

- [ ] **Step 4: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/29-40
git commit -m "docs: rewrite tool block with safe progression"
```

---

## Task 8: Rewrite Block 41-48 Python Security QA

**Files:**
- Modify: `education/lessons/41-48/*.md`

- [ ] **Step 1: Define Python safety model in every tool**

Each Python lesson must teach:

```text
allowlist
dry-run
timeout
rate limit
structured output
sanitized evidence
unit test or smoke test
clear separation of lab and product target
```

- [ ] **Step 2: Fix socket and target inconsistencies**

For `lesson_41_python_sockets.md`:

```text
If the code only allows localhost, examples must use localhost.
If Slider AI appears, it must be dry-run evidence planning only, or code must explicitly parse HTTPS host safely without port scanning.
```

- [ ] **Step 3: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/41-48
git commit -m "docs: rewrite python block for sdet security ownership"
```

---

## Task 9: Rewrite Block 49-60 Labs And Certification Bridge

**Files:**
- Modify: `education/lessons/49-60/*.md`

- [ ] **Step 1: Stop external labs from replacing lectures**

TryHackMe, HTB and PortSwigger lessons must explain the learning model inside the lecture:

```text
What skill is trained.
What legal boundary applies.
What evidence is collected.
What transfers to Slider AI.
What remains lab-only.
```

- [ ] **Step 2: Separate exam practice from product QA**

Ensure:

```text
CTF exploitation stays in cloud/lab.
Slider AI receives only safe professional QA checks.
Exam notes are mapped to SDET workflow: plan, execute, evidence, report, retest.
```

- [ ] **Step 3: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/49-60
git commit -m "docs: rewrite labs block as controlled certification bridge"
```

---

## Task 10: Rewrite Block 61-72 Process, Reporting, Final Project

**Files:**
- Modify: `education/lessons/61-72/*.md`

- [ ] **Step 1: Turn standards into process lessons**

PTES, OWASP WSTG, NIST, CVSS lessons must teach:

```text
How to plan a test.
How to select test cases.
How to define RoE.
How to record evidence.
How to classify observation vs finding.
How to report and retest.
How SDET owns security regression.
```

- [ ] **Step 2: Rewrite final project**

Final project must require:

```text
Scope statement for olddev.slider-ai.ru.
RoE.
Test plan.
Evidence register.
Safe execution log.
Findings report.
Retest plan.
Security regression checklist.
Reflection: what remains requires approval.
```

- [ ] **Step 3: Validate and commit**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
git add education/lessons/61-72
git commit -m "docs: rewrite process block and final project"
```

---

## Task 11: Final Whole-Course Review

**Files:**
- Review all: `education/lessons/**/*.md`
- Review: `README.md`
- Review: `education/book_usage_map.md`
- Review: `education/security_process_templates.md`

- [ ] **Step 1: Run structural checks**

```bash
python3 education/tools/check_course_completeness.py
bash education/tools/check_lessons.sh
```

Expected:

```text
No missing sections.
No boilerplate source blocks.
No placeholder output.
No risky commands without safe context.
```

- [ ] **Step 2: Run manual sample review**

Manually inspect:

```text
lesson_01_intro_linux.md
lesson_10_tcp_ip.md
lesson_18_sqli.md
lesson_29_nmap_basics.md
lesson_41_python_sockets.md
lesson_62_owasp_testing.md
lesson_72_final_project.md
```

For each file, confirm:

```text
The student can learn from the Markdown file alone.
Practice requires only previously explained material.
Slider AI instructions are safe and in scope.
Examples are concrete.
Rubric is actionable.
```

- [ ] **Step 3: Update README**

Ensure `README.md` states:

```text
The course is a continuation of SDET Python QA Automation Apprenticeship.
The course trains SDET to own product security quality.
The course uses 5 books as author sources.
macOS native is the beginner path.
Kali ARM64 VM and cloud labs are deepening paths.
Slider AI practice is limited to olddev and scope.
```

- [ ] **Step 4: Final commit**

```bash
git add README.md education
git commit -m "docs: complete self-contained security qa course rewrite"
```

---

## Execution Order

1. Task 1: Freeze quality contract.
2. Task 2: Strengthen validators.
3. Task 3: Make books and process templates operational.
4. Task 4: Rewrite 01-08.
5. Task 5: Rewrite 09-16.
6. Task 6: Rewrite 17-28.
7. Task 7: Rewrite 29-40.
8. Task 8: Rewrite 41-48.
9. Task 9: Rewrite 49-60.
10. Task 10: Rewrite 61-72.
11. Task 11: Final whole-course review.

Recommended commit rhythm: one commit per task. Do not push until at least one complete block passes validation and manual review.

## Definition Of Done

- Every lesson passes structural validation.
- Every lesson passes strengthened quality checks.
- Manual sample review confirms the Markdown file is enough for self-study.
- No generic source-driven boilerplate remains.
- No placeholder etalon output remains.
- Risky commands are lab-only, cloud-only, localhost-only or require approval.
- Slider AI tasks use only `https://olddev.slider-ai.ru` and stay inside `education/slider_ai_scope.md`.
- README, book usage map and process templates match the final course model.
