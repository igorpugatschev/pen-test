# Security Automation Architecture

## Goal

Build safe Security QA helpers, not offensive tools by default.

## Required Guards

- allowlist;
- dry-run default;
- rate limit;
- timeout;
- max requests;
- clear refusal message;
- sanitized output;
- unit tests for blocked targets;
- README with scope and examples.

## Suggested Structure

```text
security_qa_helper/
├── clients/
├── models/
├── reports/
├── safeguards/
├── tests/
└── README.md
```

## Output Contract

```json
{
  "target": "https://olddev.slider-ai.ru",
  "check": "headers_inventory",
  "status": "observation",
  "evidence": [],
  "secrets_masked": true
}
```

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.
