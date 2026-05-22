# Security Release Checklist

## Before Release

- [ ] Security findings triaged.
- [ ] High risks have owners.
- [ ] Retest plan exists.
- [ ] Security regression checks selected.
- [ ] Secrets were not committed.
- [ ] Evidence is sanitized.

## After Fix

- [ ] Retest completed.
- [ ] Finding status updated.
- [ ] Automation helper updated if applicable.
- [ ] Lessons learned added to strategy/backlog.

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
