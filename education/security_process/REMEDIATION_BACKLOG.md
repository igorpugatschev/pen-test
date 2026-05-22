# Remediation Backlog

| ID | Risk | Recommendation | Owner | Priority | Target date | Retest status |
|---|---|---|---|---|---|---|
| | | | | | | |

## Priority Rules

- Critical/High confirmed findings first.
- Quick hardening with low regression risk can be grouped.
- Observations require product/security owner decision.

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
