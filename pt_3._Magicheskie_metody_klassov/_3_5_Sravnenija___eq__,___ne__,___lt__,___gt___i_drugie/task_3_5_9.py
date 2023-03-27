"""
Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка);
ro - плотность тела (число: вещественное или целочисленное);
volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:
m = ro * volume
P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""


class Body:
    def __init__(self, name, ro, volume):
        if isinstance(name, str) and isinstance(ro, (int, float)) and isinstance(volume, (int, float)):
            self.name = name
            self.ro = ro
            self.volume = volume
        else:
            raise TypeError('Неверный тип данных')

    # body1 > body2  # True, если масса тела body1 больше массы тела body2
    def __gt__(self, other):
        if type(other) in (int, float):
            return (self.ro > self.volume) < other
        else:
            return (self.ro * self.volume) > (other.ro * other.volume)

    def __lt__(self, other):
        if type(other) in (int, float):
            return (self.ro * self.volume) < other
        else:
            return (self.ro * self.volume) < (other.ro * other.volume)

    # body1 == body2 # True, если масса тела body1 равна массе тела body2
    def __eq__(self, other):
        if type(other) in (int, float):
            return (self.ro * self.volume) == other
        return (self.ro * self.volume) == (other.ro * other.volume)

    def __ne__(self, other):
        if type(other) in (int, float):
            return (self.ro * self.volume) != other
        else:
            return (self.ro * self.volume) != (other.ro * other.volume)

    # body2 == 5     # True, если масса тела body2 равна 5
    # Масса тела вычисляется по формуле:
    # m = ro * volume

# # TEST
# a = Body('Lora', 10, 10)
# b = Body('Dora', 20, 20)
# x = a > b
# x1 = a < b
# x2 = 10 < a
# x3 = 10 > a
# x4 = a == 5
# x5 = a != 5