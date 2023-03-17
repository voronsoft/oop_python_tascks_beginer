"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/P0sI_Eb_i0c
Подвиг 5.
Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
wnd = WindowDlg(заголовок окна, ширина, высота)
В каждом объекте класса WindowDlg должны создаваться ПРИВАТНЫЕ локальные атрибуты:
__title - заголовок окна (строка);
__width, __height - ширина и высота окна (числа).
В классе WindowDlg необходимо реализовать метод:
- show() - для отображения окна на экране (выводит в консоль строку в формате:
 "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").

Также в классе WindowDlg необходимо реализовать два объекта-свойства:
- width - для изменения и считывания ширины окна;
- height - для изменения и считывания высоты окна.
При изменении размеров окна необходимо выполнять проверку:
- переданное значение является целым числом в диапазоне [0; 10000].
Если хотя бы один размер изменился (высота или ширина),
то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
При начальной инициализации размеров width, height вызывать метод show() не нужно.
P.S. В программе нужно объявить только класс с требуемой функциональностью.
"""


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title  # __title - заголовок окна (строка);
        self.__width = width  # __width - ширина окна (числа).
        self.__height = height  # __height - высота окна (числа)

    def show(self):
        print(f'{self.__title}: {self.width}, {self.height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if 0 <= value <= 10000 and type(value) == int:
            self.__width = value

            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 0 <= value <= 10000 and type(value) == int:
            self.__height = value

            self.show()


# TEST-TASK___________________________________
wnd = WindowDlg('Окно', 10, 11)
assert '_WindowDlg__title' in wnd.__dict__ and '_WindowDlg__width' in wnd.__dict__ and '_WindowDlg__height' in wnd.__dict__, \
    "Атрибуты в экземпляре класса не совпадают, так же они должны быть защищёнными"

assert wnd._WindowDlg__title == 'Окно' and type(wnd._WindowDlg__title) is str, 'Название должно быть строкой'
assert 'width' in dir(wnd) and 'height' in dir(wnd), 'В классе должны быть методы для обращения к приватным атрибутам'

assert wnd.width == 10, 'Геттер для __width работает неправильно'
wnd.width = 11
assert wnd.width == 11, 'Сеттер для __width работает неправильно'

assert wnd.height == 11, 'Геттер для __height работает неправильно'
wnd.height = 22
assert wnd.height == 22, 'Сеттер для __height работает неправильно'

import io
import sys

output = io.StringIO()
sys.stdout = output
wnd.show()
sys.stdout = sys.__stdout__
assert output.getvalue().strip() == "Окно: 11, 22", 'Неправильный формат вывода в методе show'
print("Правильно ! ")
