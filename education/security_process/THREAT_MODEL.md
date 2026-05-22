# Threat Model

## Asset

## Entry Points

| Entry point | Trust boundary | Abuse case | Expected control |
|---|---|---|---|
| | | | |

## Assumptions

-

## Open Questions

-

## Security QA Cases

| Abuse case | Safe test case | Evidence | Status |
|---|---|---|---|
| | | | |

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
