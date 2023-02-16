"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/qKTQLo-plpc

Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:
MoneyR - для рублевых кошельков
MoneyD - для долларовых кошельков
MoneyE - для евро-кошельков

Объекты этих классов могут создаваться командами:
rub = MoneyR()   # с нулевым балансом
dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
euro = MoneyE(100) # с балансом в 100 евро
В каждом объекте этих классов должны формироваться локальные атрибуты:
__cb - ссылка на класс CentralBank (центральный банк, изначально None);
__volume - объем денежных средств в кошельке (если не указано, то 0).
Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы с локальными атрибутами:
cb - для изменения и считывания данных из переменной __cb;
volume - для изменения и считывания данных из переменной __volume.

Объекты классов должны поддерживать следующие операторы сравнения:
rub < dl
dl >= euro
rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
euro > rub
При реализации операторов сравнения считываются соответствующие значения __volume
из сравниваемых объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют центрального банка.

Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки,
необходимо в программе объявить еще один класс CentralBank.
Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:
cb = CentralBank()
должно просто возвращаться значение None.
А в самом классе должен присутствовать атрибут:
rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
Здесь числа (в значениях словаря) - курс валюты по отношению к доллару.

Также в CentralBank должен быть метод уровня класса:
register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.
При регистрации значение __cb объекта money должно ссылаться на класс CentralBank.
Через эту переменную объект имеет возможность обращаться к атрибуту rates класса CentralBank и брать нужные котировки.
Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:
raise ValueError("Неизвестен курс валют.")

Пример использования классов (эти строчки в программе писать не нужно):
CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
r = MoneyR(45000)
d = MoneyD(500)
CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
P.S. В программе на экран ничего выводить не нужно, только объявить классы.
"""


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}  # курс валюты по отношению к доллару

    # Объекты класса CentralBank создаваться не должны (запретить), при выполнении команды:
    # cb = CentralBank()
    # должно просто возвращаться значение None.
    def __new__(cls, *args, **kwargs):
        return None

    # Также в CentralBank должен быть метод уровня класса:
    # register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.
    @classmethod
    def register(cls, money):
        money.cb = cls

    @classmethod
    def exchange(cls, obj_cash):
        r = cls.rates['rub']
        d = cls.rates['dollar']
        e = cls.rates['euro']
        
        if type(obj_cash) == MoneyR:
            return obj_cash.volume / r
        
        elif type(obj_cash) == MoneyD:
            return obj_cash.volume / d
        
        elif type(obj_cash) == MoneyE:
            return obj_cash.volume / e
        


# DESCRIPTOR
class Descriptor:
    """Дескриптор"""

    def __set_name__(self, owner, name):
        """Формируем имя"""
        self.name = "__" + name

    def __get__(self, instance, owner):
        """Получить значение"""
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """Записать значение"""
        instance.__dict__[self.name] = value


# END


class MoneyR:  # - для рублевых кошельков
    cb = Descriptor()
    volume = Descriptor()

    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """Rub"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


class MoneyD:  # - для долларовых кошельков
    cb = Descriptor()
    volume = Descriptor()

    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """D"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


class MoneyE:  # - для евро-кошельков
    cb = Descriptor()
    volume = Descriptor()

    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.cb = None
        self.volume = volume

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """E"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


# # TEST
# bank = CentralBank()
# rub = MoneyR(800)  # с нулевым балансом
# rub1 = MoneyR(800.005)  # с нулевым балансом
# dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро
# CentralBank.register(rub)
# CentralBank.register(rub1)
# CentralBank.register(dl)
# CentralBank.register(euro)
# x = dl > rub
# x1 = dl < rub
#
# x2 = dl >= euro
# x3 = dl <= euro
#
# x4 = rub == euro
# x5 = rub != euro
# x6 = euro > rub
# x7 = euro < dl
# x8 = euro > dl
# x9 = dl < euro
# x10 = rub == rub1
