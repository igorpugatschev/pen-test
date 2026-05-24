# Security Process Templates

Этот файл собирает короткие рабочие шаблоны, которые используются во всех уроках курса. Они нужны не как бюрократия, а как способ превратить проверку безопасности в воспроизводимый SDET-процесс.

## Evidence Record

```markdown
Environment:
Target:
Scope status:
Action:
Command or browser path:
Observed result:
Interpretation:
Risk status: observation / finding / not reproducible / not applicable / requires approval
Sanitization notes:
Next safe step:
```

## Safe Test Case

```markdown
Objective:
Preconditions:
Allowed target:
Environment:
Steps:
Expected safe result:
Stop condition:
Evidence:
Pass criteria:
Requires approval when:
```

## Tool Approval Card

```markdown
Tool:
Mode: manual / passive / low-rate / lab-only / forbidden
Target:
Reason:
Rate limit:
Data modification risk:
Secret exposure risk:
Approved by:
Decision: allowed / lab-only / requires approval / forbidden
```

## Finding Draft

```markdown
Title:
Severity:
Affected area:
Scope:
Evidence:
Business impact:
Reproduction steps:
Recommended remediation:
Retest plan:
Security regression idea:
Sanitization notes:
```

## Retest Record

```markdown
Finding:
Fix version or commit:
Retest date:
Environment:
Steps repeated:
Observed result:
Status: fixed / partially fixed / not fixed / not reproducible
Regression coverage:
Next action:
```

## Lab-To-Product Transfer Note

```markdown
Lab skill:
Where practiced:
What was learned:
What is safe to transfer to Slider AI:
What remains lab-only:
What requires approval:
Product-safe test case:
Evidence format:
```

## Final Project Evidence Register

```markdown
Project:
Scope:
Rules of engagement:
Evidence item:
Source lesson:
Target:
Action:
Result status:
Report section:
Sanitization status:
Retest or follow-up:
```
