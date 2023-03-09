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

# TEST-TASK___________________________________
p1 = Point(10, 20)
p2 = Point(12, 5, 'red')
assert isinstance(p1, Point), "p1 не создан"
assert isinstance(p2, Point), "p2 не создан"

assert hasattr(p1, 'x') and hasattr(p1, "y") and hasattr(p1, "color"), "В объекте должно быть 3 атрибута"
assert p1.color == "black", "color по умолчанию должен принимать значение black"
assert len(points) == 1000, "длина points не равна 1000"
assert points[1].color == 'yellow', "ошибка, для второго объекта в списке points укажите цвет 'yellow'"
assert points[10].x - points[11].x == -2, "ошибка, в каждом следующем объекте x и y должны увеличиваться на 2 !!"
print("Правильно !")
