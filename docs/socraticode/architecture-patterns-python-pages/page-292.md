# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 292

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

ПРИЛОЖЕНИЕ Б
Шаблонная структура проекта
В главе 4 мы перешли от простого хранения всех элементов в одной папке
к более структурированному дереву и подумали, что было бы интересно
рассмотреть его в деталях.
Код для этого приложения находится в ветке appendix_project_structure
на GitHub 1 :
git clone https://github.com/cosmicpython/code.git
cd code
git checkout appendix_project_structure
Базовая структура папок выглядит следующим образом:
Дерево проекта
.
├── Dockerfile 
├── Makefile 
├── README.md
├── docker-compose.yml 
├── license.txt
├── mypy.ini
├── requirements.txt
├── src 
│ ├── allocation
│ │ ├── __init__.py
│ │ ├── adapters
│ │ │ ├── __init__.py
│ │ │ ├── orm.py
│ │ │ └── repository.py
│ │ ├── config.py
│ │ ├── domain
│ │ │ ├── __init__.py
1 См. https://oreil.ly/1rDRC
