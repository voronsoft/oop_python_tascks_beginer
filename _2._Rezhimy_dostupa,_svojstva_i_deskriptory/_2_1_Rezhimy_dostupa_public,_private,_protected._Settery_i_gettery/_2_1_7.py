"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZX8fVI0KTfE

Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:
line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные свойства:
__x1, __y1 - начальная координата;
__x2, __y2 - конечная координата.

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:
set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
get_coords(self) - для получения кортежа из текущих координат линии.
А также метод:
draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # В самом классе Line должны быть реализованы следующие сеттеры и геттеры:
    # set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    # get_coords(self) - для получения кортежа из текущих координат линии.
    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    # А также метод:
    # draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).
    # def draw(self):
    #     print(self.__x1, self.__y1, self.__x2, self.__y2)
    def draw(self):
        print(*[_ for _ in line.__dict__.values()])


# TEST-TASK___________________________________
line = Line(1, 2, 3, 4)
assert len(line.__dict__) == 4
assert hasattr(Line, "set_coords"), "В классе не определён метод set_coords"
assert hasattr(Line, "get_coords"), "В классе не определён метод get_coords"
assert hasattr(Line, "draw"), "В классе не определён метод draw"

assert '_Line__x1' in line.__dict__ and '_Line__y1' in line.__dict__ and '_Line__x2' in line.__dict__ and \
       '_Line__y2' in line.__dict__, "Ошибка, проверьте имена атрибутов, а так же атрибуты должны быть приватными"

assert type(line.get_coords()) == tuple and \
       len(line.__dict__) == len(line.get_coords()), "Метод get_coords вернул неправильный результат"

# проверка метода draw()
import io
import sys
# Создаю объект StringIO
output = io.StringIO()
# Перенаправляю стандартный вывод в StringIO
sys.stdout = output
# выполняю метод draw() что бы перехватить то что будет выведенно в консоль принтом
line.draw()
# Получаю данные из StringIO и записываю в переменную output_str
output_str = output.getvalue()
# Возвращаю перехват вывода, на стандартный вывод в консоль
sys.stdout = sys.__stdout__
# проверяю что данные в output_str это одна строка
# проверяю что перенос строки в самом конце
# проверяю что '\n' в строке только 1
assert type(output_str) == str and output_str[-1:] == '\n' and output_str.count('\n') == 1, "Ошибка, метод draw работает неверно"
# end draw
print('Правильный ответ !')
