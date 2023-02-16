"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YPppgpsCo3E

Подвиг 5. Объявите класс Box (ящик), объекты которого создаются командой:
box = Box(name, max_weight)
где name - название ящика (строка);
max_weight - максимальный суммарный вес вещей в ящике (любое положительное число).

В каждом объекте этого класса должны формироваться локальные атрибуты:
_name - ссылка на параметр name;
_max_weight - ссылка на параметр max_weight;
_things - список из вещей, хранящиеся в ящике (изначально пустой список).

В классе Box объявите метод:
def add_thing(self, obj)
для добавления новой вещи в ящик,
где obj - кортеж из двух значений: (название_вещи, вес_вещи)
Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight, то генерировать исключение командой:
raise ValueError('превышен суммарный вес вещей')

Затем, объявите еще один класс BoxDefender, который должен работать совместно с менеджером контекста следующим образом
(эти строчки в программе не писать):
box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))

with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    ...
Здесь b - это ссылка на объект класса Box.
Если при добавлении вещей возникает исключение ValueError, то объект box должен оставаться без изменений
(с теми вещами, что были до вызова менеджера контекста). Иначе, все добавленные вещи остаются в объекте box.

P.S. В программе только объявить классы. Выводить что-либо на экран и использовать классы не нужно.

"""


class Box:
    """ящик"""

    def __init__(self, name, max_weight):
        self._name = name  # название ящика (строка) / ссылка на параметр name
        self._max_weight = max_weight  # максимальный суммарный вес вещей в ящике (любое положительное число) / ссылка на параметр max_weight
        self._things = list()  # список из вещей, хранящиеся в ящике (изначально пустой список) /
        self._real_weight = 0

    # В классе Box объявите метод:
    # def add_thing(self, obj) для добавления новой вещи в ящик,
    # где obj - кортеж из двух значений: (название_вещи, вес_вещи)
    # Если в момент добавления новой вещи суммарный вес всех вещей в ящике становится больше величины _max_weight, то генерировать исключение командой:
    # raise ValueError('превышен суммарный вес вещей')
    def add_thing(self, obj):
        """Добавление новой вещи в ящик"""
        # где obj - кортеж из двух значений: (название_вещи, вес_вещи)
        if self._real_weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        else:
            self._things.append(obj)
            self._real_weight += obj[1]


# должен работать совместно с менеджером контекста
class BoxDefender:
    def __init__(self, vol):
        self._obj = vol
        self._temp_things = vol._things[:]

    def __enter__(self):
        return self._obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self._obj._things = self._temp_things
            self._obj._real_weight = sum(i[1] for i in self._temp_things)

# # TEST
# b = Box('name', 2000)
# assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"
# #
# b.add_thing(("1", 100))
# b.add_thing(("2", 200))
# #
# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 1000))
#         bb.add_thing(("4", 1900))
# except ValueError:
#     assert len(b._things) == 2
# #
# else:
#     assert False, "не сгенерировалось исключение ValueError"
# #
# try:
#     with BoxDefender(b) as bb:
#         bb.add_thing(("3", 100))
# except ValueError:
#     assert False, "возникло исключение ValueError, хотя, его не должно было быть"
# else:
#     assert len(b._things) == 3, "неверное число элементов в списке _things"
