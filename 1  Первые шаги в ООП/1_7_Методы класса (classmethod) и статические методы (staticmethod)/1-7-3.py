"""
В программе объявлен следующий класс с одним методом:

class Math:
    @staticmethod
    def sqrt(x):
        return x ** 0.5
И создается объект этого класса:

m = Math()

Выберите все верные варианты вызова метода sqrt:
res = Math.sqrt(4)
res = m.sqrt(2)
res = Math.sqrt(m, 4)
m.Math.sqrt(3)
"""


class Math:
    @staticmethod
    def sqrt(x):
        return x ** 0.5


m = Math()
res = Math.sqrt(4)
res = m.sqrt(2)
# res = Math.sqrt(m, 4)
# m.Math.sqrt(3)