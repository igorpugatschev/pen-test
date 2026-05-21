# Rules of Engagement

## Scope

- In scope: `https://olddev.slider-ai.ru`
- Out of scope: production, другие домены, инфраструктура третьих лиц, DoS/load, brute force, destructive payloads, изменение чужих данных, извлечение секретов.

## Contacts

- Owner:
- QA/SDET:
- Escalation contact:

## Allowed Activities

- Manual UI/API observation.
- DevTools/Burp/ZAP passive analysis.
- Low-rate checks only after approval.
- Lab-only execution for intrusive techniques.

## Stop Conditions

- 5xx spike.
- Account lockout risk.
- Unexpected data modification.
- Evidence may contain secrets.
- Any sign of production target.

## Evidence Rules

- Mask cookies, tokens, emails and personal data.
- Save request/response only after sanitization.
- Keep timestamp, component, URL path and test account context.
