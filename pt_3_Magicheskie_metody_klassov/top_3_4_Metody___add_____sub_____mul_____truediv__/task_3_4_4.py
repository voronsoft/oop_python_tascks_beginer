"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/tkjqkiCSnqM

Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:
lst = [1, 2, 3] + [4.5, -3.6, 0.78]
Но нет реализации оператора - который бы убирал из списка соответствующие значения вычитаемого списка,
как это показано в примере:
lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен сохраняться)
Давайте это поправим и создадим такой функционал.
Для этого нужно объявить класс с именем NewList, объекты которого создаются командами:
lst = NewList() # пустой список
lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями.
Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было выполнять следующие действия:

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
Также в классе NewList необходимо объявить метод:

get_list() - для возвращения результирующего списка объекта класса NewList

Например:

lst = res_2.get_list() # [1, 2, 3]
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""


# ваш код:
class NewList:
    def __init__(self, ls=list()):
        self.lst = ls

    def __sub__(self, other):
        """для вычитания списка от списка по совпадающим цифрам, сохраняем в новом списке то что не совпало"""
        if type(other) is list:
            _answer = []
            a_lst = [i for i in self.lst]
            b_lst = [i for i in other]
            for i in a_lst:
                if str(i) in map(str, b_lst):
                    a_lst[a_lst.index(i)] = None
                    b_lst[b_lst.index(i)] = None
                else:
                    _answer.append(i)
            return NewList(_answer)

        if isinstance(other, NewList):
            _answer = []
            a_lst = [i for i in self.lst]
            b_lst = [i for i in other.lst]
            for i in a_lst:
                if str(i) in list(map(str, b_lst)):
                    a_lst[a_lst.index(i)] = None
                    b_lst[b_lst.index(i)] = None
                else:
                    _answer.append(i)

        return NewList(_answer)

    def __rsub__(self, other):
        if type(other) is list:
            _answer = []
            a_lst = [i for i in other]
            b_lst = [i for i in self.lst]
            for i in a_lst:
                if str(i) in list(map(str, b_lst)):
                    a_lst[a_lst.index(i)] = None
                    b_lst[b_lst.index(i)] = None
                else:
                    _answer.append(i)
            return NewList(_answer)

    def __isub__(self, other):
        self.lst = [i for i in self.lst if i not in other.lst]
        return self

    def get_list(self):
        """для возвращения результирующего списка объекта класса NewList"""
        return self.lst


# end ваш код

# TEST-TASK___________________________________
from test3_4.test_3_4_4 import test_4

test_4(NewList)
# END
