"""
Имеется следующий класс для считывания информации из входного потока:
import sys
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = ['10', 'Питон - основы мастерства', 512]  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

Которым, затем, можно воспользоваться следующим образом:
sr = StreamReader()
data, result = sr.readlines()

Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
def create(self, fields, lst_values): ...
который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields)
и список строк lst_in (передается в атрибут lst_values)
и формировал бы в объекте класса StreamData локальные свойства
с именами полей из fields и соответствующими значениями из lst_values.

Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False.
Если число полей и число строк не совпадает, то метод create() возвращает False и локальные атрибуты создавать не нужно.

P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.

Пример входной информации (Sample Input):
10
Питон - основы мастерства
512
"""


# ваш код:
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
# который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields)
# и список строк lst_in (передается в атрибут lst_values)
# и формировал бы в объекте класса StreamData локальные свойства
# с именами полей из fields и соответствующими значениями из lst_values.
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            q = tuple(zip(fields, lst_values))
            # # и формировал бы в объекте класса StreamData локальные свойства
            # # с именами полей из fields и соответствующими значениями из lst_values.
            for i in q:
                setattr(self, i[0], i[1])
            # Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False.
            return True
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = ['10', 'Питон - основы мастерства', 512]  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
# end ваш код

# TEST-TASK___________________________________
from test1_4.test_1_4_7 import test_7

test_7(data, result)
# END
