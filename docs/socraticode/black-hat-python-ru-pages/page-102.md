# Black Hat Python. Программирование для хакеров и пентестеров — страница 102

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

102   Глава 5. Веб-хакерство
Определение структуры каталогов WordPress
Допустим, известно, что интересующее вас веб-приложение использует
фреймворк W ordPress. Посмотрим, как выглядит его структура каталогов.
Скачайте и распакуйте копию W ordPress. Последнюю версию можно получить
на странице https://wordpress.org/download/. Здесь мы задействуем W ordPress 5.4.
Несмотря на то что расположение файлов может отличаться от того, которое
используется на атакуемом сервере, это станет хорошей отправной точкой для
поиска файлов и каталогов, имеющихся в большинстве версий.
Чтобы получить карту файлов и каталогов, поставляемых в стандартном дис-
трибутиве W ordPress, создайте файл с именем mapper.py. Давайте напишем
функцию под названием gather_paths, которая будет обходить дистрибутив
и вставлять каждый полный путь к файлу в очередь web_paths:
import contextlib
import os
import queue
import requests
import sys
import threading
import time
FILTERED = [".jpg", ".gif", ".png", ".css"]
TARGET = "http://boodelyboo.com/wordpress" 
THREADS = 10
answers = queue.Queue()
web_paths = queue.Queue() 
def gather_paths():
    for root, _, files in os.walk('.'): 
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERED:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)
@contextlib.contextmanager
def chdir(path): 
    """
    Сначала переходим по заданному пути.
    В конце возвращаемся в исходную папку.
    """
    this_dir = os.getcwd()
