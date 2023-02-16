"""
Подвиг 3. Пусть в программе объявлен класс для реализации геометрической прогрессии:

class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration
И создается объект этого класса командой:

g = GeomRange(1, 1.2, 2)
Отметьте все строчки, которые будут выполнены без ошибок.
"""


class GeomRange:
    def __init__(self, start, step, stop):
        self.start = start
        self.step = step
        self.stop = stop
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration


g = GeomRange(1, 1.2, 2)


# for x in g: print(x)
#
# it = iter(g); res = next(g)
#
res = next(g)
#
# for x in g: print(x); for x in g: print(x)
#
res = next(g); res = next(g)