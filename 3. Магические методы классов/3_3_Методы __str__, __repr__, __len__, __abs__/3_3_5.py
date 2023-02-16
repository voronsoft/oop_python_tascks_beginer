"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6-xKuQp9b7Y

Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:

-----------Тут двух-связный список

Здесь создается список из связанных между собой объектов класса ObjList.
Объекты этого класса создаются командой:
obj = ObjList(data)
где data - строка с некоторой информацией.
Также в каждом объекте obj класса ObjList должны создаваться следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()
и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):

linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev
P.S. На экран в программе ничего выводить не нужно.
"""


# Для этого объявите класс LinkedList который будет представлять связный список в целом и иметь набор следующих методов:
class LinkedList:

    # В каждом объекте этого класса должны создаваться локальные публичные атрибуты:
    def __init__(self, head=None, tail=None):
        self.head = head  # head - ссылка на первый объект связного списка (если список пустой, то head = None);
        self.tail = tail  # tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
        self.list_obj = list()

    # - add_obj(self, obj) - добавление нового объекта obj класса ObjList в конец связного списка;
    def add_obj(self, obj):
        if self.tail is None:
            obj.prev = self.tail
            self.tail = obj
            # добавление в список list_obj
            self.list_obj.append(obj)

            if self.head is None:
                self.head = obj

            if self.tail is None:
                self.tail = None
            else:
                self.tail = obj

        else:
            obj.prev = self.tail
            self.tail.next = obj
            # добавление в список list_obj
            self.list_obj.append(obj)
            self.tail = obj

    # - remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу);
    # индекс отсчитывается с нуля.;
    def remove_obj(self, indx):
        # перед тем как удалить объект из списка нужно в предыдущем объекте и в следующем
        # изменить ссылки в переменных next-prev
        # если удаляемый объект первый в списке то у следующего prev=None
        if indx == 0 and len(self.list_obj) > 1:
            self.list_obj[indx + 1].prev = None
            # а head меняется на следующий объект после удаляемого
            self.head = self.list_obj[indx + 1]
            # теперь можно удалять сам объект (ссылки изменены)
            del self.list_obj[indx]

        # если в списке всего 1 объект
        elif indx == 0 and len(self.list_obj) == 1:
            self.list_obj[indx].prev = None
            self.head = None
            self.tail = None
            # теперь можно удалять сам объект (ссылки изменены)
            del self.list_obj[indx]

        # если индекс больше или меньше длинны списка ничего не делаем
        elif indx == 0 and len(self.list_obj) == 0:
            return 'None'

        # если удаляемый объект последний, то у предыдущего объекта меняем переменную next=None
        # так же меняем tail на предыдущий объект от удаляемого (последнего в списке)
        elif indx == len(self.list_obj) - 1:
            self.list_obj[indx - 1].next = None
            # так же меняем tail на предыдущий объект от удаляемого (последнего в списке)
            self.tail = self.list_obj[indx - 1]
            # теперь можно удалять сам объект (ссылки изменены)
            del self.list_obj[indx]

        # если удаляемый объект не первый и не последний в списке, то меняем в соседних объектах ссылки, то:
        # у предыдущего объекта меняем next
        # у следующего объекта меняем prev
        elif (indx not in (0, len(self.list_obj) - 1)) and (indx < len(self.list_obj) - 1):
            # у предыдущего объекта меняем next
            self.list_obj[indx - 1].next = self.list_obj[indx + 1]
            # у следующего объекта меняем prev
            self.list_obj[indx + 1].prev = self.list_obj[indx - 1]
            # теперь можно удалять сам объект (ссылки изменены)
            del self.list_obj[indx]

        elif len(self.list_obj) - 1 > indx > len(self.list_obj) - 1:
            return

    # len(linked_lst) - возвращает число объектов в связном списке;
    def __len__(self):
        """Должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами)"""
        return len(self.list_obj)

    # linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList,
    # расположенного под индексом indx (в связном списке).
    def linked_lst(self, indx):
        if len(self.list_obj) != 0:
            return self.list_obj[indx].data
        else:
            return 'None'

    # assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
    def __call__(self, indx, *args, **kwargs):
        return self.linked_lst(indx)


# Объявите класс ObjList
class ObjList:

    def __init__(self, data):
        # Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
        # __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
        self.next = None
        # __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
        self.prev = None
        self.data = data  # __data - строка с данными.

    @property
    # получение значения приватного свойства __next;
    def next(self):
        return self.__next

    # изменение приватного свойства __next на значение obj;
    @next.setter
    def next(self, obj):
        self.__next = obj

    # получение значения приватного свойства __prev;
    @property
    def prev(self):
        return self.__prev

    # изменение приватного свойства __prev на значение obj;
    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    # получение значения приватного свойства __data.
    @property
    def data(self):
        return self.__data

    # изменение приватного свойства __data на значение data;
    @data.setter
    def data(self, data):
        self.__data = data

# # ТЕСТ
# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
# assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
# assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
# 
# n = 0
# h = ln.head
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__next
#     n += 1
# 
# assert n == 3, "при перемещении по списку через __next не все объекты перебрались"
# 
# n = 0
# h = ln.tail
# while h:
#     assert isinstance(h, ObjList)
#     h = h._ObjList__prev
#     n += 1
# 
# assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
