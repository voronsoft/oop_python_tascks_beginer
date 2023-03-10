"""
Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:
line = Line(x1, y1, x2, y2)
где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
Могут быть произвольными числами.
В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.
В классе Line определить магический метод __len__() так, чтобы функция:
bool(line)
возвращала False, если длина линии меньше 1.
P.S. На экран ничего выводить не нужно. Только объявить класс.
"""

from math import sqrt


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.verify(x1, y1, x2, y2)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def verify(x1, y1, x2, y2):
        if not all(map(lambda x: isinstance(x, (int, float)), (x1, y1, x2, y2))):
            raise NameError('Координаты должны быть или int или float')

    # В классе Line определить магический метод __len__() так, чтобы функция:
    # bool(line)
    # возвращала False, если длина линии меньше 1.
    def __len__(self):
        return True if sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) > 1 else False

# TEST
# line = Line(0, 0, 0, 1)
# x = bool(line)
