"""
Подвиг 7
Используя информацию о модуле abc из предыдущего подвига 6
объявите базовый класс с именем StackInterface со следующими абстрактными методами
def push_back(self, obj) - добавление объекта в конец стека
def pop_back(self) - удаление последнего объекта из стека

На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:
st = Stack()
и в каждом объекте этого класса должен формироваться локальный атрибут
_top - ссылка на первый объект стека (для пустого стека _top = None)
В самом классе Stack переопределить абстрактные методы базового класса
def push_back(self, obj) - добавление объекта в конец стека
def pop_back(self) - удаление последнего объекта из стека

Сами объекты стека должны определяться классом StackObj и создаваться командой
obj = StackObj(data)
где data - информация, хранящаяся в объекте (строка)
В каждом объекте класса StackObj должны автоматически формироваться атрибуты
_data - информация, хранящаяся в объекте (строка)
_next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None)

Пример использования классов (эти строчки в программе писать не нужно)
st = Stack()
st.push_back(StackObj("obj 1"))
obj = StackObj("obj 2")
st.push_back(obj)
del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно
"""

from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):  # добавление объекта в конец стека
        raise NotImplementedError('в дочернем классе не переопределен метод push_back()')

    @abstractmethod
    def pop_back(self):  # удаление последнего объекта из стека
        raise NotImplementedError('в дочернем классе не переопределен метод pop_back()')


# На основе этого класса объявите дочерний класс с именем Stack. Объекты этого класса должны создаваться командой:
# st = Stack()
# и в каждом объекте этого класса должен формироваться локальный атрибут
# _top - ссылка на первый объект стека (для пустого стека _top = None)
# В самом классе Stack переопределить абстрактные методы базового класса
# def push_back(self, obj) - добавление объекта в конец стека
# def pop_back(self) - удаление последнего объекта из стека
class Stack(StackInterface):
    def __init__(self):
        self._top = None
        self.lst = list()

    def push_back(self, obj):  # - добавление объекта в конец стека
        # проверяем пустой ли список
        if len(self.lst) == 0:
            # добавляем объект в список
            self.lst.append(obj)
            # меняем переменную_top
            self._top = obj

        # Если список не пустой то
        elif len(self.lst) != 0:
            # в предпоследнем объекте lst меняем _next на добавленный объект
            self.lst[-1]._next = obj
            # добавляем объект
            self.lst.append(obj)
        elif len(self.lst) == 0:
            return 'None'

    def pop_back(self):  # - удаление последнего объекта из стека
        if len(self.lst) > 1:
            # теперь у пред-последнего объекта меняем ссылку _next  на None
            self.lst[-2]._next = None
            # удаляем последний объект из списка
            return self.lst.pop()

        # если в списке всего 1 объект то
        elif len(self.lst) == 1:
            # _top очищаем (так как объектов более в списке нет)
            self._top = None
            # удаляем последний объект из списка
            return self.lst.pop()


# Сами объекты стека должны определяться классом StackObj и создаваться командой
# obj = StackObj(data)
# где data - информация, хранящаяся в объекте (строка)
# В каждом объекте класса StackObj должны автоматически формироваться атрибуты
# _data - информация, хранящаяся в объекте (строка)
# _next - ссылка на следующий объект стека (если следующий отсутствует, то _next = None)
class StackObj:
    def __init__(self, data):
        self._data = str(data)
        self._next = None

# # TEST
# assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"
# #
# try:
#     a = StackInterface()
#     a.pop_back()
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"
# #
# #
# st = Stack()
# assert st._top is None, "атрибут _top для пустого стека должен быть равен None"
# #
# obj_top = StackObj("obj")
# st.push_back(obj_top)
# #
# assert st._top == obj_top, "неверное значение атрибута _top"
# #
# obj = StackObj("obj")
# st.push_back(obj)
# #
# n = 0
# h = st._top
# while h:
#     assert h._data == "obj", "неверные данные в объектах стека"
#     h = h._next
#     n += 1
# #
# assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"
# #
# del_obj = st.pop_back()
# assert del_obj == obj, "метод pop_back возвратил неверный объект"
# #
# del_obj = st.pop_back()
# assert del_obj == obj_top, "метод pop_back возвратил неверный объект"
# #
# assert st._top is None, "неверное значение атрибута _top"
