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


# ваш код:
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


class MoneyR:  # - для рублевых кошельков
    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    # ########## property
    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    # ########## end property

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """Rub >"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """Rub <"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """Rub =="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """Rub !="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """Rub >="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """Rub <="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


class MoneyD:  # - для долларовых кошельков
    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    # ########## property
    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    # ########## end property

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """D >"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """D <"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """D =="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """D !="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """D >="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """D <="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


class MoneyE:  # - для евро-кошельков
    # __cb - ссылка на класс CentralBank (центральный банк, изначально None);
    # __volume - объем денежных средств в кошельке (если не указано, то 0).
    def __init__(self, volume=0):
        self.__cb = None
        self.__volume = volume

    # ########## property
    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    # ########## end property

    # ########## операции сравнения
    def __gt__(self, other):  # >
        """E >"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) > CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __lt__(self, other):  # <
        """E <"""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) < CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __eq__(self, other):  # ==
        """E =="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return abs(CentralBank.exchange(self) - CentralBank.exchange(other)) < 0.1  # 0.1
        else:
            raise ValueError('Неизвестен курс валют')

    def __ne__(self, other):  # !=
        """E !="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) != CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __ge__(self, other):  # >=
        """E >="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) >= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    def __le__(self, other):  # <=
        """E <="""
        if self.cb == CentralBank and other.cb == CentralBank:
            return CentralBank.exchange(self) <= CentralBank.exchange(other)
        else:
            raise ValueError('Неизвестен курс валют')

    # ########## END операции сравнения


# end ваш код

# TEST-TASK___________________________________
from test3_5.test_3_5_8 import test_8

test_8(CentralBank, MoneyR, MoneyE, MoneyD)
# END
