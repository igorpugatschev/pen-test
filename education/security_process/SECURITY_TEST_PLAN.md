# Security Test Plan

## Objective

What risk or control is being checked:

## Scope

- Target:
- Component:
- Test account:
- Time window:

## Checks

| Check | Method | Tool | Safety limit | Expected evidence | Status |
|---|---|---|---|---|---|
| | manual | browser/DevTools | no destructive actions | screenshot/request | planned |

## Stop Conditions

-

## Reporting

- Finding template:
- Evidence location:
- Retest owner:

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
