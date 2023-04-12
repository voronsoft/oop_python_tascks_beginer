"""
Подвиг 4. Объявите класс Dimensions (габариты) с атрибутами:
MIN_DIMENSION = 10
MAX_DIMENSION = 10000
Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.

Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property) с именами: a, b, c.
Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION].
Если число не попадает, то оно игнорируется и существующее значение не меняется.
С объектами класса Dimensions должны выполняться следующие операторы сравнения:
dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
dim1 > dim2    # True, если объем dim1 больше объема dim2
dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
dim1 < dim2    # True, если объем dim1 меньше объема dim2

Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:
item = ShopItem(name, price, dim)
где name - название товара (строка);
price - цена товара (целое или вещественное число);
dim - габариты товара (объект класса Dimensions).

В каждом объекте класса ShopItem должны создаваться локальные атрибуты:
name - название товара;
price - цена товара;
dim - габариты товара (объект класса Dimensions).

Создайте список с именем lst_shop из четырех товаров со следующими данными:
- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)

Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop,
используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки.
Прежний список lst_shop должен оставаться без изменений.

P.S. На экран в программе ничего выводить не нужно.
"""


# ваш код:
class Dimensions:
    """Габариты"""
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    # d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры
    # Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def verify(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    # ##### property
    # Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property) с именами: a, b, c.
    # Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон [MIN_DIMENSION; MAX_DIMENSION].
    # Если число не попадает, то оно игнорируется и существующее значение не меняется.
    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.verify(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.verify(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.verify(value):
            self.__c = value

    # С объектами класса Dimensions должны выполняться следующие операторы сравнения:
    # dim1 < dim2    # True, если объем dim1 меньше объема dim2 - __lt__(self, other)
    # dim1 > dim2    # True, если объем dim1 больше объема dim2  - __gt__(self, other)
    def __gt__(self, other):
        s = self.a * self.b * self.c
        o = other.a * other.b * other.c
        return s > o

    # dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2 - __ge__(self, other)
    # dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2 - __le__(self, other)
    def __ge__(self, other):
        s = self.a * self.b * self.c
        o = other.a * other.b * other.c
        return s >= o


# Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:
# item = ShopItem(name, price, dim)
# где name - название товара (строка);
# price - цена товара (целое или вещественное число);
# dim - габариты товара (объект класса Dimensions).
class ShopItem:
    """Товар"""

    def __init__(self, name: str, price: (int, float), dim: Dimensions):
        if type(name) is str and type(price) in (int, float) and isinstance(dim, Dimensions):
            self.name = name  # название товара (строка)
            self.price = price  # цена товара (целое или вещественное число)
            self.dim = dim  # габариты товара (объект класса Dimensions)


# Создайте список с именем lst_shop из четырех товаров со следующими данными:
# - кеды; 1024; (40, 30, 120)
# - зонт; 500.24; (10, 20, 50)
# - холодильник; 40000; (2000, 600, 500)
# - табуретка; 2000.99; (500, 200, 200)
lst_shop = [ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
            ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
            ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
            ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)),
            ]
#
# Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop,
# используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки.
# Прежний список lst_shop должен оставаться без изменений.
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)

# end ваш код

# TEST-TASK___________________________________
from test3_5.test_3_5_4 import test_4

test_4(lst_shop, ShopItem, Dimensions, lst_shop_sorted)
# END
