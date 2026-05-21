# Black Hat Python. Программирование для хакеров и пентестеров — страница 124

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

124   Глава 6. Расширение прокси Burp Proxy
     * @return The name of the payload generator.
     */
String getGeneratorName(); 
    /**
     * This method is used by Burp when the user starts an Intruder
     * attack that uses this payload generator.
     * @param attack
     * An IIntruderAttack object that can be queried to obtain details
     * about the attack in which the payload generator will be used.
     * @return A new instance of
     * IIntruderPayloadGenerator that will be used to generate
     * payloads for the attack.
     */
IIntruderPayloadGenerator createNewInstance(IIntruderAttack attack); 
}
В первой части документации  говорится о том, что мы должны заре -
гистрировать наше расширение средствами Burp. Вместе с IIntruderPay-
loadGeneratorFactory  унаследуем главный класс Burp. Последний тре -
бует, чтобы мы реализовали в наследнике два метода. Burp вызовет метод
getGeneratorName  для получения имени нашего расширения, и мы должны
вернуть в ответ строку . Метод createNewInstance   должен возвращать
экземпляр IIntruderPayloadGenerator  — второго класса, который нужно
создать.
Т еперь приступим непосредственно к написанию кода на Python, который
будет удовлетворять этим требованиям, а позже придумаем, как добавить
класс IIntruderPayloadGenerator . Создайте файл с именем bhp_fuzzer.py
и наберите следующий код:
from burp import IBurpExtender 
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
from java.util import List, ArrayList
import random
class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory): 
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.registerIntruderPayloadGeneratorFactory(self) 
