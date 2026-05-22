# Glossary

| Термин | Простое объяснение для SDET | Security QA пример |
|---|---|---|
| Scope | Границы разрешенной проверки | только olddev.slider-ai.ru |
| Evidence | Доказательство результата | sanitized request/response, screenshot |
| Finding | Подтвержденная проблема | воспроизводимый риск с impact |
| Observation | Наблюдение без полного подтверждения | отсутствует header, нужен owner review |
| Retest | Проверка исправления | повторить safe check после фикса |
| False positive | Инструмент ошибся или контекст не подтверждает риск | scanner alert без воспроизведения |
| Stop condition | Условие немедленной остановки проверки | всплеск 5xx, блокировка аккаунта, изменение чужих данных |
| Automation appendix | Приложение к отчету с безопасными helpers | allowlist, pytest, sanitized output |
