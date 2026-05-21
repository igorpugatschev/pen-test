# Evidence Policy

## What To Capture

- Timestamp.
- Environment.
- Component.
- User role.
- Request path without secrets.
- Sanitized response excerpt.
- Screenshot with masked sensitive data.

## What Not To Capture

- Real cookies/tokens.
- Passwords.
- Personal data.
- Secrets.
- Data belonging to other users.

## Naming

```text
evidence/YYYY-MM-DD_lesson-NN_component_short-result.md
screenshots/YYYY-MM-DD_lesson-NN_component.png
requests/YYYY-MM-DD_lesson-NN_sanitized.http
```
