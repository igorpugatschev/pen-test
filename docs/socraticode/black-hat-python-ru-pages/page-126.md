# Black Hat Python. Программирование для хакеров и пентестеров — страница 126

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

126   Глава 6. Расширение прокси Burp Proxy
 * This method is used by Burp to obtain the value of the next payload.
 *
 * @param baseValue The base value of the current payload position.
 * This value may be null if the concept of a base value is not
 * applicable (e.g. in a battering ram attack).
 * @return The next payload to use in the attack.
 */
 byte[] getNextPayload(byte[] baseValue); 
 /**
 * This method is used by Burp to reset the state of the payload
 * generator so that the next call to
 * getNextPayload() returns the first payload again. This
 * method will be invoked when an attack uses the same payload
 * generator for more than one payload position, for example in a
 * sniper attack.
 */
 void reset(); 
}
Итак, мы знаем, что нужно реализовать базовый класс, в котором должны
быть доступны три метода. Первый метод, hasMorePayloads , определяет,
продолжать ли передавать модифицированные запросы обратно инструменту
Burp Intruder. Для этого воспользуемся счетчиком. Как только счетчик до -
стигнет максимального значения, вернем False, чтобы прекратить генерацию
модифицированных запросов. Метод getNextPayload   получит исходное
содержимое перехваченного нами HTTP-запроса. Также можете выбрать
в HTTP-запросе несколько интересующих вас участков, в этом случае полу-
чите только те байты, которые планируете модифицировать (подробней об
этом позже). Этот метод позволяет видоизменить исходный тестовый случай
и затем вернуть его обратно Burp для последующей отправки. Последний ме-
тод, reset , применяется, если мы хотим сгенерировать заранее известный
набор модифицированных запросов, и во всех случаях позволяет пройтись по
всем параметрам, перечисленным на вкладке Intruder. Наш фаззер получится
не слишком вычурным, он просто будет модифицировать каждый HTTP-
запрос случайным образом.
Т еперь посмотрим, как это будет выглядеть в коде на языке Python. Добавьте
в конец файла bhp_fuzzer.py следующее:
class BHPFuzzer(IIntruderPayloadGenerator): 
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 10 
