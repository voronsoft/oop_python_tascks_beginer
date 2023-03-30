"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DEyOq7Gpko4

Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y),
а третий необязательный аргумент - цвет точки (локальное свойство color).
Если цвет не указывается, то он по умолчанию принимает значение black.

Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть,
с увеличением на два для каждой новой точки. Каждый объект следует поместить в список points (по порядку).
Для второго объекта в списке points укажите цвет 'yellow'.

P.S. На экран в программе ничего выводить не нужно.
"""


# ваш код:
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


# чтобы объекты этого класса можно было создавать командами:
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')

# Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть,
# с увеличением на два для каждой новой точки.
# Каждый объект следует поместить в список points (по порядку).
points = []
k = 1
for i in range(0, 1000):
    points.append(Point(k, k))
    k += 2
# Для второго объекта в списке points укажите цвет 'yellow'.
points[1].color = 'yellow'
# end ваш код

# TEST-TASK___________________________________
from test1_5.test_1_5_3 import test_3

test_3(Point, points)
# END
