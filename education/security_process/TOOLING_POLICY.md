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
