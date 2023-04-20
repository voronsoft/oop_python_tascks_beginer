"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/wLaOyNN8x7E
Значимый подвиг 7.
Вам поручается разработать класс TupleData, элементами которого могут являются только объекты классов: CellInteger, CellFloat и CellString.
Вначале в программе нужно объявить класс CellInteger, CellFloat и CellString, объекты которых создаются командами:
cell_1 = CellInteger(min_value, max_value)
cell_2 = CellFloat(min_value, max_value)
cell_3 = CellString(min_length, max_length)
где min_value, max_value - минимальное и максимальное допустимое значение в ячейке;
min_length, max_length - минимальная и максимальная допустимая длина строки в ячейке.
В каждом объекте этих классов должны формироваться локальные атрибуты с именами
_min_value, _max_value или _min_length, _max_length и соответствующими значениями.

Запись и считывание текущего значения в ячейке должно выполняться через объект-свойство (property) с именем:
value - для записи и считывания значения в ячейке (изначально возвращает значение None).
Если в момент записи новое значение не соответствует диапазону [min_value; max_value] или [min_length; max_length],
то генерируется исключения командами:
raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger
raise CellFloatException('значение выходит за допустимый диапазон')    # для объектов класса CellFloat
raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString
Все три класса исключений должны быть унаследованы от одного общего класса: CellException

Далее, объявите класс TupleData, объекты которого создаются командой:
ld = TupleData(cell_1, ..., cell_N)
где cell_1, ..., cell_N - объекты классов CellInteger, CellFloat и CellString (в любом порядке и любом количестве).

Обращение к отдельной ячейке должно выполняться с помощью оператора:
value = ld[index] # считывание значения из ячейке с индексом index
ld[index] = value # запись нового значения в ячейку с индексом index
Индекс index отсчитывается с нуля (для первой ячейки) и является целым числом.
Если значение index выходит за диапазон [0; число ячеек-1], то генерировать исключение IndexError.

Также с объектами класса TupleData должны выполняться следующие функции и операторы:
res = len(ld) # возвращает общее число элементов (ячеек) в объекте ld
for d in ld:  # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    print(d)

Все эти классы в программе можно использовать следующим образом:
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
P.S. Данная программа должна быть выполнена штатно, без ошибок. На экран отображать ничего не нужно.
"""


# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception):
    pass


class CellIntegerException(CellException):
    pass


class CellFloatException(CellException):
    pass


class CellStringException(CellException):
    pass


class CellInteger:
    def __init__(self, min_value, max_value):
        self._min_value = min_value  # минимальное  допустимое значение в ячейке
        self._max_value = max_value  # максимальное допустимое значение в ячейке
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, vol):
        if self._min_value <= vol <= self._max_value:
            self.__value = vol
        else:
            raise CellIntegerException('значение выходит за допустимый диапазон')  # для объектов класса CellInteger


class CellFloat:
    def __init__(self, min_value, max_value):
        self._min_value = min_value  # минимальное допустимое значение в ячейке
        self._max_value = max_value  # максимальное допустимое значение в ячейке
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, vol):
        if self._min_value <= vol <= self._max_value:
            self.__value = vol
        else:
            raise CellFloatException('значение выходит за допустимый диапазон')  # для объектов класса CellFloat


class CellString:
    def __init__(self, min_length, max_length):
        self._min_length = min_length  # минимальная допустимая длина строки в ячейке
        self._max_length = max_length  # максимальная допустимая длина строки в ячейке
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, vol):
        if self._min_length <= len(vol) <= self._max_length:
            self.__value = vol
        else:
            raise CellStringException('длина строки выходит за допустимый диапазон')  # для объектов класса CellString


# здесь объявляйте класс TupleData
class TupleData:
    def __init__(self, *args):
        self.lst = list(args)

    def __getitem__(self, item):
        if type(item) is int and 0 <= item < len(self.lst):
            return self.lst[item].value()
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if type(key) is int and 0 <= key < len(self.lst):
            self.lst[key].value = value
        else:
            raise IndexError

    # возвращает общее число элементов (ячеек) в объекте ld
    def __len__(self):
        return len(self.lst)

    # перебирает значения ячеек объекта ld (значения, а не объекты ячеек)
    def __iter__(self):
        for _ in self.lst:
            yield _.value


# эти строчки в программе не менять!
ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")

#
#
#
#
# # TEST
# t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))
# 
# d = (1, 0, 'sergey')
# t[0] = d[0]
# t[1] = d[1]
# t[2] = d[2]
# for i, x in enumerate(t):
#     assert x == d[i], "объект класса TupleData хранит неверную информацию"
# 
# assert len(t) == 3, "неверное число элементов в объекте класса TupleData"
# 
# 
# cell = CellFloat(-5, 5)
# try:
#     cell.value = -6.0
# except CellFloatException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellFloatException"
# 
# 
# cell = CellInteger(-1, 7)
# try:
#     cell.value = 8
# except CellIntegerException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellIntegerException"
# 
# 
# cell = CellString(5, 7)
# try:
#     cell.value = "hello world"
# except CellStringException:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение CellStringException"
# 
# assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException, CellException) and issubclass(CellStringException, CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
