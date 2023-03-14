"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rcj0pB1aB5M

Подвиг 8. Объявите в программе два класса Point и Rectangle. Объекты первого класса должны создаваться командой:
pt = Point(x, y)
где x, y - координаты точки на плоскости (целые или вещественные числа).
При этом в объектах класса Point должны формироваться следующие локальные свойства:
__x, __y - координаты точки на плоскости.
и один геттер:
get_coords() - возвращение кортежа текущих координат __x, __y

Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
r1 = Rectangle(Point(x1, y1), Point(x2, y2))
или
r2 = Rectangle(x1, y1, x2, y2)
Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний.
При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:
__sp - объект класса Point с координатами x1, y1 (верхний левый угол);
__ep - объект класса Point с координатами x2, y2 (нижний правый угол).
Также в классе Rectangle должны быть реализованы следующие методы:
set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
(ссылки на локальные свойства __sp и __ep);
draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)".
Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.

Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
P.S. На экран ничего выводить не нужно.
"""


# pt = Point(x, y)
# где x, y - координаты точки на плоскости (целые или вещественные числа).
# При этом в объектах класса Point должны формироваться следующие локальные свойства:
# __x, __y - координаты точки на плоскости.
# и один геттер:
# get_coords() - возвращение кортежа текущих координат __x, __y
class Point:
    def __init__(self, x, y):
        if type(x) in (int, float) and type(y) in (int, float):
            self.__x = x
            self.__y = y

    # get_coords() - возвращение кортежа текущих координат __x, __y
    def get_coords(self):
        return self.__x, self.__y


# Объекты второго класса Rectangle (прямоугольник) должны создаваться командами:
# r1 = Rectangle(Point(x1, y1), Point(x2, y2))
# или
# r2 = Rectangle(x1, y1, x2, y2)
# Здесь первая координата (x1, y1) - верхний левый угол, а вторая координата (x2, y2) - правый нижний.
# При этом, в объектах класса Rectangle (вне зависимости от способа их создания) должны формироваться следующие локальные свойства:
# __sp - объект класса Point с координатами x1, y1 (верхний левый угол);
# __ep - объект класса Point с координатами x2, y2 (нижний правый угол).
# Также в классе Rectangle должны быть реализованы следующие методы:
# set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
# get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
# (ссылки на локальные свойства __sp и __ep);
# draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)".
# Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
class Rectangle:
    def __init__(self, *args):
        # (Point(1, 1), Point(2, 2))
        if len(args) == 2 and type(args[0]) is Point and type(args[1]) is Point:
            sp, ep = args
            self.__sp = sp
            self.__ep = ep

        # (x1, y1, x2, y2)
        elif len(args) == 4:
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    # set_coords(self, sp, ep) - изменение текущих координат, где sp, ep - объекты класса Point;
    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    # get_coords(self) - возвращение кортежа из объектов класса Point с текущими координатами прямоугольника
    # (ссылки на локальные свойства __sp и __ep);
    def get_coords(self):
        return self.__sp, self.__ep

    # draw(self) - отображение в консоли сообщения: "Прямоугольник с координатами: (x1, y1) (x2, y2)".
    # Здесь x1, y1, x2, y2 - соответствующие числовые значения координат.
    def draw(self):
        print("Прямоугольник с координатами: ", self.__sp.get_coords(), self.__ep.get_coords())


# Создайте объект rect класса Rectangle с координатами (0, 0), (20, 34).
# P.S. На экран ничего выводить не нужно.
rect = Rectangle(0, 0, 20, 34)

# # Проверка
# pt = Point(1, 1)
# pt2 = Point(2, 2)
# # r1 = Rectangle(Point(x1, y1), Point(x2, y2))
# r1 = Rectangle(Point(1, 1), Point(2, 2))
# # или
# # r2 = Rectangle(x1, y1, x2, y2)
# r2 = Rectangle(1, 1, 2, 2)
# # выводим координаты
# print(r2.get_coords())
# 
# # меняем координаты
# # r1.set_coords()
# r2.set_coords(Point(5, 5), Point(6, 6))
# r2.draw()

# TEST-TASK___________________________________
assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and \
       hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), \
    "атрибуты __sp и __ep должны ссылаться на объекты класса Point"
print('Правильно')
