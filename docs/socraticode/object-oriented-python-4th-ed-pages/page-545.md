# Объектно-ориентированный Python, 4-е издание — страница 545

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

544 ГЛА ВА 12 Н ов ы е пап ерн ы пр оек ти рова ния
self .t s = Tim eSince ( star t )
else :
h_m_s = sel f.ts. parse _t ime (s tar t )
if h_m_s != (s el f.t s.h r, self .t s.m in, sel f.t s.s ec) :
self .t s = Time Since ( star t )
return sel f.ts. in terv al( now )
Этот адаптер создает объект ТimeSince, когда это необходимо. Если TimeSince
отсутствует, адаптер должен его создать. Если объект TimeSince уже существу­
ет и испо льзует уже установленное начальное время , то экземпляр TimeSince
можно испо льзова ть повторно. Однако, как только класс LogProc essor смес тил
фокус на новое сообщение об ошибке, возникает необходимость создать новый
экземпляр TimeSince.
Рассмотрим пример окончательного проекта класса LogProcessor с испо льзо­
ванием класса Inter val Adapter:
class LogPro cess or :
def _in it_(
self,
log _ent ries : list [tuple [s tr, str, st r] ]
-> None :
self . log _entries = lo g_entries
self .t ime_c onvert = In ter va lAdap te r( )
def report (s elf) -> None :
fir st_ time, fi rst _s ev, fir st_ msg = self . log _ent ries [0]
for log _t ime , severity, mess age in self . log _ent ries :
if severity == "ER RO R" :
fir st_t ime = log _t ime
inter val = self .ti me_c onver t .ti me_off set (fi rst_ time , log_ti me )
print (f"{ inter va l :8.2 f} 1 {se ver ity :7 s} {messag e}" )
Здесь в процессе инициализации был создан экземпляр In te rva lA dapt er( ).
Затем этот объект прим енялся для вычисления каждой временной позиции,
а существующий класс TimeSince повторно испо льзовался без каких-либо мо­
дификаций исходного класса, причем класс LogProcessor не заботился о деталях
работы экземп ляра TimeSince.
Также в данном случае мы можем использовать наследование. Можно расширить
экземпляр ТimeSince, чтобы добавить к нему необходимый метод. Альтернати­
ва наследования - неплохая идея. Об ратите внимание: похоже, это как раз та
ситуация , когда нет единственного правильног о ответа. В некоторых случаях
имеет смыс л обдумать реализацию с наследованием и сравнить ее с реализацией
адаптера, проанализир овав, какая из них проще.
Для добавления метода к существующему классу вместо наследования мы можем
исполь зовать метод monkey patching. Python позволяет добавлять новый метод,
