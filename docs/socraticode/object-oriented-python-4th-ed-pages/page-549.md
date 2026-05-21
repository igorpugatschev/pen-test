# Объектно-ориентированный Python, 4-е издание — страница 549

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

548 ГЛ АВА 12 Н овы е патте рны про екти рова ния
graphvi z: Path = Pat h( "Ыn" ) / "do t",
plan tjar : Path = Path ("s har e" ) / "pl antuml .j ar" ,
-> None :
self .g raph viz = self .b ase_env / graphviz
self .p lantj ar = self .b ase_env / plantj ar
def proces s( self, source : Path) -> None :
env = {
"GR APHVI Z_DOT ": str( self . graphviz ),
}
command = [
"ja va", 1' -jar" ,
st r( self .p lantj ar) , "-pr ogr ess ",
str ( source )
]
subproce ss .r un( command, env=env , chec k=True )
prin t()
При создании виртуальной среды Case Study работа класса Pla ntUML зависит от
применения conda. При испо льзова нии других менеджеров виртуальной среды
подкласс может предоставлять все необходимые пути модификации. В указан­
ную виртуальную среду нужно установить пакет Graphviz. Тоr да диаграмма
будет представлена как файл изображе ния. Необходи мо также скачать файл
plan tuml .j ar. Поместим его в общий каталог внутри выбранной виртуальной
среды . Значение командной переменной предп олагает, что среда выполнения
Java (JRE) корректно установлена и видна.
Функция subpr ocess . run () принимает аргументы командной строки и любые
сп ециальные пере менные среды, которые необходимо установить. Функция
запустит ком анду в данной среде и проверит полученный код возврата, чтобы
убедиться, что программа работает правильно.
Также эти этапы можно испо льзова ть отдельно, чтобы найти все файлы UML
и создать диаграм мы. Пос кольку интерфейс немного сложен для понимания,
класс, работ ающий с патте рном Фасад, помог ает создать полезное приложение
командной строки.
class Generateim ages :
def �init �( self, base : Path) -> None :
self .f inder = Fin dUML (b ase)
self .p ain ter = Plan tUML ()
def make _all _imag es( self) -> None :
for source, ta rget in self .f ind er . uml_ file _iter ():
if (
not ta rget .e xists ()
or source .s ta t( ). st_mtime > ta rget .s ta t( ). st _mtime
) :
