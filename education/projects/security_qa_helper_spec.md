# Security QA Helper Project Spec

## Goal

Build a safe helper for headers/status/link inventory that can be used as an automation appendix in the final Slider AI assessment.

## Required behavior

- allowlist target validation;
- dry-run mode;
- timeout;
- rate limit;
- secret masking;
- JSON output;
- Markdown report;
- pytest tests for safeguards and output.

## Forbidden behavior

- no brute force;
- no directory wordlist by default;
- no payload injection;
- no cookie/token persistence;
- no targets outside allowlist.

## Lesson increments

| Lesson | Increment |
|---|---|
| 41 | allowlist and target model |
| 42 | HTTP client with timeout |
| 43 | PoC verification plan, no payload execution |
| 44 | parser for prepared nmap XML |
| 45 | passive domain inventory model |
| 46 | visible URL inventory |
| 47 | CVE candidate mapper with confidence |
| 48 | integrated CLI/report/tests |
