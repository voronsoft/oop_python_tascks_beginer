"""
Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:

air = Aircraft(model, mass, speed, top)
где model - модель самолета (строка);
mass - подъемная масса самолета (любое положительное число);
speed - максимальная скорость (любое положительное число);
top - максимальная высота полета (любое положительное число).

В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами:
_model, _mass, _speed, _top и соответствующими значениями.
Если передаваемые аргументы не соответствуют указанным критериям (строка, любое положительное число),
то генерируется исключение командой:
raise TypeError('неверный тип аргумента')

Далее, в программе объявите следующие дочерние классы:
PassengerAircraft - пассажирский самолет;
WarPlane - военный самолет.

Объекты этих классов создаются командами:
pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест (целое положительное число)
wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь);
ключи - название оружия, значение - количество
В каждом объекте классов
PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами _chairs и _weapons соответственно.
Инициализация остальных атрибутов должна выполняться через инициализатор базового класса.
В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons.
Если тип данных не совпадает, то генерировать исключение командой:
raise TypeError('неверный тип аргумента')

Создайте в программе четыре объекта самолетов со следующими данными:

PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}

Все эти объекты представить в виде списка planes.

P.S. В программе нужно объявить только классы и сформировать список На экран выводить ничего не нужно.
"""


class Aircraft:
    def __init__(self, model, mass, speed, top):
        self.verify_data([model, mass, speed, top])
        self._model = model  # - модель самолета (строка);
        self._mass = mass  # - подъемная масса самолета (любое положительное число);
        self._speed = speed  # - максимальная скорость (любое положительное число);
        self._top = top  # - максимальная высота полета (любое положительное число).

    def verify_data(self, lst):
        if type(lst[0]) == str and all(True if type(i) in (int, float) and i >= 0 else False for i in lst[1:]):
            return True
        else:
            raise TypeError('неверный тип аргумента')


# Далее, в программе объявите следующие дочерние классы:
# В каждом объекте классов
# PassengerAircraft и WarPlane должны формироваться локальные атрибуты с именами _chairs и _weapons соответственно.
# Инициализация остальных атрибутов должна выполняться через инициализатор базового класса.
# В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых аргументов chairs и weapons.
# Если тип данных не совпадает, то генерировать исключение командой:
# raise TypeError('неверный тип аргумента')
class PassengerAircraft(Aircraft):  # - пассажирский самолет;
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.verify_chairs(chairs)
        self._chairs = chairs  # число пассажирских мест (целое положительное число)

    def verify_chairs(self, vol):
        if type(vol) == int and vol >= 0:
            return True
        else:
            raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):  # - военный самолет.
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.verify_weapons(weapons)
        self._weapons = weapons  # вооружение (словарь), ключи - название оружия, значение - количество

    def verify_weapons(self, vol):
        if type(vol) == dict:
            return True
        else:
            raise TypeError('неверный тип аргумента')


# TEST
planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
          ]
