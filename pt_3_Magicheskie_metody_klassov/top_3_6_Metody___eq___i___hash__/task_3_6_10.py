"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0EYz8-qG2iU

Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:
tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные).
В классе Triangle объявите следующие дескрипторы данных:
a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
Иначе, генерируется исключение командой:
raise ValueError("длины сторон треугольника должны быть положительными числами")

Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника.
То есть, должны выполняться условия:
a < b+c; b < a+c; c < a+b
Иначе генерируется исключение командой:
raise ValueError("с указанными длинами нельзя образовать треугольник")

Наконец, с объектами класса Triangle должны выполняться функции:
len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
где p - полу-периметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.
"""
# ваш код:
from math import sqrt


# DESCRIPTOR
class Des:
    @classmethod
    def veryfi_digit(cls, digit):
        """Проверка передаваемого параметра, что он является float числом"""
        if type(digit) not in (int, float) and digit >= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def __set_name__(self, owner, name):
        """Создает имя переменной"""
        self.name = "_" + name

    def __get__(self, instance, owner):
        """Getter"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Setter"""
        self.veryfi_digit(value)  # проверка на (int, float) число
        setattr(instance, self.name, value)


class Triangle:
    a = Des()
    b = Des()
    c = Des()

    def __init__(self, a, b, c):
        if a >= 0 and b >= 0 and c >= 0:
            self.verify_triangl(a, b, c)
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    @classmethod
    def verify_triangl(cls, a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return True
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    # Наконец, с объектами класса Triangle должны выполняться функции:
    # len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
    def __len__(self):
        return sum([self.a, self.b, self.c])

    # tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
    # где p - полу-периметр треугольника).
    def __call__(self, *args, **kwargs):
        p = sum([self.a, self.b, self.c]) / 2
        s = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s


# end ваш код

# TEST-TASK___________________________________
from test3_6.test_3_6_10 import test_10

test_10(Triangle)
# END
