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
