# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 320

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

320 Приложение Д. Валидация
 Библиотека schema1 позволяет описывать структуру и валидацию со-
общений в приятной декларативной форме.
 Метод from_json читает строку как JSON и превращает ее в тип со-
общений.
Но здесь мы рискуем столкнуться с повторением, так как нужно указывать
поля дважды, поэтому можно ввести вспомогательную библиотеку , которая
унифицирует валидацию и объявление типов сообщений.
Фабрика команд со схемой (src/allocation/commands.py)
def command(name, **fields): 
 schema = Schema(And(Use(json.loads), fields), ignore_extra_
 keys=True) 
 cls = make_dataclass(name, fields.keys())
 cls.from_json = lambda s: cls(**schema.validate(s)) 
 return cls
def greater_than_zero(x):
 return x > 0
quantity = And(Use(int), greater_than_zero) 
Allocate = command( 
 orderid=int,
 sku=str,
 qty=quantity
)
AddStock = command(
 sku=str,
 qty=quantity
 Функция command принимает имя сообщения плюс именованные аргу-
менты kwargs для полей с полезной для сообщения информацией, где имя
kwarg — это имя поля, а значение — синтаксический анализатор.
 Используем функцию make_dataclass из модуля dataclass для динами -
ческого создания типа сообщений.
 Патчим метод from_json, направляя в динамический класс данных.
1 См. https://pypi.org/project/schema
