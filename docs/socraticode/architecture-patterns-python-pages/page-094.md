# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 94

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

94 Часть I. Создание архитектуры для поддержки моделирования предметной области
Все решают эти задачи по-разному , но понадобится какой-то способ «раз-
гона» Flask, возможно, в контейнере, и обмена информацией с базой данных
Postgres. Если вы хотите посмотреть, как это сделали мы, то ознакомьтесь
с приложением Б.
Простая реализация
Реализовав приложение самым очевидным образом, можно получить что-
то вроде этого:
Первая версия приложения на основе Flask (flask_app.py)
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
import model
import orm
import repository
orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)
@app.route("/allocate", methods=['POST'])
def allocate_endpoint():
 session = get_session()
 batches = repository.SqlAlchemyRepository(session).list()
 line = model.OrderLine(
 request.json['orderid'],
 request.json['sku'],
 request.json['qty'],
 )
 batchref = model.allocate(line, batches)
 return jsonify({'batchref': batchref}), 201
Пока все идет хорошо. Возможно, вы подумали: «Ну что, Боб и Гарри, не
нужна нам ваша лишняя “архитектурно-космическая” чепуха».
Но минуточку — здесь нет команды фиксации транзакции базы данных.
На самом деле мы не сохраняем размещение заказа в базе данных. Т еперь
