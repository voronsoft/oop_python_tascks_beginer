"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Vr4c1LgE91o

Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:

tr = TriangleChecker(a, b, c)
Здесь a, b, c - длины сторон треугольника.

В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
3 - стороны a, b, c образуют треугольник.

Проверку параметров a, b, c проводить именно в таком порядке.

Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:

a, b, c = map(int, input().split())
Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.
Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).

Sample Input:

3 4 5
Sample Output:

3
"""


class TriangleChecker:
    def __init__(self, a1, b2, c3):
        self.a = a1
        self.b = b2
        self.c = c3

    # В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
    # 1 - если хотя бы одна сторона не число (не float или не int) или хотя бы одно число меньше или равно нулю;
    # 2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
    # 3 - стороны a, b, c образуют треугольник.
    def is_triangle(self):
        # если хотя бы одна сторона не число (не float или не int) или хотя бы одно число меньше или равно нулю
        if (type(self.a) in (float, int) and type(self.b) in (float, int) and type(self.c) in (float, int)) and \
                (0 != self.a > 0 != self.b > 0 and 0 < self.c != 0):
            # указанные числа a, b, c не могут являться длинами сторон треугольника
            if (self.a < self.b + self.c) and (self.b < self.c + self.a) and (self.c < self.a + self.b):
                return 3
            else:
                return 2
        else:
            return 1


# прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
a, b, c = map(int, input().split())
# Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c.              
tr = TriangleChecker(a, b, c)
# Вызовите метод is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).
print(tr.is_triangle())

# TEST-TASK___________________________________
assert isinstance(tr, TriangleChecker) and hasattr(TriangleChecker, 'is_triangle')


def is_triangle(a, b, c):
    for x in (a, b, c):
        if type(x) not in (int, float):
            return 1

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a < (b + c) and b < (a + c) and c < (a + b):
        return 3

    return 2


assert tr.is_triangle() == is_triangle(a, b, c), \
    f"неверный возвращаемый код методом is_triangle(a, b, c): {tr.is_triangle()}, а должен {is_triangle(a, b, c)}"

try:
    tr = TriangleChecker('3', 4, 5)
except TypeError:
    assert False, "При передаче нечисловых аргументов команда TriangleChecker(arg1, arg2, arg3) выдает ошибку"

assert tr.is_triangle() == is_triangle('3', 4, 5), \
    f"неверный возвращаемый код методом is_triangle('3', 4, 5) при наличии нечисловых аргументов: {tr.is_triangle()}, а должен {is_triangle('3', 4, 5)}"

tr = TriangleChecker(3.0, 4.0, 5.0)
assert tr.is_triangle() == is_triangle(3.0, 4.0, 5.0), \
    f"неверный возвращаемый код методом is_triangle при вещественных аргументах: {tr.is_triangle()}, а должен {is_triangle(3.0, 4.0, 5.0)}"
