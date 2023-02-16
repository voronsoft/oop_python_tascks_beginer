"""
Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)
где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:
Если число координат (размерность) векторов v1 и v2 не совпадает,
то при операторах +, -, * должно генерироваться исключение командой:
raise ArithmeticError('размерности векторов не совпадают')

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10
v1 += v2
v2 -= v1

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

P.S. В программе на экран выводить ничего не нужно, только объявить класс.
"""


class Vector:
    def __init__(self, *args):
        if all(True if type(i) in (int, float) else False for i in args):
            self.coords = args
        else:
            raise AttributeError('Координаты должны быть или (int, float)')

    # С каждым объектом класса Vector должны выполняться операторы:
    # Если число координат (размерность) векторов v1 и v2 не совпадает,
    # то при операторах +, -, * должно генерироваться исключение командой:
    # raise ArithmeticError('размерности векторов не совпадают')
    #
    # При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
    # v1 + v2 # суммирование соответствующих координат векторов
    def __add__(self, other):
        if len(self) == len(other):
            ans = map(sum, zip(self.coords, other.coords))
            return Vector(*ans)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    # v1 - v2 # вычитание соответствующих координат векторов
    def __sub__(self, other):
        if len(self) == len(other):
            ans = map(lambda x: x[0] - x[1], zip(self.coords, other.coords))
            return Vector(*ans)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    # v1 * v2 # умножение соответствующих координат векторов
    def __mul__(self, other):
        if len(self) == len(other):
            ans = map(lambda x: x[0] * x[1], zip(self.coords, other.coords))
            return Vector(*ans)
        else:
            raise ArithmeticError('размерности векторов не совпадают')

    # При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
    # v1 += 10 # прибавление ко всем координатам вектора числа 10
    # v1 += v2
    def __iadd__(self, other):
        if type(other) in (int, float):
            ans = map(sum, zip(self.coords, tuple(other for i in range(len(self.coords)))))
            self.coords = tuple(ans)
            return self

        elif isinstance(other, Vector):
            ans = map(sum, zip(self.coords, other.coords))
            self.coords = tuple(ans)
            return self

    # При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
    # v1 -= 10 # вычитание из всех координат вектора числа 10
    # v2 -= v1
    def __isub__(self, other):
        if type(other) in (int, float):
            ans = map(lambda x: x[0] - x[1], zip(self.coords, tuple(other for i in range(len(self.coords)))))
            self.coords = tuple(ans)
            return self

        elif isinstance(other, Vector):
            ans = map(lambda x: x[0] - x[1], zip(self.coords, other.coords))
            self.coords = tuple(ans)
            return self

    # v1 == v2 # True, если соответствующие координаты векторов равны
    # v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
    # def __ne__(self, other):
    def __eq__(self, other):
        ans = all(map(lambda x: x[0] == x[1], zip(self.coords, other.coords)))
        return ans

    def __len__(self):
        return len(self.coords)

# TEST
# v1 = Vector(1, 1, 1, 1)
# v2 = Vector(1, 2, 3, 4)
# v3 = v1 + v2
# v4 = v1 - v2
# v5 = v1 * v2
# v1 += 10
# v1 += v5
# v1 -= v5
# v1 -= 10
# 
# v1 = Vector(1, 1, 1, 1)
# ans = v1 == v1  # True
# ans1 = v1 != v2  # True
