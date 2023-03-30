from random import choice, random

"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/bPH4It1_d0c

Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse.
Должна быть возможность создавать объекты каждого класса следующими командами:

g1 = Line(a, b, c, d)
g2 = Rect(a, b, c, d)
g3 = Ellipse(a, b, c, d)
Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов(произвольные числа).
В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
в виде кортежей (a, b) и (c, d) соответственно.

Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
(или Line, или Rect, или Ellipse).
Координаты также генерируются случайным образом (числовые значения). Все объекты сохраните в списке elements.

В списке elements обнулите координаты объектов только для класса Line.

P.S. На экран в программе ничего выводить не нужно.
"""


# ваш код:
# Объявите три класса геометрических фигур: Line, Rect, Ellipse.
# Должна быть возможность создавать объекты каждого класса следующими командами:
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов(произвольные числа).
# В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний правый угол) и ep (нижний левый)
# в виде кортежей (a, b) и (c, d) соответственно.
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно
# (или Line, или Rect, или Ellipse).
# random.choice(sequence) - случайный элемент непустой последовательности.
# random.random - случайное число от 0 до 1
# Координаты также генерируются случайным образом (числовые значения).
# Все объекты сохраните в списке elements.
lst_class = [Line, Rect, Ellipse]
elements = [choice(lst_class)(random(), random(), random(), random()) for i in range(0, 217)]

# В списке elements обнулите координаты объектов только для класса Line.
for i in range(len(elements)):
    if isinstance(elements[i], Line):
        elements[i].sp = (0, 0)
        elements[i].ep = (0, 0)
# end ваш код

# TEST-TASK___________________________________
from test1_5.test_1_5_4 import test_4

test_4(elements, Line, Rect, Ellipse)
# END
