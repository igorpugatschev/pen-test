# Slider AI Practice Design

## Goal

Adapt every lesson so the course ends with practical QA-oriented security work against the authorized Slider AI test stand at `https://olddev.slider-ai.ru`.

## Scope

The course is written for the project's QA owner. The target is the old development stand only. Production systems, unrelated Slider AI assets, third-party infrastructure, denial-of-service testing, destructive payloads, credential attacks, mass scanning, and persistence attempts are out of scope unless separately authorized in writing.

## Lesson Model

Every lesson ends with `## Практика на Slider AI`. This final section contains the target, authorization context, safety limits, a beginner task, a deepening task, expected artifacts, and completion criteria.

Tasks are block-specific:

- Linux lessons build the local evidence workspace and repeatable QA workflow.
- Network lessons inspect DNS, HTTP, TLS, redirects, and headers safely.
- OWASP lessons map the concept to non-destructive checks in the browser, Burp/ZAP, or DevTools.
- Tooling lessons use passive or low-impact modes, with explicit rate limits.
- Python lessons create safe helper scripts for response/header/form analysis.
- Practice-platform lessons convert learned platform methods into Slider AI QA checklists.
- Methodology lessons produce reports, RoE, risk matrices, and final assessment artifacts.

## Verification

The validator must require `## Практика на Slider AI` and `https://olddev.slider-ai.ru` in every lesson. A dedicated `education/slider_ai_scope.md` file documents allowed and forbidden actions.
