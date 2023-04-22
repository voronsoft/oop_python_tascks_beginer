"""
Подвиг 3. В программе объявлены два класса следующим образом:

class Money:
    __slots__ = '_money',

    def __init__(self, value):
        self._money = value


class MoneyR(Money):
    __slots__ = '_value',
И, затем, выполняются команды:

m = MoneyR(10)
m._money = 100
m._value = 20

Выберите все верные утверждения, связанные с этой программой.

    если в классе MoneyR прописать __slots__ = '_value', '_money', а в базовом классе убрать определение __slots__, то поведение объекта m дочернего класса MoneyR не изменится
    программа выполнится без ошибок, так как коллекция __slots__ дочернего класса расширяет коллекцию __slots__ базового класса и атрибуты с именами _money и _value допустимы
программа завершится с ошибкой, так как коллекция __slots__ не наследуется и в объекте m дочернего класса MoneyR допустим только атрибут _value
программа завершится с ошибкой, так как коллекция __slots__ базового класса имеет приоритет и __slots__ дочернего класса будет проигнорирована
"""
