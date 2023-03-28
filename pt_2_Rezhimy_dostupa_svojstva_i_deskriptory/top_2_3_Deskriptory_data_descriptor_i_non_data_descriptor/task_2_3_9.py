"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/S4CDXCG9nbA

Подвиг 9 (на повторение).
Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:
bag = Bag(max_weight)
где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).
В каждом объекте этого класса должен создаваться локальный приватный атрибут:
__things - список вещей в рюкзаке (изначально список пуст).
Сам же класс Bag должен иметь объект-свойство:
- things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).
Также в классе Bag должны быть реализованы следующие методы:
- add_thing(self, thing) - добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит);
- remove_thing(self, indx) - удаление предмета по индексу списка __things;
= get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.

Каждая вещь описывается как объект класса Thing и создается командой:
t = Thing(name, weight)
В каждом объекте класса Thing должны формироваться локальные атрибуты:
name - наименование предмета (строка);
weight - вес предмета (целое или вещественное число).

Пример использования классов (эти строчки в программе писать не нужно):
bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


# Необходимо объявить класс Bag (рюкзак), объекты которого будут создаваться командой:
# bag = Bag(max_weight)
class Bag:
    """Создает рюкзак"""

    def __init__(self, max_weight=0):
        # где max_weight - максимальный суммарный вес вещей, который выдерживает рюкзак (целое число).
        self.max_weight = int(max_weight)
        # В каждом объекте этого класса должен создаваться локальный приватный атрибут:
        # __things - список вещей в рюкзаке (изначально список пуст).
        self.__things = list()
        # общий вес добавленных вещей в рюкзак
        self._sum_weight_things = 0.0

    # Сам же класс Bag должен иметь объект-свойство:
    # - things - для доступа к локальному приватному атрибуту __things (только для считывания, не записи).
    @property
    def things(self):
        """Объект-свойство для считывания"""
        return self.__things

    # Также в классе Bag должны быть реализованы следующие методы:
    def add_thing(self, thing):
        """Добавление нового предмета в рюкзак (добавление возможно, если суммарный вес (max_weight) не будет превышен, иначе добавление не происходит)"""

        if self._sum_weight_things + thing.weight <= self.max_weight:
            self.__things.append(thing)
            # суммируем вес вещей
            self._sum_weight_things += thing.weight

    def remove_thing(self, indx):
        """Удаление предмета по индексу списка __things"""
        del self.__things[indx]

    # - get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.
    def get_total_weight(self):
        """Возвращает суммарный вес предметов в рюкзаке"""
        return self._sum_weight_things


# Каждая вещь описывается как объект класса Thing и создается командой:
# t = Thing(name, weight)
# В каждом объекте класса Thing должны формироваться локальные атрибуты:
class Thing:
    """Вещь в рюкзаке"""

    def __init__(self, name: str, weight: float):
        self.name = str(name)  # name - наименование предмета (строка);
        self.weight = float(weight)  # weight - вес предмета (целое или вещественное число).


# TEST-TASK___________________________________
x_thing = Thing("Книга по Python", 100)
assert hasattr(x_thing, 'name') and hasattr(x_thing, 'weight'), "В классе не созданны локальные атрибуты"
assert type(x_thing.name) is str, "Название должно быть строкой"
assert type(x_thing.weight) is float or type(x_thing.weight) is int, "Вес должен быть числом"

bag = Bag(1000)
assert hasattr(bag, 'max_weight'), "Не создан атрибут max_weight"
assert type(bag.max_weight) is int, "Максимальный суммарный вес вещей должен быть целым числом"
assert '_Bag__things' in bag.__dict__, "Не создан локальный приватный атрибут __things"

assert bag.things == [], "Нет доступа к локальному приватному атрибуту __things"
assert type(bag.things) is list, "__things должен быть списком"
assert len(bag.things) == 0, "__things изначально должен быть пустым"

# проверка add_thing добавление вещей

assert hasattr(bag, "add_thing"), "Не создан метод add_thing"
assert bag.max_weight >= sum(_.weight for _ in bag.things), "Некоректно отработал метод add_thing"

# проверка get_total_weight вес предметов в рюкзаке
assert hasattr(bag, "get_total_weight"), "Не создан метод get_total_weight"
bag.add_thing(Thing("Палатка", 500))
assert bag.get_total_weight() == sum(_.weight for _ in bag.things), "Некоректно отработал метод get_total_weight"
print("Умница правильный ответ !")
