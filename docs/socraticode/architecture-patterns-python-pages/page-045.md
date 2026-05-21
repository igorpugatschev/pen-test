# Паттерны разработки на Python — Гарри Персиваль и Боб Грегори — страница 45

Источник: `Паттерны_разработки_на_Python_Гарри_Персиваль_и_Боб_Грегори.pdf`

Г лава 1. Моделирование предметной области 45
Еще примеры объектов-значений
from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple
@dataclass(frozen=True)
 class Name:
 first_name: str
 surname: str
 class Money(NamedTuple):
 currency: str
 value: int
Line = namedtuple('Line', ['sku', 'qty'])
def test_equality():
 assert Money('gbp', 10) == Money('gbp', 10)
 assert Name('Harry', 'Percival') != Name('Bob', 'Gregory')
 assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)
Эти объекты-значения совпадают с нашими интуитивными представлениями
о работе их значений. Совсем не важно, о какой банкноте в 10 фунтов мы го-
ворим, потому что все они имеют одинаковый номинал. Схожим образом два
полных имени эквивалентны, если совпадают имя и фамилия, и две товарных
позиции эквивалентны, если они имеют один и тот же клиентский заказ, код
продукта и количество. Вместе с тем объекту-значению по-прежнему можно
задавать сложное поведение. На самом деле широко принято поддерживать
операции со значениями, например математические операторы.
Вычисления с объектами-значениями
fiver = Money('gbp', 5)
tenner = Money('gbp', 10)
def can_add_money_values_for_the_same_currency():
 assert fiver + fiver == tenner
def can_subtract_money_values():
 assert tenner - fiver == fiver
def adding_different_currencies_fails():
 with pytest.raises(ValueError):
 Money('usd', 10) + Money('gbp', 10)
