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

for x in g: print(x); for x in g: print(x)
res = next(g); res = next(g)
res = next(g)
for x in g: print(x)
it = iter(g); res = next(g)
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test3_9.test_3_9_3 import test_3

test_3(temp)
# END
