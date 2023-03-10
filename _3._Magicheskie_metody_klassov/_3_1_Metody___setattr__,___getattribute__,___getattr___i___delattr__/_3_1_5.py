"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7b8d5zqiiAM

Подвиг 5. Необходимо создать программу для обучающего курса. Для этого объявляются три класса:

Course - класс, отвечающий за управление курсом в целом;
Наконец, объекты класса Course создаются командой:
course = Course(название курса)
И содержат следующие локальные атрибуты:
- name - название курса (строка);
- modules - список модулей в курсе (изначально список пуст).
Также в классе Course должны присутствовать следующие методы:
- add_module(self, module) - добавление нового модуля в конце списка modules;
- remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.


Module - класс, описывающий один модуль (раздел) курса;
Объекты класса Module должны создаваться командой:
module = Module(название модуля)
Каждый объект класса Module должен содержать локальные атрибуты:
name - название модуля;
lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).
Также в классе Module должны быть реализованы методы:
- add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
- remove_lesson(self, indx) - удаление урока по индексу в списке lessons.

LessonItem - класс одного занятия (урока).
Объекты класса LessonItem должны создаваться командой:
lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
Соответственно, в каждом объекте класса LessonItem должны создаваться локальные атрибуты:
title - название урока (строка);
practices - число практических занятий (целое положительное число);
duration - общая длительность урока (целое положительное число).
Необходимо с помощью магических методов реализовать следующую логику взаимодействия с объектами класса LessonItem:
1. Проверять тип присваиваемых данных локальным атрибутам.
Если типы не соответствуют требованиям, то генерировать исключение командой:
raise TypeError("Неверный тип присваиваемых данных.")
2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.




Пример использования классов (в программе эти строчки не писать):
course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
P.S. На экран ничего выводить не нужно.
"""


# Course - класс, отвечающий за управление курсом в целом;
# Наконец, объекты класса Course создаются командой:
# course = Course(название курса)
class Course:
    """Course - класс, отвечающий за управление курсом в целом"""

    # И содержат следующие локальные атрибуты:
    def __init__(self, name):
        """Инициализатор объектов Course"""
        self.name = str(name)  # - name - название курса (строка);
        self.modules = list()  # - modules - список модулей в курсе (изначально список пуст).

    # Также в классе Course должны присутствовать следующие методы:
    def add_module(self, module):
        """Добавление нового модуля в конце списка modules"""
        self.modules.append(module)

    def remove_module(self, indx):
        """Удаление модуля из списка modules по индексу в этом списке"""
        del self.modules[indx]


# Module - класс, описывающий один модуль (раздел) курса;
# Объекты класса Module должны создаваться командой:
# module = Module(название модуля)
class Module:
    """Module - класс, описывающий один модуль (раздел) курса"""

    # Каждый объект класса Module должен содержать локальные атрибуты:
    def __init__(self, name):
        """Инициализатор объектов Module"""
        self.name = str(name)  # name - название модуля;
        self.lessons = list()  # lessons - список из уроков (объектов класса LessonItem), входящих в модуль (изначально список пуст).

    # Также в классе Module должны быть реализованы методы:
    def add_lesson(self, lesson):
        """Добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem)"""
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        """Удаление урока по индексу в списке lessons"""
        del self.lessons[indx]


# LessonItem - класс одного занятия (урока).
# Объекты класса LessonItem должны создаваться командой:
# lesson = LessonItem(название урока, число практических занятий, общая длительность урока)
class LessonItem:
    """LessonItem - класс одного занятия (урока)"""

    # Соответственно, в каждом объекте класса LessonItem должны создаваться локальные атрибуты:
    def __init__(self, title, practices, duration):
        self.title = title  # title - название урока (строка);
        self.practices = practices  # practices - число практических занятий (целое положительное число);
        self.duration = duration  # duration - общая длительность урока (целое положительное число).

    # Необходимо с помощью магических методов реализовать следующую логику взаимодействия с объектами класса LessonItem:
    # 1. Проверять тип присваиваемых данных локальным атрибутам.
    # Если типы не соответствуют требованиям, то генерировать исключение командой:
    # raise TypeError("Неверный тип присваиваемых данных.")
    def __setattr__(self, key, value):
        if key == 'title' and type(value) is str:
            return object.__setattr__(self, key, value)

        elif key == "practices" and type(value) is int and value >= 0:
            return object.__setattr__(self, key, value)

        elif key == "duration" and type(value) is int and value >= 0:
            return object.__setattr__(self, key, value)

        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    # 2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
    def __getattr__(self, item):
        return False

    # 3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
    def __delattr__(self, item):
        if item not in ('title', 'practices', 'duration'):
            return object.__delattr__(self, item)

# ПРОВЕРКА
# Пример использования классов (в программе эти строчки не писать):
# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# 
# course.remove_module(0)
# x = LessonItem('fghfgh', 7, 1000)
# # P.S. На экран ничего выводить не нужно.
# 
# del x.title
# del x.practices
# del x.duration
