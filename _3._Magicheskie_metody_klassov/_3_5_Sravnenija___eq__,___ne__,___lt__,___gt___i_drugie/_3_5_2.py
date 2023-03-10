"""
Подвиг 2. Пусть в программе объявлен следующий класс:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
И создаются его экземпляры:

v1 = Vector(1, 2)
v2 = Vector(2, 1)
Для каких операций сравнения будет вызван магический метод __eq__() класса Vector?
"""

# v1 <= v2
# v1 >= v2
#     v1 == v2
#     v1 != v2
