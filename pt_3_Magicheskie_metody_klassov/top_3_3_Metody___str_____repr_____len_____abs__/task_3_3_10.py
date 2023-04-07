"""
Подвиг 10 (на повторение).
Объявите класс PolyLine (полилиния) для представления линии из последовательности прямолинейных сегментов.
Объекты этого класса должны создаваться командой:
poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3,
... - последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.
Например:
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))

В классе PolyLine должны быть объявлены следующие методы:
add_coord(x, y) - добавление новой координаты (в конец);
remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
get_coords() - получение списка координат (в виде списка из кортежей).

P.S. На экран ничего выводить не нужно, только объявить класс.
"""


# ваш код:

class PolyLine:
    def __init__(self, *args):
        self.lst_coords = list(args)
        self.start_coord = self.lst_coords[0]

    # add_coord(x, y) - добавление новой координаты (в конец);
    def add_coord(self, *args):
        self.lst_coords.append(args)

    # remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
    def remove_coord(self, indx):
        if indx == 0:
            self.start_coord = self.lst_coords[1]
        del self.lst_coords[indx]

    # get_coords() - получение списка координат (в виде списка из кортежей).
    def get_coords(self):
        return self.lst_coords


# end ваш код

# TEST-TASK___________________________________
from test3_3.test_3_3_10 import test_10

test_10(PolyLine)
# END
