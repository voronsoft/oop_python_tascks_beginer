"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/jk9AOnvm65k
Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ
Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на следующий и так по цепочке до последнего:
Для этого в программе объявлялись два класса:

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

- Объекты класса StackObj следовало создавать командой:
obj = StackObj(data)
где data - это строка с некоторым содержимым объекта (данными).
При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:
data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

- Класс Stack предполагается использовать следующим образом:
st = Stack() # создание объекта стек-подобной структуры
В каждом объекте класса Stack должен быть локальный публичный атрибут:
top - ссылка на первый объект стека (если стек пуст, то top = None).
В классе Stack следующие методы:
- push(self, obj) - добавление объекта класса StackObj в конец стека;
- pop(self) - извлечение последнего объекта с его удалением из стека;

В классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:
- __getitem__
obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
- __setitem__
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:
raise IndexError('неверный индекс')

Пример использования классов Stack и StackObj (эти строчки в программе не писать):
st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
res = st[3] # исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
"""


# ваш код:
# - Объекты класса StackObj следовало создавать командой:
# obj = StackObj(data)
# где data - это строка с некоторым содержимым объекта (данными).
# При этом каждый объект класса StackObj должен иметь следующие локальные атрибуты:
# data - ссылка на строку с данными, указанными при создании объекта;
# next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

class StackObj:
    """для описания объектов стека"""

    def __init__(self, data):
        self.data = data
        self.next = None


# - Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта стек-подобной структуры
# В каждом объекте класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый объект стека (если стек пуст, то top = None).
# В классе Stack следующие методы:
# - push(self, obj) - добавление объекта класса StackObj в конец стека;
# - pop(self) - извлечение последнего объекта с его удалением из стека;
#
#
# В классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:
# obj_top = st[0] # получение первого объекта
# obj = st[4] # получение 5-го объекта стека
# st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
# Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:
# raise IndexError('неверный индекс')
class Stack:
    """для управления стек-подобной структурой."""

    def __init__(self):
        self.top = None
        self.end_obj = None
        self.lst = list()

    def push(self, obj):
        """Добавление объекта класса StackObj в конец стека"""
        if len(self.lst) == 0:
            self.top = obj
            self.lst.append(obj)
            self.end_obj = self.lst[-1:]
        else:
            self.lst[-1].next = obj
            self.lst.append(obj)
            self.end_obj = obj

    def pop(self):
        """Извлечение последнего объекта с его удалением из стека"""
        if len(self.lst) == 1:
            self.top = None
            self.end_obj = None
            return self.lst.pop()

        else:
            x = self.lst.pop()
            self.lst[-1].next = None
            self.end_obj = self.lst[-1]
            return x

    # obj_top = st[0] # получение объекта
    # Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:
    # raise IndexError('неверный индекс')
    def __getitem__(self, item):
        if type(item) != int or item >= len(self.lst) or item < 0:
            raise IndexError('неверный индекс')

        return self.lst[item]

    # st[2] = StackObj("obj3")  # замена прежнего объекта стека на новый
    # Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:
    # raise IndexError('неверный индекс')
    def __setitem__(self, key, value):
        if type(key) != int or key > len(self.lst) or key < 0:
            raise IndexError('неверный индекс')
        else:
            # next предыдущего объекта меняем на = новый объект(value)
            self.lst[key - 1].next = value
            # меняем ссылку(next) нового объекта(value)
            value.next = self.lst[key].next
            # производим замену объектов в списке lst
            self.lst[key] = value


# end ваш код

# TEST-TASK___________________________________
from test3_8.test_3_8_6 import test_6

test_6(Stack, StackObj)

# END
