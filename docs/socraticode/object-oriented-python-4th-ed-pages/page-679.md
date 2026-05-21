# Объектно-ориентированный Python, 4-е издание — страница 679

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

678 ГЛАВА 11+ Ко нк уре нтн а я обрабо тка да нных
сбор регистраци онных сообщ ений. У совершенс твованная реализация станет об­
рабатывать очень большое количество одновременно обращающихся клиентов,
поск ольку в ней будут испо льзоваться методы Asy ncIO.
Сервер приложений �������� ��������
!О
Приложение 1 Приложение 2
\"socke tHaпdler "" Socke tHaпdler
�--___ , -'7'/ �-_,--�г,;;;:,о,; �-;;;;,-� �� -�-� - I-�
t---.,. \"Сокет/ /
Сервер регистрации
__ f� �С читывает Сборщик U ... записывает Файл
журнальных журнала
записей
Рис. 11+.1. С борщик ре ги стра цио нных за п и сей в об лак е
Центральной частью этой конструкции является сопрограмма, считыва ющая
регистра ционные записи из сок ета. В перечне ее действ ий будет ожидан ие
байт ов, составля ющих заголовок, а затем декодир ование заголовка для вычис­
ления размера полез ных данных. Сопр ограм ма считы вает нужное количество
байт ов, составл яющих полез ные данные регистра ционного сообщ ения, а затем
использует отдельную сопрограмму для обработки полезных данных. Функция
log_c atcher () имеет следующий вид:
SIZ E_FO RМAT = "> L"
SIZ E_BYT ES = struct .c alcs ize (SI ZE_F ORМAT )
async def lo g_catcher (
read er : asy ncio . StreamRe ader, writer : async io . StreamWriter
-> None :
count = 0
cli ent_ soc ket = writer . get_ext ra_i nfo("s ocke t")
size _header = await reader .r ead (SI ZE _BYTES )
while si ze_hea der :
payload _s ize = struct .u npack(S IZE _FO RМAT , size _hea der)
byt es_ payload = await read er . read ( payload _s i ze [0] )
awa it lo g_wri ter( bytes_pay lo ad)
count += 1
size _header = await reader .r ead ( SIZ E_BY TES)
prin t(f"Fr om {c lie nt_s oc ket . get peern ame ()}: {c ount} lines ")
