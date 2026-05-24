# Пользовательская инструкция по прохождению курса

Эта инструкция описывает, как проходить Pen-Test Learning Program самостоятельно и безопасно. Курс рассчитан на QA/SDET-специалиста, который уже знаком с Python и базовой инженерной дисциплиной, но постепенно осваивает security testing.

## 1. Как устроено обучение

Проходите занятия последовательно. Не переходите к углублению, если не выполнен обязательный безопасный путь текущего урока.

Рекомендуемый ритм:

- 3 занятия в неделю;
- 1-2 часа на занятие;
- 70% времени на практику и evidence;
- 30% времени на чтение теории и ответы на вопросы.

Каждый урок нужно закрывать не “прочитал”, а артефактом: Markdown-заметкой, sanitized выводом команды, checklist, finding draft, helper output, report fragment или retest note.

## 2. Как читать лекцию

В каждой лекции сначала изучите учебную рамку:

- входные требования;
- результат занятия;
- безопасная цель;
- среда выполнения;
- минимальная проверка успеха;
- эталонный вывод;
- критерии сдачи.

После этого прочитайте теорию и выполните guided practice. Если вы не можете объяснить модель урока своими словами, практику пока не запускайте.

## 3. Два слоя практики

Обязательный безопасный путь новичка выполняется на macOS native, localhost, локальных файлах, браузере, DevTools или одиночном разрешенном наблюдении. Он не должен создавать нагрузку, менять чужие данные или требовать специальных разрешений.

Углубление выполняется только после освоения базовой темы. Для углубления используются Kali ARM64 VM, TryHackMe AttackBox, HackTheBox/Pwnbox, PortSwigger Academy или локальные deliberately vulnerable приложения.

## 4. Slider AI olddev

Единственная разрешенная продуктовая цель курса:

```text
https://olddev.slider-ai.ru
```

На Slider AI olddev разрешены только безопасные действия, явно совместимые с уроком: ручное наблюдение, DevTools, одиночные low-impact запросы, заполнение checklist, оформление evidence, finding draft, limitation и request for approval.

Запрещено:

- тестировать production;
- выполнять DoS/load/stress;
- выполнять brute force/password guessing;
- запускать destructive payloads;
- извлекать или сохранять secrets;
- сохранять cookies, tokens, passwords, PII;
- менять чужие данные;
- сканировать вне scope;
- переносить lab-only технику на olddev без отдельного written approval.

Если сомневаетесь, классифицируйте следующий шаг как `requires approval`.

## 5. Evidence

Каждый артефакт должен содержать:

- дату и номер урока;
- среду выполнения;
- target;
- scope status;
- команду или ручной шаг;
- 3-10 строк sanitized output или краткое описание UI-наблюдения;
- интерпретацию;
- limitation;
- следующий безопасный шаг.

Evidence не должен содержать cookies, tokens, passwords, private keys, PII, чужие данные и полные ответы, где могут быть секреты.

Минимальный формат:

```markdown
Lesson:
Environment:
Target:
Scope status:
Action:
Evidence:
Interpretation:
Limitations:
Next safe step:
Status: observation | finding | not applicable | not reproducible | requires approval
```

## 6. Рабочая среда MacBook Air M2

Базовый путь:

- macOS native;
- Homebrew или официальные installers;
- браузер и DevTools;
- Burp/ZAP в безопасном режиме;
- Python 3;
- nmap для разрешенных одиночных или lab-only проверок.

Kali Linux ARM64 VM используйте только как углубление. Рекомендуемый лимит для MacBook Air M2 8GB: 3-4GB RAM и 2 CPU. Тяжелые сценарии переносите в cloud lab.

VirtualBox и x86/x64 VM не являются базовым путем для Apple Silicon.

## 7. Критерии зачета урока

Зачет:

- теория объяснена своими словами;
- выполнен обязательный безопасный путь;
- получен ожидаемый результат;
- оформлен sanitized evidence.

Хорошо:

- добавлены ограничения, scope и причина выбора среды;
- результат классифицирован как observation/finding/not applicable/not reproducible/requires approval.

Отлично:

- результат превращен в SDET/Security QA артефакт: test case, checklist item, automation helper, finding draft, remediation note или retest step.

## 8. Как использовать книги

Книги являются источниками автора курса. Это значит, что лекции уже должны содержать достаточную теорию для выполнения заданий.

К книгам можно обращаться для углубленного понимания, но это не должно быть условием выполнения текущего урока. Если для задания не хватает термина, команды, примера, ожидаемого вывода или критерия сдачи внутри лекции, это дефект лекции.

## 9. Финальный результат курса

К концу курса студент должен собрать assessment package для Slider AI olddev:

- security test strategy;
- Rules of Engagement;
- safe checklist по OWASP/WSTG;
- sanitized evidence index;
- findings/observations;
- remediation backlog;
- retest plan;
- automation appendix на Python;
- итоговый отчет для команды.
