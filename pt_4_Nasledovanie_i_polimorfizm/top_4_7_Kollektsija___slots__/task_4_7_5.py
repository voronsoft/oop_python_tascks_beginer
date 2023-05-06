"""
Подвиг 5. Объявите класс Planet (планета), объекты которого создаются командой:
p = Planet(name, diametr, period_solar, period)
где:
name - наименование планеты;
diametr - диаметр планеты (любое положительное число);
period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число);
period - период обращения планеты вокруг своей оси (любое положительное число).

В каждом объекте класса Planet должны формироваться локальные атрибуты с именами:
_name,
_diametr,
_period_solar,
_period
c соответствующими значениями.

Затем, объявите класс с именем SolarSystem (солнечная система).
В объектах этого класса должны быть допустимы, следующие локальные атрибуты (ограничение задается через коллекцию __slots__):

_mercury - ссылка на планету Меркурий (объект класса Planet);
_venus - ссылка на планету Венера (объект класса Planet);
_earth - ссылка на планету Земля (объект класса Planet);
_mars - ссылка на планету Марс (объект класса Planet);
_jupiter - ссылка на планету Юпитер (объект класса Planet);
_saturn - ссылка на планету Сатурн (объект класса Planet);
_uranus - ссылка на планету Уран (объект класса Planet);
_neptune - ссылка на планету Нептун (объект класса Planet).

Объект класса SolarSystem должен создаваться командой:
s_system = SolarSystem()
и быть только один (одновременно в программе два и более объектов класса SolarSystem недопустимо).
Используйте для этого паттерн Singleton.

В момент создания объекта SolarSystem должны автоматически создаваться перечисленные локальные атрибуты
и ссылаться на соответствующие объекты класса Planet со следующими данными по планетам:

название        диаметр         период вращения вокруг солнца\дни       период вращения вокруг оси\часы
Меркурий        4878                        87,97                                   1407,5
Венера          12104                       224,7                                   5832,45
Земля           12756                       365,3                                   23,93
Марс            6794                        687                                     24,62
Юпитер          142800                      4330                                    9,9
Сатурн          120660                      10753                                   10,63
Уран            51118                       30665                                   17,2
Нептун          49528                       60150                                   16,1

Создайте в программе объект s_system класса SolarSystem.

P.S. В программе следует объявить только классы и создать объект s_system. На экран выводить ничего не нужно.
"""


# ваш код:
class Planet:

    def __init__(self, name=None, diametr=0, period_solar=0, period=0):
        # name - наименование планеты
        self._name = str(name)

        # diametr - диаметр планеты (любое положительное число)
        self._diametr = diametr if type(diametr) in (int, float) and diametr >= 0 else None

        # period_solar - период (время) обращения планеты вокруг Солнца (любое положительное число)
        self._period_solar = period_solar if type(period_solar) in (int, float) and period_solar >= 0 else None

        # period - период обращения планеты вокруг своей оси (любое положительное число)
        self._period = period if type(period) in (int, float) and period >= 0 else None


class SolarSystem:
    """Солнечная система"""
    __slots__ = ['_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune']
    SS = None

    def __new__(cls, *args, **kwargs):
        if cls.SS is None:
            cls.SS = super().__new__(cls)
        return cls.SS

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


# TEST
s_system = SolarSystem()

# end ваш код
# TEST-TASK___________________________________
from test4_7.test_4_7_5 import test_5

test_5(Planet, s_system, SolarSystem)
# END
