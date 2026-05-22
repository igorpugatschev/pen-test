# Security Test Strategy

## Product Context

- Product:
- Environment:
- Business-critical flows:

## Risk Areas

| Area | Risk | Security expectation | Evidence |
|---|---|---|---|
| Auth | | | |
| API | | | |
| Data | | | |
| UI | | | |
| Integrations | | | |

## Test Layers

- Manual exploratory checks:
- API checks:
- UI checks:
- Passive proxy checks:
- Safe automation helpers:
- Lab-only learning:

## Entry Criteria

- Scope confirmed.
- Test account ready.
- Evidence policy accepted.
- Stop conditions known.

## Exit Criteria

- Findings triaged.
- Observations classified.
- Remediation backlog created.
- Retest plan prepared.

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
