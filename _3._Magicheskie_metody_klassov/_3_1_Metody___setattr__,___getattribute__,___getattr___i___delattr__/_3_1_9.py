"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2iS8qnEK9to

Подвиг 9. Объявите в программе класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 1000
Каждый объект класса Dimensions должен создаваться командой:
d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
и содержать локальные атрибуты:
__a, __b, __c - габаритные размеры (целые или вещественные числа).
Для работы с этими локальными атрибутами в классе Dimensions следует прописать следующие объекты-свойства:
a, b, c - для изменения и считывания соответствующих локальных атрибутов __a, __b, __c.

При изменении значений __a, __b, __c следует проверять,
что присваиваемое значение число в диапазоне [MIN_DIMENSION; MAX_DIMENSION].
Если это не так, то новое значение не присваивается (игнорируется).
С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions.
При попытке это сделать генерировать исключение:
raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

Пример использования класса (эти строчки в программе писать не нужно):
d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
d.MAX_DIMENSION = 10 # исключение AttributeError
P.S. В программе нужно объявить только класс Dimensions. На экран ничего выводить не нужно.
"""


class Dimensions:
    """Габаритные размеры"""

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        """Инициализатор"""
        self.__a = a
        self.__b = b
        self.__c = c

    # ###############################
    @property
    def a(self):
        """a getter property"""
        return self.__a

    @a.setter
    def a(self, value):
        """a setter property"""
        self.__a = value

    # ------------------------------  
    @property
    def b(self):
        """b getter property"""
        return self.__b

    @b.setter
    def b(self, value):
        """b setter property"""
        self.__b = value

    # ------------------------------
    @property
    def c(self):
        """a getter property"""
        return self.__c

    @c.setter
    def c(self, value):
        """a setter property"""
        self.__c = value

    # ###############################

    # С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION
    # в объектах класса Dimensions.
    # При попытке это сделать генерировать исключение:
    # raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
    def __setattr__(self, key, value):
        """Автоматом вызывается если идет запись или изменение значения в атрибут класса или объекта"""
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")

        # проверка (целые или вещественные числа и в пределах MIN_DIMENSION и MAX_DIMENSION)
        if type(value) in (int, float) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            return object.__setattr__(self, key, value)


# ПРОВЕРКА

# x.a = 1000.5
# print(x.a)
# print(x.MAX_DIMENSION)
# x.MAX_DIMENSION = 9

# TEST-TASK___________________________________
x = Dimensions(10.0, 20, 30)
# проверка что в классе прописаны объекты свойства a-b-c
assert type(Dimensions.a) is property, "a - не является объектом свойством property"
assert type(Dimensions.b) is property, "b - не является объектом свойством property"
assert type(Dimensions.c) is property, "c - не является объектом свойством property"

# проверка что в объекте класса существуют 3 приватных локальных атрибута
assert '_Dimensions__a' in x.__dict__ and '_Dimensions__b' in x.__dict__ and '_Dimensions__c' in x.__dict__, \
    "атрибуты не являются приватными"
# проверка что данные считываются с приватных атрибутов
assert x.a == 10.0 and x.b == 20 and x.c == 30, \
    "при обращении к приватным атрибутам значения не получены проверьте объекты свойства"
# проверка что значения являются целым или вещественным числами
assert type(x.a) in (int, float) and type(x.b) in (int, float) and type(x.c) in (int, float), \
    "значения должны быть или целым числом или вещественным"
# проверка на существование атрибутов минимум-максимум
assert hasattr(x, "MIN_DIMENSION"), "не найден атрибут MIN_DIMENSION"
assert hasattr(x, "MAX_DIMENSION"), "не найден атрибут MAX_DIMENSION"

# проверка что значение в диапазоне
x.a = 9
assert x.a == 10.0, "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.b = -1
assert x.b == 20, "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"
x.c = 1001
assert x.c == 30, "присваиваемое значение должно быть в диапазоне [MIN_DIMENSION; MAX_DIMENSION]"

# проверка
# С помощью магических методов данного занятия запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions.
# При попытке это сделать генерировать исключение:
# raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
try:
    x.MIN_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

try:
    x.MAX_DIMENSION = 0
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError"

assert "MIN_DIMENSION" not in x.__dict__, \
    "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
assert "MAX_DIMENSION" not in x.__dict__, \
    "запретить создание локальных атрибутов MIN_DIMENSION и MAX_DIMENSION в объектах класса Dimensions"
print("Прекрасный ответ !")
