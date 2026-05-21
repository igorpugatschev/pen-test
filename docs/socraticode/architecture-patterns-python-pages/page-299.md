# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 299

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Приложение Б. Шаблонная структура проекта 299
метический характер, но обязателен. Для пакета, который на самом деле
никогда не попадет в PyPI, это будет прекрасно1 .
Файл Dockerfile
Файлы Dockerfile специфичны для каждого конкретного проекта, но вот
несколько ключевых этапов, которые, скорее всего, будут общими:
Наш файл Dockerfile (Dockerfile)
FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc postgresqldev musl-
dev python3-dev
RUN apk add libpq

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN apk del --no-cache .build-deps

RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests/

WORKDIR /src
ENV FLASK_APP=allocation/entrypoints/flask_app.py
FLASK_DEBUG=1 PYTHONUNBUFFERED=1
CMD flask run --host=0.0.0.0 --port=80
 У становка зависимостей системного уровня.
 У становка питоновских зависимостей (возможно, вы захотите отделить
свои зависимости среды разработки от зависимостей производственной
среды; ради упрощения кода мы здесь этого не сделали).
1 Дополнительные советы по setup.py см. в статье Хайнека о сборке пакетов по ссылке:
https://oreil.ly/KMWDz.
