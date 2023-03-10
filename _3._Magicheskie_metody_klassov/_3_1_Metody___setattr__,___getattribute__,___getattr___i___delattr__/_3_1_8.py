"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg

Подвиг 8.
Объявите класс Circle (окружность), объекты которого должны создаваться командой:
circle = Circle(x, y, radius)
x, y - координаты центра окружности;
radius - радиус окружности
- В каждом объекте класса Circle должны формироваться локальные ПРИВАТНЫЕ атрибуты:
__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).
Для доступа к этим приватным атрибутам в классе Circle следует объявить ОБЪЕКТЫ-СВОЙСТВА (property):
x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.
- При изменении значений приватных атрибутов через объекты-свойства нужно проверять,
что присваиваемые значения - числа (целые или вещественные).
Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля).
Сделать все эти проверки нужно через магические методы.
При некорректных переданных числовых значениях, прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).
Если присваиваемое значение не числовое, то генерировать исключение командой:
raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):
circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
P.S. На экран ничего выводить не нужно.
"""


class Circle:
    # - В каждом объекте класса Circle должны формироваться локальные ПРИВАТНЫЕ атрибуты:
    # __x, __y - координаты центра окружности (вещественные или целые числа);
    # __radius - радиус окружности (вещественное или целое положительное число).
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля).
        if type(value) != str:
            return object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    # При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.
    def __getattr__(self, item):
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float):
            self.__x = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float):
            self.__y = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if type(value) in (int, float) and value > 0:
            self.__radius = value
        elif type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")

# # ПРОВЕРКА
# # Пример использования класса (эти строчки в программе писать не нужно):
# circle = Circle(10.5, 7.5, 22)
# circle.x = -100
# circle.y = 20
# circle.radius = 100
# circle.radius = -10  # Прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name  # False, т.к. атрибут name не существует
# # P.S. На экран ничего выводить не нужно.
# 
# 
# 
# # ТЕСТ
# assert type(Circle.x) == property and type(Circle.y) == property and\
#        type(Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"
# 
# try:
#     cr = Circle(20, '7', 22)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"
# 
# cr = Circle(20, 7, 22)
# assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"
# 
# cr.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"
# 
# x, y = cr.x, cr.y
# assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
# assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"
# 
# try:
#     cr.x = '20'
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError"
# 
# cr.y = 7.8
# cr.radius = 10.6
