"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FaHqn8Yr45o

Подвиг 10.
Объявите класс GeyserClassic - фильтр для очистки воды.
В этом классе должно быть три слота для фильтров.
Каждый слот строго для своего класса фильтра:
- Mechanical - для очистки от крупных механических частиц;
- Aragon - для последующей очистки воды;
- Calcium - для обработки воды на третьем этапе.

Объекты классов фильтров должны создаваться командами:
filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)
Во всех объектах этих классов должен формироваться локальный атрибут:
date - дата установки фильтров (для простоты - положительное вещественное число).
Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.

Объекты класса GeyserClassic должны создаваться командой:
g = GeyserClassic()
А сам класс иметь атрибут:
MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

- add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
если он (слот) пустой (без фильтра).
Также здесь следует проверять:
что в первый слот можно установить только объекты класса Mechanical,
во второй - объекты класса Aragon
и в третий - объекты класса Calcium.
Иначе слот должен оставаться пустым.

- remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
- get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
- water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
Метод water_on() должен возвращать значение True при выполнении следующих условий:
- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])

Пример использования классов (эти строчки в программе писать не нужно):
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
P.S. На экран ничего выводить не нужно.
"""

# ваш код:
import time


# Объекты класса GeyserClassic должны создаваться командой:
# g = GeyserClassic()
class GeyserClassic:
    """ Фильтр для очистки воды"""
    # Максимальное время работы фильтра (любого)
    MAX_DATE_FILTER = 100

    # В этом классе должно быть три слота для фильтров.
    # Каждый слот строго для своего класса фильтра:
    # - Mechanical - для очистки от крупных механических частиц;
    # - Aragon - для последующей очистки воды;
    # - Calcium - для обработки воды на третьем этапе.
    def __init__(self):
        self.lst = {1: None, 2: None, 3: None}

    # и следующие методы:
    # - add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3),
    # если он (слот) пустой (без фильтра).
    # Также здесь следует проверять:
    # что в первый слот можно установить только объекты класса Mechanical,
    # во второй - объекты класса Aragon
    # и в третий - объекты класса Calcium.
    # Иначе слот должен оставаться пустым.
    def add_filter(self, slot_num, filter):
        """Добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3)"""
        if type(filter) == Mechanical and self.lst[1] is None and slot_num == 1:
            self.lst[1] = filter
        elif type(filter) == Aragon and self.lst[2] is None and slot_num == 2:
            self.lst[2] = filter
        elif type(filter) == Calcium and self.lst[3] is None and slot_num == 3:
            self.lst[3] = filter

    # - remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);
    def remove_filter(self, slot_num):
        """Извлечение фильтра из указанного слота (slot_num: 1, 2, и 3)"""
        self.lst[slot_num] = None

    # - get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);
    def get_filters(self):
        """Возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов)"""
        return tuple(i[1] for i in self.lst.items())

    # - water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.
    # Метод water_on() должен возвращать значение True при выполнении следующих условий:
    # - все три фильтра установлены в слотах;
    # - все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])
    def water_on(self):
        """Включение воды: возвращает True, если вода течет и False - в противном случае"""
        answer = False
        temp = list()
        # проверяем все ли места заняты картриджами
        if None not in self.lst.values():
            for i in self.lst.values():
                temp.append(i.date)
        else:
            return answer
        # проверяем валидность даты
        if max(temp) - min(temp) < self.MAX_DATE_FILTER:
            answer = True

        return answer


# Объекты классов фильтров должны создаваться командами:
# filter_1 = Mechanical(дата установки)
# filter_2 = Aragon(дата установки)
# filter_3 = Calcium(дата установки)
# Во всех объектах этих классов должен формироваться локальный атрибут:
# date - дата установки фильтров (для простоты - положительное вещественное число).
# Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).
# В случае присвоения нового значения, прежнее значение не менять. Ошибок никаких не генерировать.
class Mechanical:
    """Фильтр очистка от крупных механических частиц"""

    def __init__(self, date=None):
        self.date = date

    def __setattr__(self, key, value):
        """Автомат вызывается если идет запись или изменение значения в атрибут класса или объекта"""
        if hasattr(self, 'date'):
            return
        else:
            if value > 0 and type(value) in (int, float):
                return object.__setattr__(self, key, value)


class Aragon:
    """Фильтр последующaя очистка воды"""

    def __init__(self, date=None):
        self.date = date

    def __setattr__(self, key, value):
        """Автомат вызывается если идет запись или изменение значения в атрибут класса или объекта"""
        if hasattr(self, 'date'):
            return
        else:
            if value > 0 and type(value) in (int, float):
                return object.__setattr__(self, key, value)


class Calcium:
    """Фильтр обработка воды на третьем этапе"""

    def __init__(self, date=None):
        self.date = date

    def __setattr__(self, key, value):
        """Автомат вызывается если идет запись или изменение значения в атрибут класса или объекта"""
        if hasattr(self, 'date'):
            return
        else:
            if value > 0 and type(value) in (int, float):
                return object.__setattr__(self, key, value)


# end ваш код

# TEST-TASK___________________________________
from test3_1.test_3_1_10 import test_10

test_10(GeyserClassic, Mechanical, Aragon, Calcium)
# END
