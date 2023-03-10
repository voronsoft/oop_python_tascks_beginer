"""
Подвиг 6. Объявите класс Furniture (мебель), объекты которого создаются командой:

f = Furniture(name, weight)
где name - название предмета (строка); weight - вес предмета (целое или вещественное число).

В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight.
В самом классе Furniture нужно объявить приватные методы:
__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, то генерируется исключение командой:
raise TypeError('название должно быть строкой')

Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля),
если это не так, то генерируется исключение командой:
raise TypeError('вес должен быть положительным числом')

Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:
Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объекты этих классов должны создаваться командами:
obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные числа)
В каждом объекте этих классов должны создаваться соответствующие защищенные атрибуты:
- в объектах класса Closet: _name, _weight, _tp, _doors
- в объектах класса Chair: _name, _weight, _height
- в объектах класса Table: _name, _weight, _height, _square

В каждом классе (Closet, Chair, Table) объявить метод:
get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.

Пример использования классов (эти строчки в программе писать не нужно):
cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""


class Furniture:
    """Мебель"""

    def __init__(self, name, weight):
        self._name = self.__verify_name(name)  # название предмета (строка)
        self._weight = self.__verify_weight(weight)  # вес предмета (целое или вещественное число)

    # Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).
    #
    # В самом классе Furniture нужно объявить приватные методы:
    # Метод __verify_name() проверяет, что имя должно быть строкой, если это не так, то генерируется исключение командой:
    # raise TypeError('название должно быть строкой')
    def __verify_name(self, val):  # для проверки корректности имени;
        if type(val) != str:
            raise TypeError('название должно быть строкой')
        else:
            return val

    # Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля),
    # если это не так, то генерируется исключение командой:
    # raise TypeError('вес должен быть положительным числом')
    def __verify_weight(self, val):  # для проверки корректности веса.
        if type(val) in (int, float) and val > 0:
            return val
        else:
            raise TypeError('вес должен быть положительным числом')

    def __setattr__(self, key, value):
        if key == '_name':
            object.__setattr__(self, key, value)
        elif key == '_weight':
            object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)

    # возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.
    def get_attrs(self):
        return tuple(i for i in self.__dict__.values())


# На основе базового класса Furniture объявить следующие дочерние классы:
# obj = Closet(name, weight, tp, doors)   # tp: True - шкаф-купе; False - обычный шкаф; doors - число дверей (целое число)
class Closet(Furniture):  # - для представления шкафов;
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = int(doors)


# obj = Chair(name, weight, height)       # height - высота стула (любое положительное число)
class Chair(Furniture):  # - для представления стульев;
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = self.__verify_weight(height)  # height - высота стула (любое положительное число)

    # Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля),
    # если это не так, то генерируется исключение командой:
    # raise TypeError('вес должен быть положительным числом')
    def __verify_weight(self, val):  # для проверки корректности веса.
        if type(val) in (int, float) and val > 0:
            return val
        else:
            raise TypeError('вес должен быть положительным числом')


# obj = Table(name, weight, height, square) # height - высота стола; square - площадь поверхности (любые положительные числа)
class Table(Furniture):  # - для представления столов.
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = self.__verify_weight(square)  # square - площадь поверхности (любые положительные числа)

    # Метод __verify_weight() проверяет, что вес должен быть положительным числом (строго больше нуля),
    # если это не так, то генерируется исключение командой:
    # raise TypeError('вес должен быть положительным числом')
    def __verify_weight(self, val):  # для проверки корректности веса.
        if type(val) in (int, float) and val > 0:
            return val
        else:
            raise TypeError('вес должен быть положительным числом')

# # TEST
# f = Furniture('Стол', 1.0)
# # Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).
# f._name = 'Стул'  # _name == 'Стул'
#
# cl = Closet('шкаф-купе', 342.56, True, 3)
# chair = Chair('стул', 14, 55.6)
# tb = Table('стол', 34.5, 75, 10)
# print(cl.get_attrs())
# print(chair.get_attrs())
# print(tb.get_attrs())
