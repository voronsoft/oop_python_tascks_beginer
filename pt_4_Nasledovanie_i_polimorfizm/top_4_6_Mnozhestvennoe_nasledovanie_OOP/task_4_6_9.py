"""
Подвиг 9. Объявите класс с именем Money (деньги), объекты которого создаются командой:

money = Money(value)
где value - любое число (целое или вещественное). Если указывается не числовое значение, то генерируется исключение командой:

raise TypeError('сумма должна быть числом')
В каждом объекте этого класса должен формироваться локальный атрибут _money с соответствующим значением.
Также в классе Money должно быть объект-свойство (property):
money - для записи и считывания значения из атрибута _money.

В связке с классом Money работает еще один класс:

class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)
Он определяет работу арифметических операторов.
В данном примере описан алгоритм сложения двух объектов класса Money (или объектов его дочерних классов).

Обратите внимание, как реализован метод __add__() в этом классе.
Он универсален при работе с любыми объектами класса Money или его дочерних классов.
Здесь атрибут __class__ - это ссылка на класс объекта self. С помощью __class__ можно создавать объекты того же класса, что и self.

Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.

На основе двух классов (Money и MoneyOperators) предполагается создавать классы кошельков разных валют. Например, так:

class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"
И, затем применять их следующим образом (эти строчки в программе писать не нужно):

m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m2  # TypeError
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    # ваш код:
    # здесь объявляйте еще один метод
    def __radd__(self, other):
        if type(other) in (int, float):
            return self.__class__(other + self.money)

    # здесь объявляйте еще один метод
    # Вам необходимо добавить в класс MoneyOperators аналогичную реализацию оператора вычитания.
    # __sub__(self, other) - вычитание (x - y).
    # Пример m = m1 - 5.4
    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)

    def __rsub__(self, other):
        if type(other) in (int, float):
            return self.__class__(other - self.money)


# ваш код:
# здесь объявляйте класс Money
class Money:
    def __init__(self, value):
        if type(value) in (int, float):
            self._money = value
        else:
            raise TypeError('сумма должна быть числом')

    # Также в классе Money должно быть объект-свойство (property):
    # money - для записи и считывания значения из атрибута _money.
    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


# end ваш код
# TEST-TASK___________________________________
from test4_6.test_4_6_9 import test_9

test_9()
# END

# TEST
# m1 = MoneyR(100)
# m2 = MoneyR(2)
# m = m1 + 10
# print(m)  # MoneyR: 11
# m = m1 - 5.4
# m = m1 - m2  # TypeError
# m = 10 - m1  # TypeError
# P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
