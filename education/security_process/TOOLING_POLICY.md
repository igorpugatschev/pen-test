# Tooling Policy

## Tool Classification

| Tool | Default mode | Slider AI use | Notes |
|---|---|---|---|
| Browser/DevTools | manual/passive | allowed | sanitize evidence |
| Burp | proxy/repeater | allowed with care | no Intruder unless approved |
| ZAP | passive | allowed with care | active scan requires approval |
| Nmap | single-port/low-rate | approval required | no broad scan by default |
| ffuf/dirsearch | wordlist | approval required | small list, low rate, stop conditions |
| Hydra/Patator | credential attack | forbidden by default | lab-only |
| Nuclei | templates | approval required | classify template intrusiveness |

## Safe Defaults For Automation

- allowlist target;
- dry-run by default;
- timeout;
- rate limit;
- max requests;
- token masking;
- JSON/Markdown output;
- pytest coverage for safety guards.

## Мини-пример для Slider AI

- Target: `https://olddev.slider-ai.ru`.
- Scope: только функции тестового стенда, доступные QA-учетной записи.
- Evidence: sanitized Markdown, без cookies, tokens, персональных данных и чужих данных.
- Ограничения: без DoS/load, brute force, destructive payloads, secrets extraction и действий вне согласованного scope.
- Статус результата: `finding`, `observation`, `not reproducible`, `not applicable` или `requires approval`.

## Tool approval card

- Tool:
- Target:
- Mode: passive / manual / low-rate / lab-only / forbidden
- Command:
- Rate limit:
- Stop conditions:
- Expected evidence:
- False positive review:
- Owner approval:
