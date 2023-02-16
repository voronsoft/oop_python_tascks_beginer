"""
Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска),
объекты которого создаются командой:

box = Box3D(width, height, depth)
где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)
В каждом объекте класса Box3D должны создаваться публичные атрибуты:
width, height, depth - ширина, высота и глубина соответственно.

С объектами класса Box3D должны выполняться следующие операторы:
box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.

P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.
"""


class Box3D:
    def __init__(self, width, height, depth):
        if type(width) in (int, float) and type(height) in (int, float) and type(depth) in (int, float):
            self.width = width
            self.height = height
            self.depth = depth

    # box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
    def __add__(self, other):
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    # box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
    # box = 3 * box2    # Box3D: width=6, height=12, depth=18
    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)
    
    def __rmul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    # box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
    def __sub__(self, other):
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    # box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    # box = box2 % 3    # Box3D: width=2, height=1, depth=0
    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)
    # При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями локальных атрибутов.


# TEST
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)    
# box = box1 + box2  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2     # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2     # Box3D: width=6, height=12, depth=18
# box = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2    # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3     # Box3D: width=2, height=1, depth=0
