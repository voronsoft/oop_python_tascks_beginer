"""
Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:

rect = Rect(x, y, width, height)
где x, y - координата верхнего левого угла (числа: целые или вещественные);
width, height - ширина и высота прямоугольника (числа: целые или вещественные).

В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны.
Например:
r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
P.S. На экран ничего выводить не нужно, только объявить класс.
"""


class Rect:
    def __init__(self, x, y, width, height):
        if type(x) in (int, float) and type(y) in (int, float) and type(width) in (int, float) and type(height) in (
                int, float):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash((self.height, self.width))

# # TEST
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
# 
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# x = r1 == r2