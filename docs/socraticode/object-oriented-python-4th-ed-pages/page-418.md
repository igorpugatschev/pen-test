# Объектно-ориентированный Python, 4-е издание — страница 418

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

from path lib import Path
from typing import CallaЬle
def sca n_pyt hon_l (p ath : Path) -> int :
sl oc = 0
with path .o pe n() as source :
for line in source :
line = line .s tri p()
Пу ти фа йлово й сис те м ы 41 7
if line and not line . sta rtswith (" #") :
sloc += 1
return sl oc
def cou nt_s loc (p ath : Path, scanner : CallaЫe [[ Pat h], in t] ) -> int :
if path .n ame . star ts wit h( "."):
return 0
elif path .i s_fil e( ):
if path . su ffix ! = ". ру ":
return 0
with path . open () as source :
re turn scanner( path)
elif path .i s_d ir ():
count = sum(
count _s loc ( name, scanner) for name in path . iterd ir( ))
return count
else :
return 0
При стандартном испо льзовании pathlib редко приходится создавать большое
количество объектов Path. В данном приме ре базовый путь пре доставля ется
в качестве параметра. Основ ная часть манипуля ций с объектом Path заклю­
чается в поиске других файлов или каталогов относите льно данного объекта
Path. Оста льная часть обработ ки, связанной с путем, запраш ивает атрибуты
конкретного пути .
Функция cou nt_s loc () просма трива ет имя пути , пропуск ая имена, начина­
ющиеся с " . ". Это позволяет избежать " . " и " .. ", но также пропуск ает такие
каталоги, как . tox, . coverage или . gi t, создан ные нашими инструм ентами.
Существу ет три универсальных случая.
• Фактические файл ы, которые могут иметь исхо дный код Python. Убеди м­
ся, что имеется суффикс имени файла . ру, чтобы можно было открыть
файл. Для открытия и чтения каждого файла Python мы будем вызы вать
функцию sca n(). Су ществует несколько подходов к подсч ету исходног о
кода. Мы по казали один: поср едст вом функции scan _pyt hon_l ( }, которая
должна быть предоставл ена в качестве значения аргумента.
