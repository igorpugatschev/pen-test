# PyCharm. Профессиональная работа на Python 2024 — страница 318

Источник: `PyCharm. Профессиональная работа на Python 2024.pdf`

Метод render_template  – это вариативная	 функция.	 Вы  можете передать
в него столько параметров, сколько захотите. Jinja2 сможет отображать передан-
ные данные в шаблоне. Здесь мы просто добавляем одну переменную данных.
Мы закончили с app.py! Окончательный код выглядит так:
from flask import Flask, render_template
app = Flask (__name__)
library_data = list()
library_data.append({"python_library": "Flask",
            "description": "An unopinionated web framework",
            "rating": 5,
            "url": "https://pypi.org/project/Flask"})
library_data.append({"python_library": "Jinja2",
            "description": "Templating library",
            "rating": 3,
            "url": "https://pypi.org/project/Jinja2"})
@app.route('/', methods=['GET'])
def root(): # put application's code here
    return render_template("index.html", library_data=
library_data)
if __name__ == '__main__':
    app.run()
Теперь, когда мы передаем некоторые данные в шаблон, нужно вернуться
и изменить шаблон index.html для отображения данных. Вам нужно изменить
содержимое тега tbody на следующее:
<tbody>
        {% if library_data|length > 0 %}
Маркеры {% и {{	 в шаблоне отмечают места, где реализуется логика и кон-
тент. Здесь мы проверяем длину массива. Если она больше нуля, мы отобра-
жаем строки таблицы, используя содержимое массива. Дальше есть else, что
будет отображать то, что у нас есть сейчас, а именно одну строку, сообщающую
об отсутствии данных:
{% for data in library_data %}
   <tr>
      <td>{{ data.python_library }} </td>
      <td>{{ data.description }}</td>
      <td>
         {% for _ in range(data.rating) %}
          <i class="fas fa-star gold-star"></i>
         {% endfor %}
      </td>
      <td><a href="{{ data.url }}"
         target="_blank">View on pypi.org</a></td>
   </tr>
{% endfor %}
Глава 8. Создание динамических сетевых приложений с Flask  317
