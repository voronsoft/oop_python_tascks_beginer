"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c

Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения.
При записи вещественного числа должна выполняться проверка на вещественный тип данных.
Если проверка не проходит, то генерировать исключение командой:
raise TypeError("Присваивать можно только вещественный тип данных.")

Объявите класс Cell, в котором создается объект value дескриптора FloatValue.
А объекты класса Cell должны создаваться командой:
cell = Cell(начальное значение ячейки)

Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
работать с вещественными числами через объект value (начальное значение должно быть 0.0).
В каждом объекте класса TableSheet должен формироваться локальный атрибут:
cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).
P.S. На экран в программе выводить ничего не нужно.
"""


# Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения.
# Descriptor
class FloatValue:
    # При записи вещественного числа должна выполняться проверка на вещественный тип данных.
    # Если проверка не проходит, то генерировать исключение командой:
    # raise TypeError("Присваивать можно только вещественный тип данных.")
    @classmethod
    def veryfi_float(cls, digit):
        """Проверка передаваемого параметра, что он является float числом"""
        if type(digit) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        """Создает имя переменной"""
        self.name = "_" + name

    def __get__(self, instance, owner):
        """Getter"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Setter"""
        self.veryfi_float(value)  # проверка на вещественное число
        setattr(instance, self.name, value)


# Объявите класс Cell, в котором создается объект value дескриптора FloatValue.
# А объекты класса Cell должны создаваться командой:
# cell = Cell(начальное значение ячейки)
class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


# Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:
# table = TableSheet(N, M)
# Каждая ячейка этой таблицы должна быть представлена объектом класса Cell,
# работать с вещественными числами через объект value (начальное значение должно быть 0.0).
# В каждом объекте класса TableSheet должен формироваться локальный атрибут:
# cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).
class TableSheet:

    def __init__(self, N, M):
        # В каждом объекте класса TableSheet должен формироваться локальный атрибут:
        # cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).
        self.cells = [[Cell() for _i in range(M)] for _k in range(N)]


# ПРОВЕРКА
# Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3.
# Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).
# P.S. На экран в программе выводить ничего не нужно.
table = TableSheet(5, 3)
x = 1.0
for i in range(len(table.cells)):
    for k in table.cells[i]:
        k.value = x
        x += 1.0

# TEST-TASK___________________________________
a = Cell()

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value

try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"
print("Правильно !")
