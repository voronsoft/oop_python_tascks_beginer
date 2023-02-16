"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YJiPpHVguyE

Большой подвиг 9.
Необходимо реализовать связный список (не список языка Python и не хранить объекты в списке Python),
когда объекты класса ObjList связаны с соседними через приватные свойства __next и __prev:

Для этого объявите класс LinkedList, который будет представлять связный список в целом и иметь набор следующих методов:
- add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
- remove_obj(self) - удаление последнего объекта из связного списка;
- get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.
И в каждом объекте этого класса должны создаваться локальные публичные атрибуты:
head - ссылка на первый объект связного списка (если список пустой, то head = None);
tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
__next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
__prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
__data - строка с данными.
Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
- set_next(self, obj) - изменение приватного свойства __next на значение obj;
- set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
- get_next(self) - получение значения приватного свойства __next;
- get_prev(self) - получение значения приватного свойства __prev;
- set_data(self, data) - изменение приватного свойства __data на значение data;
- get_data(self) - получение значения приватного свойства __data.

Создавать объекты класса ObjList предполагается командой:
ob = ObjList("данные 1")

А использовать класс LinkedList следующим образом (пример, эти строчки писать в программе не нужно):
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']

Объявите в программе классы LinkedList и ObjList в соответствии с заданием.
P.S. На экран ничего выводить не нужно.
"""


# Для этого объявите класс LinkedList который будет представлять связный список в целом и иметь набор следующих методов:
class LinkedList:

    # В каждом объекте этого класса должны создаваться локальные публичные атрибуты:
    def __init__(self, head=None, tail=None):
        self.self = list()
        self.head = head  # head - ссылка на первый объект связного списка (если список пустой, то head = None);
        self.tail = tail  # tail - ссылка на последний объект связного списка (если список пустой, то tail = None).

    # - add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
    def add_obj(self, obj):
        if self.tail is None:
            obj.set_prev(self.tail)
            self.tail = obj

            if self.head is None:
                self.head = obj

            if self.tail is None:
                self.tail = None
            else:
                self.tail = obj

        else:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj
            self.tail = obj

    # - remove_obj(self) - удаление последнего объекта из связного списка;
    def remove_obj(self):
        # tail - меняет значение на последний объект
        self.tail = self.tail.get_prev()
        # при удалении, в последнем объекте меняем значение __next на None
        if self.tail is not None:
            self.tail.set_next(None)
        else:
            self.head = None

    # - get_data(self) - получение списка из строк локального свойства __data всех объектов связного списка.
    def get_data(self):

        if self.tail is not None:
            lst_temp = list()
            lst_temp.append(self.tail.get_data())
            temp = self.tail.get_prev()

            while temp is not None:
                lst_temp.append(temp.get_data())
                temp = temp.get_prev()

            lst_temp.reverse()
            return lst_temp
        else:
            return list()


# Объявите класс ObjList
class ObjList:

    def __init__(self, data):
        # Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
        # __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
        self.__next = None
        # __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
        self.__prev = None
        self.__data = data  # __data - строка с данными.

    # Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    # - set_next(self, obj) - изменение приватного свойства __next на значение obj;
    def set_next(self, obj):
        self.__next = obj

    # - set_prev(self, obj) - изменение приватного свойства __prev на значение obj;
    def set_prev(self, obj):
        self.__prev = obj

    # - get_next(self) - получение значения приватного свойства __next;
    def get_next(self):
        return self.__next

    # - get_prev(self) - получение значения приватного свойства __prev;
    def get_prev(self):
        return self.__prev

    # - set_data(self, data) - изменение приватного свойства __data на значение data;
    def set_data(self, data):
        self.__data = data

    # - get_data(self) - получение значения приватного свойства __data.
    def get_data(self):
        return self.__data

# Создавать объекты класса ObjList предполагается командой:
lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
# # lst.remove_obj()
# # lst.remove_obj()
# # lst.remove_obj()
# res = lst.get_data()  # ['данные 1', 'данные 2', 'данные 3']
# Объявите в программе классы LinkedList и ObjList в соответствии с заданием.
# P.S. На экран ничего выводить не нужно.
