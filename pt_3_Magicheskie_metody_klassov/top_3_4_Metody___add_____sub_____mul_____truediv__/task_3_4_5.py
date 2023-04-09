"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Poea079PSs

Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
остальные игнорировать (если указываются в списке).
Например:
lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть ПУБЛИЧНЫЙ атрибут:
lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками,
прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта
(новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.
"""


# ваш код:
class ListMath:
    def __init__(self, lst=list()):
        self.lst_math = [i for i in lst if type(i) in (int, float)]

    @staticmethod
    def verify(num):
        return True if type(num) in (int, float) else False

    # lst = lst + 76 # сложение каждого числа списка с определенным числом
    def __add__(self, other):
        if self.verify(other):
            return ListMath([i + other for i in self.lst_math])

    # lst = 6.5 + lst # сложение каждого числа списка с определенным числом
    def __radd__(self, other):
        if self.verify(other):
            return ListMath([i + other for i in self.lst_math])

    # lst += 76.7  # сложение каждого числа списка с определенным числом
    def __iadd__(self, other):
        if self.verify(other):
            self.lst_math = [i + other for i in self.lst_math]
            return self

    # lst = lst - 76 # вычитание из каждого числа списка определенного числа
    def __sub__(self, other):
        if self.verify(other):
            return ListMath([i - other for i in self.lst_math])

    # lst = 7.0 - lst # вычитание из числа каждого числа списка
    def __rsub__(self, other):
        if self.verify(other):
            return ListMath([other - i for i in self.lst_math])

    # lst -= 76.3
    def __isub__(self, other):
        if self.verify(other):
            self.lst_math = [i - other for i in self.lst_math]
            return self

    # lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
    # lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
    # lst *= 5.54
    def __mul__(self, other):
        if self.verify(other):
            return ListMath([i * other for i in self.lst_math])

    # lst = 7.0 - lst # вычитание из числа каждого числа списка
    def __rmul__(self, other):
        if self.verify(other):
            return ListMath([other * i for i in self.lst_math])

    # lst -= 76.3
    def __imul__(self, other):
        if self.verify(other):
            self.lst_math = [i * other for i in self.lst_math]
            return self

    # lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
    # lst = 3 / lst # деление числа на каждый элемент списка
    # lst /= 13.0
    def __truediv__(self, other):
        if self.verify(other):
            return ListMath([i / other for i in self.lst_math])

    # lst = 7.0 - lst # вычитание из числа каждого числа списка
    def __rtruediv__(self, other):
        if self.verify(other):
            return ListMath([other / i for i in self.lst_math])

    # lst -= 76.3
    def __itruediv__(self, other):
        if self.verify(other):
            self.lst_math = [i / other for i in self.lst_math]
            return self


# end ваш код

# TEST-TASK___________________________________
from test3_4.test_3_4_5 import test_5

test_5(ListMath)
# END
