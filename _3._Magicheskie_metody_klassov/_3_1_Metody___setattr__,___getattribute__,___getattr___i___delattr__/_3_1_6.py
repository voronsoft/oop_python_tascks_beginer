"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/oyeub94DCKw

Подвиг 6. Вам необходимо написать программу описания музеев.
Для этого нужно объявить класс Museum, объекты которого формируются командой:
mus = Museum(название музея)
В объектах этого класса должны формироваться следующие локальные атрибуты:
- name - название музея (строка);
- exhibits - список экспонатов (изначально пустой список).
Сам класс Museum должен иметь методы:
- add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
- remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
- get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
Метод должен возвращать значение атрибута descr указанного экспоната в формате:
"Описание экспоната {name}: {descr}"
Например:
"Описание экспоната Девятый вал: Айвазовский написал супер картину."

Экспонаты представляются объектами своих классов.
Для примера объявите в программе следующие классы экспонатов:
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
- class Picture: - для картин;
p = Picture(название, художник, описание)
# локальные атрибуты:
name - название;
author - художник;
descr - описание

- class Mummies: - для мумий;
m = Mummies(имя мумии, место находки, описание)
# локальные атрибуты:
name - имя мумии;
location - место находки;
descr - описание

- class Papyri: - для папирусов.
pr = Papyri(название папируса, датировка, описание)
# локальные атрибуты:
name - название папируса;
date - датировка (строка);
descr - описание

Пример использования классов (в программе эти строчки писать не нужно - только для примера):
mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
"""


# Объявить класс Museum, объекты которого формируются командой:
# mus = Museum(название музея)
class Museum:
    """Museum(название музея)"""

    # В объектах этого класса должны формироваться следующие локальные атрибуты:
    def __init__(self, name):
        """Инициализатор объектов Museum"""
        self.name = name  # - name - название музея (строка);
        self.exhibits = list()  # - exhibits - список экспонатов (изначально пустой список).

    # Сам класс Museum должен иметь методы:
    def add_exhibit(self, obj):
        """Добавление нового экспоната в музей (в конец списка exhibits);"""
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        """Удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)"""
        for ind, value in enumerate(self.exhibits):
            if obj == value:
                del self.exhibits[ind]

    # Метод должен возвращать значение атрибута descr указанного экспоната в формате:
    # "Описание экспоната {name}: {descr}"
    # Например: "Описание экспоната Девятый вал: Айвазовский написал супер картину."
    def get_info_exhibit(self, indx):
        """Получение информации об экспонате (строка) по индексу списка (нумерация с нуля)."""
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"

    def __setattr__(self, key, value):
        if key == 'name' and type(value) is str:
            return object.__setattr__(self, key, value)

        return object.__setattr__(self, key, value)


# Экспонаты представляются объектами своих классов.
# Для примера объявите в программе следующие классы экспонатов:
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# p = Picture(название, художник, описание)
class Picture:
    """для картин"""

    def __init__(self, name, author, descr):
        self.name = name  # name - название;
        self.author = author  # author - художник;
        self.descr = descr  # descr - описание


# m = Mummies(имя мумии, место находки, описание)
class Mummies:
    """для мумий"""

    def __init__(self, name, location, descr):
        self.name = name  # name - имя мумии;
        self.location = location  # location - место находки;
        self.descr = descr  # descr - описание


# pr = Papyri(название папируса, датировка, описание)
class Papyri:
    """для папирусов"""

    def __init__(self, name, date, descr):
        self.name = name  # name - название папируса;
        self.date = date  # date - датировка (строка);
        self.descr = descr  # descr - описание

    def __setattr__(self, key, value):
        if key == 'date' and type(value) is str:
            return object.__setattr__(self, key, value)

        return object.__setattr__(self, key, value)


# ПРОВЕРКА
# Пример использования классов (в программе эти строчки писать не нужно - только для примера):
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)
#
# mus.remove_exhibit(p)

# TEST-TASK___________________________________
mus = Museum("Эрмитаж")
assert type(mus.name) is str, "название должно быть строкой"
assert mus.exhibits == [], "exhibits должен быть списком"
assert hasattr(mus, "add_exhibit"), "метод не объявлен"
assert hasattr(mus, "remove_exhibit"), "метод не объявлен"
assert hasattr(mus, "get_info_exhibit"), "метод не объявлен"

pic = Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
              "Вдохновляющая, устрашающая, волнующая картина")
assert 'name' in pic.__dict__.keys() and 'descr' in pic.__dict__.keys() and 'author' in pic.__dict__.keys(), "ошибка в локальных атрибутах"

mum = Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации")
assert 'name' in mum.__dict__.keys() and 'location' in mum.__dict__.keys() and 'descr' in mum.__dict__.keys(), "ошибка в локальных атрибутах"

p = Papyri("Ученья для, не злата ради",
           "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
assert 'name' in p.__dict__.keys() and 'date' in p.__dict__.keys() and 'descr' in p.__dict__.keys(), "ошибка в локальных атрибутах"
assert type(p.date) is str, "название должно быть строкой"

# проверка методов
# add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
# remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
# get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
mus.add_exhibit(pic)
assert mus.exhibits[0] == pic and len(mus.exhibits) == 1, "некорректно отработал метод add_exhibit"

mus.remove_exhibit(pic)
assert len(mus.exhibits) == 0 and pic not in mus.exhibits, "некорректно отработал метод remove_exhibit"

mus.add_exhibit(p)
mus.add_exhibit(pic)
answ = mus.get_info_exhibit(0)
assert answ == f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}", "некорректно отработал метод get_info_exhibit"
print("Правильный ответ.")
