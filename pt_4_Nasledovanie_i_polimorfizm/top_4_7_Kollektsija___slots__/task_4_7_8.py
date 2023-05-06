"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V1fqV9pfARQ
Подвиг 8 (на повторение). В программе объявлен базовый класс Function (функция) следующим образом:
class Function:
    def __init__(self):
        self._amplitude = 1.0     # амплитуда функции
        self._bias = 0.0          # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj
Здесь в инициализаторе создаются два локальных атрибута:

_amplitude - амплитуда функции;
_bias - смещение функции по оси ординат (Oy).

Далее, в методе __call__() берется значение функции в точке x через метод _get_function(),
который должен быть определен в дочерних классах, умножается на амплитуду функции и добавляется ее смещение.
Следующий метод __add__() позволяет менять смещение функции, изменяя атрибут _bias на указанное значение other.

Обратите внимание, в методе __add__() происходит создание нового объекта командой:
obj = self.__class__(self)
Здесь __class__ - это ссылка на класс, к которому относится объект self.
Благодаря этому в базовом классе можно создавать объекты соответствующих дочерних классов.
В момент создания объекта ему передается параметр self как аргумент.
Так будет создаваться копия объекта, т.е. новый объект с тем же набором и значениями локальных атрибутов.

Чтобы обеспечить этот функционал, объявите дочерний класс с именем Linear (линейная функция y = k*x + b),
объекты которого должны создаваться командами:

obj = Linear(k, b)
linear = Linear(obj)  # этот вариант используется в базовом классе в методе __add__()
В первом случае происходит создание объекта линейной функции с параметрами k и b.
Во втором - создание объекта со значениями параметров k и b, взятыми из объекта obj.

В каждом объекте класса Linear должны создаваться локальные атрибуты с именами _k и _b с соответствующими значениями.
В результате будет создан универсальный базовый класс Function для работы с произвольными функциями от одного аргумента.

Применять эти классы можно следующим образом (эти строчки в программе писать не нужно):

f = Linear(1, 0.5)
f2 = f + 10   # изменение смещения (атрибут _bias)
y1 = f(0)     # 0.5
y2 = f2(0)    # 10.5

Пропишите в базовом классе Function еще один магический метод для изменения масштаба (амплитуды) функции, чтобы был доступен оператор умножения:
f = Linear(1, 0.5)
f2 = f * 5    # изменение амплитуды (атрибут _amplitude)
y1 = f(0)     # 0.5
y2 = f2(0)    # 2.5
P.S. В программе следует объявить только классы. На экран выводить ничего не нужно.
"""


class Function:
    """Функция"""

    def __init__(self):
        self._amplitude = 1.0  # амплитуда функции
        self._bias = 0.0  # смещение функции по оси Oy

    def __call__(self, x, *args, **kwargs):
        return self._amplitude * self._get_function(x) + self._bias

    def _get_function(self, x):
        raise NotImplementedError('метод _get_function должен быть переопределен в дочернем классе')

    def __add__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._bias = self._bias + other
        return obj

    # ваш код:
    # здесь добавляйте еще один магический метод для умножения
    def __mul__(self, other):
        if type(other) not in (int, float):
            raise TypeError('смещение должно быть числом')

        obj = self.__class__(self)
        obj._amplitude = self._amplitude * other
        return obj


# ваш код:
# здесь объявляйте класс Linear
class Linear(Function):
    """Линейная функция y = k*x + b"""

    def __init__(self, *args):
        super().__init__()
        if isinstance(args[0], Linear):  # если args объект
            self._k = args[0]._k
            self._b = args[0]._b

        elif type(args[0]) == int:
            self._k, self._b = args

    def _get_function(self, x):
        y = self._k * x + self._b
        return y


# end ваш код
# TEST-TASK___________________________________
from test4_7.test_4_7_8 import test_8

test_8()
# END
