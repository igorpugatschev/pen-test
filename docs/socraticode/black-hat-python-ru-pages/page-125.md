# Black Hat Python. Программирование для хакеров и пентестеров — страница 125

Источник: `Black Hat Python. Программирование для хакеров и пентестеров.pdf`

Фаззинг с использованием Burp   125
        return
    def getGeneratorName(self): 
        return "BHP Payload Generator"
    def createNewInstance(self, attack): 
        return BHPFuzzer(self, attack)
Этот простой каркас показывает, что нужно сделать, чтобы удовлетворять
первой группе требований. Любое создаваемое расширение должно импор-
тировать класс IBurpExtender . Мы также должны импортировать классы,
необходимые для написания генератора содержимого Intruder. Вслед за этим
определяем класс BurpExtender , который является наследником классов
IBurpExtender и IIntruderPayloadGeneratorFactory. Дальше регистрируем
его с помощью метода registerIntruderPayloadGeneratorFactory , чтобы
инструмент Intruder знал, что мы можем генерировать содержимое запросов.
Затем реализуем метод getGeneratorName  , который просто возвращает
название генератора содержимого. В конце находится реализация метода
createNewInstance  , который принимает параметр attack  и возвращает
экземпляр класса IIntruderPayloadGenerator  — мы назвали последний
BHPFuzzer.
Заглянем в документацию класса IIntruderPayloadGenerator, чтобы увидеть,
что нужно реализовать:
/**
 * This interface is used for custom Intruder payload generators.
 * Extensions
 * that have registered an
 * IIntruderPayloadGeneratorFactory must return a new instance of
 * this interface when required as part of a new Intruder attack.
 */
public interface IIntruderPayloadGenerator
{
 /**
 * This method is used by Burp to determine whether the payload
 * generator is able to provide any further payloads.
 *
 * @return Extensions should return
 * false when all the available payloads have been used up,
 * otherwise true
 */
 boolean hasMorePayloads(); 
 /**
