"""
Подвиг 4. Создается программа по учету склада. Каждый предмет на складе должен описываться базовым классом Thing.
Объекты этого класса создаются командой:
th1 = Thing(name, weight)
где name - наименование предмета (строка);
weight - вес предмета (вещественное число).

Для описания каждого конкретного вида предметов, создаются дочерние классы (на основе базового Thing):
ArtObject - для представления арт-объектов;
Computer - для системных блоков компьютеров;
Auto - для автомобилей.

Объекты этих классов создаются командами:
obj = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
obj = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - вещественные или целые числа

На основе класса Auto создаются дочерние классы Mercedes и Toyota, объекты которых определяются командами:
auto = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования, в годах (целое число)
auto = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
Во всех объектах классов должны создаваться соответствующие локальные атрибуты: name, weight и т.д.
Инициализация атрибутов должна выполняться в соответствующих классах (не должно быть дублирования кода).

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""


class Thing:
    """Предмет"""

    def __init__(self, name=None, weight=0.0):
        self.name = str(name)  # наименование предмета (строка)
        self.weight = float(weight)  # вес предмета (вещественное число)


# obj = ArtObject(name, weight, author, date)  # author - автор (строка); date - дата создания (строка)
class ArtObject(Thing):  # - для представления арт-объектов;
    """Представление арт-объектов"""

    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        self.author = str(author)  # автор (строка)
        self.date = str(date)  # дата создания (строка)


# obj = Computer(name, weight, memory, cpu)    # memory - размер памяти (целое число); cpu - тип процессора (строка)
class Computer(Thing):  # - для системных блоков компьютеров;
    """Представление системных блоков компьютеров"""

    def __init__(self, name, weight, memory, cpu):
        super().__init__(name, weight)
        self.memory = int(memory)  # размер памяти (целое число)
        self.cpu = str(cpu)  # тип процессора (строка)


# obj = Auto(name, weight, dims)               # dims - габариты, кортеж (width, length, height) - вещественные или целые числа
class Auto(Thing):  # - для автомобилей.
    """Представление автомобилей"""

    def __init__(self, name, weight, dims, model=None):
        super().__init__(name, weight)
        self.dims = dims  # габариты, кортеж (width, length, height) - вещественные или целые числа
        self.model = str(model)  # модель (строка)


# auto = Mercedes(name, weight, dims, model, old) # model - модель (строка); old - время использования, в годах (целое число)
class Mercedes(Auto):
    """Марка автомобилей Mercedes"""

    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims, model)
        self.old = int(old)  # время использования, в годах (целое число)


# auto = Toyota(name, weight, dims, model, wheel) # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
class Toyota(Auto):
    """Марка автомобилей Toyota"""

    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims, model)
        self.wheel = bool(wheel)  # тип руля: True - лево-рульный, False - право-рульный

# # TEST
# th1 = Thing()
# # Объекты этих классов создаются командами:
# Art = ArtObject('Картина', 2.1, 'Норов', 1977)  # author - автор (строка); date - дата создания (строка)
# Comp = Computer('Spectrum', 1.2, 8000, 'INTEL')  # memory - размер памяти (целое число); cpu - тип процессора (строка)
# Aut = Auto('BMW', 1960, (100, 200, 300))  # dims - габариты, кортеж (width, length, height) - вещественные или целые числа
# model_M = Mercedes('Viana', 2.5, (2.5, 3.4, 5.2), 'Mercedes', 3)  # model - модель (строка); old - время использования, в годах (целое число)
# model_T = Toyota('Land Cruiser', 2.2, (2.5, 3.4, 5.2), 'Toyota', True)  # model - модель (строка); wheel - тип руля: True - леворульный, False - праворульный
