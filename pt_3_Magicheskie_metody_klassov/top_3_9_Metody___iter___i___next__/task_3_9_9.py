"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/kmmvxZWxaAY
Подвиг 9. В программе необходимо реализовать таблицу TableValues по следующей схеме:
Каждая ячейка таблицы должна быть представлена классом Cell.
Объекты этого класса создаются командой:
cell = Cell(data)
где data - данные в ячейке.
В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением.
Для работы с ним в классе Cell должно быть объект-свойство (property):
data - для записи и считывания информации из атрибута __data.

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:
table = TableValues(rows, cols, type_data)
где rows, cols - число строк и столбцов таблицы;
type_data - тип данных ячейки (int - по умолчанию, float, list, str и т.п.).
Начальные значения в ячейках таблицы равны 0 (целое число).
С объектами класса TableValues должны выполняться следующие команды:
table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col
for row in table: # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
При попытке записать по индексам table[row, col] данные другого типа
(не совпадающего с атрибутом type_data объекта класса TableValues), должно генерироваться исключение командой:
raise TypeError('неверный тип присваиваемых данных')
При работе с индексами row, col, необходимо проверять их корректность.
Если индексы не целое число или они выходят за диапазон размера таблицы, то генерировать исключение командой:
raise IndexError('неверный индекс')
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


# ваш код:
class TableValues:
    """Таблица"""

    def __init__(self, rows=0, cols=0, type_data=int):
        self.rows = rows  # число строк
        self.cols = cols  # число столбцов
        self.type_data = type_data  # тип данных ячейки (int - по умолчанию, float, list, str и т.п.).
        self.lst = [[Ceill(type_data(0)) for _j in range(cols)] for _ in range(rows)]

    # проверка индекса
    def verify_ind(self, val):
        if 0 <= val[0] < self.rows and 0 <= val[1] < self.cols:
            return True
        else:
            raise IndexError('неверный индекс')

    # проверка типа данных
    def verify_data(self, val):
        if type(val) == self.type_data:
            return True
        else:
            raise TypeError('неверный тип присваиваемых данных')

    # С объектами класса TableValues должны выполняться следующие команды:
    # table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
    def __setitem__(self, key, value):
        # проверка
        self.verify_ind(key)
        self.verify_data(value)
        self.lst[key[0]][key[1]].data = value

    # value = table[row, col] # считывание значения из ячейки с индексами row, col
    def __getitem__(self, item):
        self.verify_ind(item)
        return self.lst[item[0]][item[1]].data

    # for row in table:  # перебор по строкам
    #     for value in row: # перебор по столбцам
    #         print(value, end=' ')  # вывод значений ячеек в консоль
    #     print()
    def __iter__(self):
        for rows in self.lst:
            w = [_.data for _ in rows]
            yield iter(w)


# Объекты этого класса создаются командой:
# cell = Cell(data)
# где data - данные в ячейке.
# В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data с соответствующим значением.
# Для работы с ним в классе Cell должно быть объект-свойство (property):
# data - для записи и считывания информации из атрибута __data.
class Ceill:
    """Отдельная ячейка таблицы"""

    def __init__(self, data=None):
        self.__data = data  # данные в ячейке

    # PROPERTY
    @property
    def data(self):
        """getter data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter data"""
        self.__data = value
    # END PROPERTY


# end ваш код
# TEST-TASK___________________________________
from test3_9.test_3_9_9 import test_9

test_9(TableValues)
# END
