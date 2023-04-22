"""
Подвиг 1. В программе объявлены два класса следующим образом:

class Geom:
    def __init__(self, width, color):
        if type(width) not in (int, float) or type(color) != str or width < 0:
            raise ValueError('неверные параметры фигуры')

        self._width = width
        self._color = color


class Ellipse(Geom):
    def __init__(self, x1, y1, x2, y2, width=1, color='red'):
        super().__init__(width, color)

        if not self._is_valid(x1) or not self._is_valid(y1) or not self._is_valid(x2) or not self._is_valid(y2):
            raise ValueError('неверные координаты фигуры')

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _is_valid(self, x):
        return type(x) in (int, float)
И создается объект класса Ellipse:

try:
    x1, y1, x2, y2, w = map(float, input().split())
    el = Ellipse(x1, y1, x2, y2, w)
except ValueError as e:
    print(e)
Выберите все верные утверждения, связанные с этой программой.

    если бы переменная w ссылалась на строку, то в классе Geom было бы сгенерировано исключение, которое поднялось бы до класса Ellipse и обработано в основной программе в блоке try
    все исключения, формируемые в классе Geom, можно обрабатывать внутри класса Ellipse
при возникновении исключения в классе Geom, его можно обрабатывать только в классе Ellipse, иначе программа завершится с ошибкой
    при вводе положительных числовых значений объект класса Ellipse будет создан успешно
исключения, генерируемые в классе Ellipse можно обрабатывать в базовом классе Geom
"""
