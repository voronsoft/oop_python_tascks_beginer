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
