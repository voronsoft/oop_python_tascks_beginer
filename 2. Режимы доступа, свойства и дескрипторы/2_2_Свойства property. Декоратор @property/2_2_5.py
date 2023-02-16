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


# Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
# wnd = WindowDlg(заголовок окна, ширина, высота)
class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title  # __title - заголовок окна (строка);
        self.__width = width  # __width - ширина окна (числа).
        self.__height = height  # __height - высота окна (числа)

    # В классе WindowDlg необходимо реализовать метод:
    # - show() - для отображения окна на экране (выводит в консоль строку в формате:
    #  "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").
    def show(self):
        print(f'{self.__title}: {self.width}, {self.height}')

    # Также в классе WindowDlg необходимо реализовать два объекта-свойства:
    # - width - для считывания ширины окна;
    @property
    def width(self):
        return self.__width

    # - width - для изменения ширины окна;
    # При изменении размеров окна необходимо выполнять проверку:
    # - переданное значение является целым числом в диапазоне [0; 10000].
    @width.setter
    def width(self, value):
        if 0 <= value <= 10000 and type(value) == int:
            self.__width = value
            # Если хотя бы один размер изменился (высота или ширина),
            # то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
            # При начальной инициализации размеров width, height вызывать метод show() не нужно.
            self.show()

    # - height - для считывания высоты окна.
    @property
    def height(self):
        return self.__height

    # - height - для изменения высоты окна.
    # При изменении размеров окна необходимо выполнять проверку:
    # - переданное значение является целым числом в диапазоне [0; 10000].
    @height.setter
    def height(self, value):
        if 0 <= value <= 10000 and type(value) == int:
            self.__height = value
            # Если хотя бы один размер изменился (высота или ширина),
            # то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
            # При начальной инициализации размеров width, height вызывать метод show() не нужно.
            self.show()

    # width = property(get_width, set_width)
    # height = property(get_height, set_height)


# Проверка:
wnd = WindowDlg('Окно-1', 10, 11)

# Если хотя бы один размер изменился (высота или ширина),
# то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
# При начальной инициализации размеров width, height вызывать метод show() не нужно.
# wnd.width = 100
# wnd.height = 111
# print(wnd.__dict__)
