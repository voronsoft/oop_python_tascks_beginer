"""Подвиг 4. В программе объявлен дескриптор RealValue и класс Point:
class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y


А, затем, выполняются команды:
pt = Point(1.5, 2.3)
pt.__dict__['x'] = 10.0
print(pt.x)

Какое значение будет выведено в консоль и почему?

Будет выведено 1.5, так как RealValue - это дескриптор, а в инициализаторе идет обращение к дескрипторам x, y. Затем, в строчке pt.x берется дескриптор x и возвращается значение 1.5
Будет выведено 1.5, так как дескриптор RealValue имеет более высокий приоритет перед созданным в строчке pt.__dict__['x'] = 10.0 локальным атрибутом x. Поэтому при обращении pt.x мы, фактически, обращаемся к дескриптору и берем значение 1.5.
Будет выведено 10.0, так как RealValue - это дескриптор не данных и в инициализаторе будут созданы локальные свойства x, y. Затем, в строчке pt.x идет обращение к локальному свойству x со значением 10.
Будет выведено 10.0, так как строчка pt.__dict__['x'] = 10.0 явно создает локальный атрибут x и при последующем обращении к нему через pt.x возвращается эта величина 10.0. Дескрипторы здесь уже не учитываются.
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test2_3.test_2_3_4 import test_4

test_4(temp)
# END
