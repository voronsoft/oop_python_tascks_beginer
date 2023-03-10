"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/45q8BT03c_U

Подвиг 10 (на повторение).
Необходимо написать программу для представления и управления расписанием телевизионного вещания.
Для этого нужно объявить класс TVProgram, объекты которого создаются командой:
pr = TVProgram(название канала)
где название канала - это строка с названием телеканала.
В каждом объекте класса TVProgram должен формироваться локальный атрибут:
- items - список из телепередач (изначально список пуст).
В самом классе TVProgram должны быть реализованы следующие методы:
- add_telecast(self, tl) - добавление новой телепередачи в список items;
- remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).

Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:
tl = Telecast(порядковый номер, название, длительность)
где порядковый номер - номер телепередачи в сетке вещания (от 1 и далее);
название - наименование телепередачи;
длительность - время телепередачи (в секундах - целое число).
Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:
__id - порядковый номер (целое число);
__name - наименование телепередачи (строка);
__duration - длительность телепередачи в секундах (целое число).

Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):
uid - для записи и считывания из локального атрибута __id;
name - для записи и считывания из локального атрибута __name;
duration - для записи и считывания из локального атрибута __duration.

Пример использования классов (эти строчки в программе писать не нужно):

pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


class TVProgram:
    """Программа для представления и управления расписанием телевизионного вещания"""

    def __init__(self, chenel):
        # канал
        self.chenel = chenel
        # список из телепередач
        self.items = list()

    # add_telecast(self, tl) - добавление новой телепередачи в список items;
    def add_telecast(self, tl):
        """Добавление новой телепередачи в список items"""
        self.items.append(tl)

    # remove_telecast(self, indx) - удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее).
    def remove_telecast(self, indx):
        """Удаление телепередачи по ее порядковому номеру (атрибуту __id, см. далее)"""
        for _i in range(len(self.items)):
            if self.items[_i].uid == indx:
                del self.items[_i]
                break


# Каждая телепередача должна описываться классом Telecast, объекты которого создаются командой:
# tl = Telecast(порядковый номер, название, длительность)
class Telecast:
    """Телепередача"""

    def __init__(self, id, name, duration):
        # Соответственно, в каждом объекте класса Telecast должны формироваться локальные приватные атрибуты:
        # __id - порядковый номер (целое число); (от 1 и далее)
        if id > 0 and type(id) is int:
            self.__id = id

        # __name - наименование телепередачи (строка);
        if type(name) is str:
            self.__name = name

        # __duration - длительность телепередачи в секундах (целое число).
        if type(duration) is int:
            self.__duration = duration

    # Для работы с этими приватными атрибутами в классе Telecast должны быть объявлены соответствующие объекты-свойства (property):
    # uid - для записи и считывания из локального атрибута __id;
    @property
    def uid(self):
        """Gerret property"""
        return self.__id

    @uid.setter
    def uid(self, value):
        """Setter property"""
        self.__id = value

    # name - для записи и считывания из локального атрибута __name;
    @property
    def name(self):
        """Gerret property"""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter property"""
        self.__name = value

    # duration - для записи и считывания из локального атрибута __duration.
    @property
    def duration(self):
        """Gerret property"""
        return self.__duration

    @duration.setter
    def duration(self, value):
        """Setter property"""
        self.__duration = value

# ТЕСТ
# assert hasattr(TVProgram, 'add_telecast') and hasattr(TVProgram, 'remove_telecast'), "в классе TVProgram должны быть методы add_telecast и remove_telecast"
# #
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(3, "Новости", 2000))
# t = Telecast(2, "Интервью с Балакиревым", 20)
# pr.add_telecast(t)
# #
# pr.remove_telecast(3)
# assert len(pr.items) == 2, "неверное число телепередач, возможно, некорректно работает метод remove_telecast"
# assert pr.items[-1] == t, "удалена неверная телепередача (возможно, вы удаляете не по __id, а по порядковому индексу в списке items)"
# #
# assert type(Telecast.uid) == property and type(Telecast.name) == property and type(Telecast.duration) == property, "в классе Telecast должны быть объекты-свойства uid, name и duration"
# #
# for x in pr.items:
#     assert hasattr(x, 'uid') and hasattr(x, 'name') and hasattr(x, 'duration')
# #
# assert pr.items[0].name == "Доброе утро", "объект-свойство name вернуло неверное значение"
# assert pr.items[0].duration == 10000, "объект-свойство duration вернуло неверное значение"
# #
# t = Telecast(1, "Доброе утро", 10000)
# t.uid = 2
# t.name = "hello"
# t.duration = 10
