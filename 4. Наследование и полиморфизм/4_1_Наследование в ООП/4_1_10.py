"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Q_zIap6F1Lw
Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
v = Vector(x1, x2, ..., xN)
где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
С объектами этого класса должны выполняться команды:
v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:
raise TypeError('размерности векторов не совпадают')
В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих координат вектора.

На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
v = VectorInt(1, 2, 3, 4)
v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
При операциях сложения и вычитания с объектом класса VectorInt:
v = v1 + v2  # v1 - объект класса VectorInt
v = v1 - v2  # v1 - объект класса VectorInt
должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной.
Иначе, v должен быть объектом класса VectorInt.

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


class Vector:
    def __init__(self, *args):
        self.data = args

    @staticmethod
    def verify_data(data_obj):
        if all(True if type(_) == int else False for _ in data_obj):
            return True
        else:
            return False

    def __add__(self, other):
        """ Сложение объектов"""
        a = self.data
        b = other.data
        if len(a) == len(b):
            # определение списков в объектах
            # если все int  то генерируем объект как VectorInt
            # иначе генерируем как объект Vector
            if self.verify_data(a) and self.verify_data(b):
                return VectorInt(*map(sum, zip(a, b)))
            else:
                return Vector(*map(sum, zip(a, b)))
        else:
            raise TypeError('размерности векторов не совпадают')

    def __sub__(self, other):
        """Вычитание объектов"""
        a = self.data
        b = other.data
        if len(a) == len(b):
            x = tuple(_[0] - _[1] for _ in tuple(zip(a, b)))
            return Vector(*x)
        else:
            raise TypeError('размерности векторов не совпадают')

    def get_coords(self):
        """Возвращает кортеж из текущих координат вектора"""
        return self.data


# На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными координатами:
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты должны быть целыми числами')
# При операциях сложения и вычитания с объектом класса VectorInt:
# v = v1 + v2  # v1 - объект класса VectorInt
# v = v1 - v2  # v1 - объект класса VectorInt
# должен формироваться объект v как объект класса Vector, если хотя бы одна координата является вещественной.
# Иначе, v должен быть объектом класса VectorInt.
class VectorInt(Vector):
    def __init__(self, *args):
        if all(list(map(lambda x: True if type(x) == int else False, args))):
            self.data = args
        else:
            raise ValueError('координаты должны быть целыми числами')


# # TEST
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# #
# assert (v1 + v2).get_coords() == (
#     4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
# assert (v1 - v2).get_coords() == (
#     -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"
# # #
# v = VectorInt(1, 2, 3, 4)
# assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"
# #
# try:
#     v = VectorInt(1, 2, 3.4, 4)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"
# #
# v1 = VectorInt(1, 2, 3, 4)
# v2 = VectorInt(4, 2, 3, 4)
# v3 = Vector(1.0, 2, 3, 4)
# #
# v = v1 + v2
# assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
# v = v1 + v3
# assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
