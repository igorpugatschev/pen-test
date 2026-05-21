# Объектно-ориентированный Python, 4-е издание — страница 614

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Пр ове дение мо дул ьног о те сти р о вани я с помо щью pytest 61 3
Чтобы протестирова ть совместную работу клиента и сервера, нужно запустить
сервер в отдельном процессе. Не хотелось бы проводить его многократный запуск
и остановку (по скольку на это уходит много време ни), поэтому он запус кается
один раз и испо льзуется в нескольких тестах . Весь процесс разбит на две части
и начинается с двух фи кстур:
from �f utu re� import ann otat ions
impor t sub proc ess
import si gnal
impor t ti me
import pyt est
import logging
import sys
impor t remot e_l og ging _app
fr om typing impor t Iterator, Any
@pyt est .f ixture (sc ope= "s essio n")
def log _cat che r( ) -> Iter ator [N one ]:
prin t (" load ing serv er" )
р = su bproces s. Popen (
["p ytho nЗ ", "s rc/ log _c atch er .p y" ],
stdou t=s ubproces s. PIPE,
stderr =subpr oces s. STDO UT,
text=True,
)
tim e. sl eep( 0.2 5}
yield
p. terminate ()
p.w ai t()
if p. stdout :
prin t(p. stdout .r ead (})
as ser t (
p. retu rncode == -signal .S I GTER M .v alue
}, f"E rror in wat cher, retu rncode ={p . returnco de }"
@pyt est .f ixt ure
def logging _confi g( ) -> Iterat or [N one ]:
HOST, PORT = "l oca lhost ", 188 42
soc ket_ handler = logging .h andlers . Soc ketH andler( HOST, PORT )
remote_logg ing _app . logg er . addHand ler ( soc ket_ha ndler)
yield
soc ke t_h andler .c los e()
remote_logg ing _app . logg er. removeHa ndler( soc ket_ handler )
Фикстура log_c atcher запус кает в качестве подпроцесса сервер lo g_ catcher . ру.
Для этого в дeкopa тope @f ixtu re задана область видимости "s essi on", означа­
ющая, что все делается один раз для всего сеанса тестирован ия. Область види­
мости задается одним из строковых значений "funct ion", "cl ass", "module ",
