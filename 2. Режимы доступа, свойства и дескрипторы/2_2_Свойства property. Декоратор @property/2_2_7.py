"""
Подвиг 7.
Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
В каждом объекте класса RadiusVector2D должны формироваться локальные ПРИВАТНЫЕ атрибуты:
__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два ОБЪЕКТА-СВОЙСТВА:
x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как ПУБЛИЧНЫЕ атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:
- norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D
(квадратическая норма вектора: x*x + y*y).

P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    # Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
    # v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
    # v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
    # v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
    # В каждом объекте класса RadiusVector2D должны формироваться локальные ПРИВАТНЫЕ атрибуты:
    # __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
    #
    # При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
    # - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
    # Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
    # Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как ПУБЛИЧНЫЕ атрибуты класса RadiusVector2D.
    def __init__(self, x=0, y=0):
        # При инициализации локальных атрибутов, необходимо проверять корректность передаваемых значений:
        # - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
        # Как реализовать проверку решайте сами
        if self.verify_coord(x) and self.verify_coord(y):
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0

    # В классе RadiusVector2D необходимо объявить два ОБЪЕКТА-СВОЙСТВА:
    # x - для изменения и считывания локального атрибута __x;
    # y - для изменения и считывания локального атрибута __y.
    @property
    def x(self):
        return self.__x

    # При изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
    # - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
    @x.setter
    def x(self, value):
        if self.verify_coord(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    # При изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
    # - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
    @y.setter
    def y(self, value):
        if self.verify_coord(value):
            self.__y = value

    # необходимо объявить СТАТИЧЕСКИЙ метод:
    # - norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D
    # (квадратическая норма вектора: x*x + y*y).
    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y

    # При изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
    # - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
    @classmethod
    def verify_coord(cls, coord):
        return (type(coord) is int or type(coord) is float) and cls.MIN_COORD <= coord <= cls.MAX_COORD

# Проверка
# v1 = RadiusVector2D()  # радиус-вектор с координатами (0; 0)
# v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
# v3 = RadiusVector2D(1, 2)  # радиус-вектор с координатами (1; 2)
# v3.y = -1000

# проверка тест
# r1 = RadiusVector2D()
# r2 = RadiusVector2D(1)
# r3 = RadiusVector2D(4, 5)
# 
# assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(RadiusVector2D, 'MAX_COORD'), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"
# 
# assert type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property, "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"
# 
# assert r1.x == 0 and r1.y == 0 and r2.x == 1 and r2.y == 0 and r3.x == 4 and r3.y == 5, "свойства x и y возвращают неверные значения"
# 
# assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"
# 
# r4 = RadiusVector2D(4.5, 5.5)
# assert 4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6, "свойства x и y возвращают неверные значения"
# 
# r5 = RadiusVector2D(-102, 2000)
# assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"
# 
# r = RadiusVector2D(10, 20)
# r.x = 'a'
# r.y = (1, 2)
# assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"
