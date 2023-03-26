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


# TEST-TASK___________________________________
course = Course("Python ООП")
assert type(course.name) is str, "название курса должно быть строкой"
assert type(course.modules) is list and len(course.modules) == 0, "modules должен быть списком, изначально список пуст"
# add_module(self, module) - добавление нового модуля в конце списка modules;
# remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
assert hasattr(course, 'add_module'), "add_module необъявлен"
assert hasattr(course, 'remove_module'), "remove_module необъявлен"

#
module_1 = Module("Часть первая")
module_2 = Module("Часть вторая")
assert type(module_1.name) is str, "название модуля должно быть строкой"
assert type(module_1.lessons) is list and len(
    module_1.lessons) == 0, "lesson должен быть списком, изначально список пуст"
# add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
# remove_lesson(self, indx) - удаление урока по индексу в списке lessons.
assert hasattr(module_1, "add_lesson"), "add_lesson необъявлен"
assert hasattr(module_1, "remove_lesson"), "remove_lesson необъявлен"

#
les_1 = LessonItem("Урок 1", 7, 1000)
les_2 = LessonItem("Урок 2", 10, 1200)
assert type(les_1.title) is str, "название урока должно быть строкой"
assert type(les_1.practices) is int and les_1.practices > 0, "practices должен быть целым числом больше ноля"
assert type(les_1.duration) is int and les_1.practices > 0, "duration должен быть целым положительным числом"

#
# проверка методов
course.add_module(module_1)
course.add_module(module_2)
assert len(course.modules) == 2 and course.modules[1] == module_2, "некоректно отработал метод add_module"
course.remove_module(0)
assert module_1 not in course.modules and len(course.modules) == 1, "некоректно отработал метод remove_module"
#
module_1.add_lesson(les_1)
module_1.add_lesson(les_2)
assert len(module_1.lessons) == 2 and module_1.lessons[1] == les_2, "некоректно отработал метод add_lesson"
module_1.remove_lesson(0)
assert les_1 not in module_1.lessons and len(module_1.lessons) == 1, "некоректно отработал метод remove_lesson"
#
# проверка методов - LessonItem
# 1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
try:
    les_3 = LessonItem(3, 8, 900)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в title"

try:
    les_3 = LessonItem("Урок 2", 8.0, 900)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в practices"

try:
    les_3 = LessonItem("Урок 2", 8, 900, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в duration"

# 2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
les_4 = LessonItem("Урок 2", 8, 900)
assert hasattr(les_1, "__getattr__"), \
    "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
assert les_4.value_not_atr is False, "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
# 3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
assert hasattr(les_4, "__delattr__"), \
    "возможно вы не продумали запрет на удаление локальных атрибутов - title, practices и duration"
try:
    del les_4.title
    del les_4.practices
    del les_4.duration
except:
    ...
else:
    if any(True if _ not in les_4.__dict__ else False for _ in ["title", "practices", "duration"]):
        print('Ошибка при удалении локальных атрибутов - title, practices и duration')

print("Умница правильный ответ ))")
