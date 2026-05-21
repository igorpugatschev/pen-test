# Объектно-ориентированный Python, 4-е издание — страница 554

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

Buffer
Па тте рн Л ег ко вес 553
Message Factory
+List[ Listbytes] +getM essage(bu ffer: Buffer, start: int) -> Message
Созда ем
г------- �---- 1
�---�---�-� · flywe1ght : L------- ___ .J
Извлекаем
Point
latitude: bytes
N/S : bytes
longitude : bytes
EfW: bytes
Message
+buffer: Buffer
+offset: in t
+set_fields(bu ffer: Buffer, offset : int)
+fix(): Point
GPGGA GPGLL
+fix( ): Point +fix( ): Point
GPRMC
+fix( ): Point
Рис. 12 .lt. Сооб щение GP S на U М L- ди а гр амме
Для приме ра рассмотрим следующую диаграмму (рис. 12 .5).
Клиент
+B uffer
1 Буфер
� GPGGA
о id = 14 0682444 146048
68 GPL L г---. buffer = Buffer
offset = О
98 GPRMC
Рис. 12 .5. Ссылоч ная диаг рамма
Нек оторое клиентское приложение, изображе нное как объект Clie nt, содер­
жит ссылку на экзем пляр Buffer. Объект Cl ient считы вает в буфер множество
