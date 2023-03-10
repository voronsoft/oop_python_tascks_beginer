"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/o66Is1ab4ho
Подвиг 8.
Объявите класс с именем Rect (прямоугольник), объекты которого создаются командой:
r = Rect(x, y, width, height)
где x, y - координаты верхнего левого угла (любые числа-(int, float));
width - ширина, (положительные числа) прямоугольника
height - высота (положительные числа) прямоугольника
Ось абсцисс (Ox) направлена вправо, ось ординат (Oy) направлена вниз.

В каждом объекте класса Rect должны формироваться локальные атрибуты с именами: _x, _y, _width, _height и соответствующими значениями.
Если переданные аргументы x, y (не числа) и width, height не положительные числа, то генерировать исключение командой:
raise ValueError('некорректные координаты и параметры прямоугольника')
В классе Rect реализовать метод:
def is_collision(self, rect): ...
который проверяет пересечение текущего прямоугольника с другим (с объектом rect).
Если прямоугольники пересекаются, то должно генерироваться исключение командой:
raise TypeError('прямоугольники пересекаются')

Сформировать в программе несколько объектов класса Rect со следующими значениями:
0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1

Сохранить их в списке lst_rect. На основе списка lst_rect сформировать еще один список lst_not_collision,
в котором должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.

P.S. В программе требуется объявить только класс и списки. На экран выводить ничего не нужно.

Подсказка. Для определения пересечения двух прямоугольников, у которых стороны параллельны осям координат
(как в этом подвиге) достаточно проверить, что верхняя грань первого прямоугольника находится ниже нижней грани второго,
или нижняя грань первого прямоугольника выше верхней грани второго. И то же самое для вертикальных граней.
"""


class Rect:
    def __init__(self, x, y, width, height):
        self.verify(x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    # проверка
    # Если переданные аргументы x, y (не числа) и width, height не положительные числа, то генерировать исключение командой:
    # raise ValueError('некорректные координаты и параметры прямоугольника')
    def verify(self, x, y, width, height):
        if all([lambda _: True if _ in (int, float) else False for _ in (x, y, width, height)]) and \
                all(True if _ > 0 else False for _ in (width, height)):
            return True
        else:
            raise ValueError('некорректные координаты и параметры прямоугольника')

    def is_collision(self, rect):
        if not isinstance(rect, Rect):
            raise TypeError("аргумент метода is_collision должен быть объект класса Rect")

        if not (self._x + self._width < rect._x or
                rect._x + rect._width < self._x or
                self._y + self._height < rect._y or
                rect._y + rect._height < self._y):
            raise TypeError('прямоугольники пересекаются')


def is_collision(r1, r2):
    try:
        r1.is_collision(r2)
    except TypeError:
        return True
    return False


# Сформировать в программе несколько объектов класса Rect со следующими значениями:
lst_rect = [Rect(0, 0, 5, 3), Rect(6, 0, 3, 5), Rect(3, 2, 4, 4), Rect(0, 8, 8, 1)]
# На основе списка lst_rect сформировать еще один список lst_not_collision,
# в котором должны быть объекты rect не пересекающиеся ни с какими другими объектами в списке lst_rect.
lst_not_collision = [lst_rect[i] for i in range(len(lst_rect))
                     if not any(is_collision(lst_rect[i], lst_rect[j]) for j in range(len(lst_rect)) if i != j)]

# # print(lst_not_collision)
# # TEST
# r = Rect(1, 2, 10, 20)
# assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"
# #
# r2 = Rect(1.0, 2, 10.5, 20)
# #
# try:
#     r2 = Rect(0, 2, 0, 20)
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"
# #
# #
# assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
# assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"
#
#
# #
# def not_collision(rect):
#     for x in lst_rect:
#         try:
#             if x != rect:
#                 rect.is_collision(x)
#         except TypeError:
#             return False
#     return True
#
#
# #
# f = list(filter(not_collision, lst_rect))
# assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"
# #
# r = Rect(3, 2, 2, 5)
# rr = Rect(1, 4, 6, 2)
# #
# try:
#     r.is_collision(rr)
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
