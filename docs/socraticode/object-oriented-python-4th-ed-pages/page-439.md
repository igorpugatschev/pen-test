# Объектно-ориентированный Python, 4-е издание — страница 439

Источник: `_media_books_obektno-orientirovannyj-python-4-izd.pdf`

438 ГЛА ВА 9 Стр ок и , сер иализ а ци я и пути к фа йлам
класс ифика ции. Пр ежде чем что-либо делать, убедимся, что образец документа
имеет прав ильные атрибуты.
Док умент JSON также написан в форма те JS ОN. Он включает в себя некоторые
метаданные, помогающие понять цель и значение документа. Как правило, про­
ще создать словарь Python с опре делением JSО N Schema.
Рассмо трим приме р опре деления схемы Iris для отдельного образца:
IRIS _S CHEМA = {
"$sc hema" : "h ttps :/ /js on -sch ema . org/d raft/ 2019 -09/hyp er-sc hema",
"titl e" : "I ris Data Schem a",
"d esc rip tion ": "Sc hema of Bezdek Iris data ",
"t yp e" : "o bject ",
"pr oper t ies ": {
"s epal _leng th" : {
"typ e" : "nu mber" , "desc rip ti on ": "S epal Length in cm" },
"s epal _wid th" : {
"t ype" : "nu mber ", "descrip tio n" : "S epal Width in cm" },
"p etal _leng th" : {
"t ype" : "n umber ", "d escrip tion ": "P etal Length in cm" },
"p etal _width ": {
"t ype" : "nu mber ", "desc rip tion ": "P etal Width in cm" },
"s pecies ": {
},
"t ype" : "s trin g" ,
"desc riptio n" : "c la ss",
"e num" : [
"Ir is -seto sa ", "Iris-v ersi color ", "Ir is -virg inica "],
},
"r equir ed" :
"s epal _leng th" , "s epal _wid th ", "p etal _leng th ", "p etal _wid th" ],
}
Каждый образец - это объект, элемент JSON Schema для слова ря с ключами
и значениями. Свойс тва объекта - это ключи словаря. Все они описыв аются
типом данных, в данном случае числом. Мы можем предостав ить дополн итель­
ную информацию, например диапазоны значений, и уже предостав или описание
из файла iris . names.
Для подтверж дения того, что данные соответствуют нашим общим ожиданиям,
в случае свойс тва species мы с вами предостав или еще и переч исление допу­
стимых строковых значений.
Ис пользуем данную информацию о схеме, создавая валидатор j sonsc hema и при­
меняя его для проверки каждого считанного образца. Ра сширенный класс будет
выг лядеть следующим обра зом:
