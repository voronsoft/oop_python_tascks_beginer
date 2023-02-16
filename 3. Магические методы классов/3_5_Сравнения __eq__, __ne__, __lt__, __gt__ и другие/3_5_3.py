"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/cHV-yuNFavg
Подвиг 3. Объявите класс Track (маршрут), объекты которого создаются командой:
track = Track(start_x, start_y)
где start_x, start_y - координаты начала маршрута (целые или вещественные числа).

Каждый линейный сегмент маршрута определяется классом TrackLine, объекты которого создаются командой:

line = TrackLine(to_x, to_y, max_speed)
где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа);
max_speed - максимальная скорость на данном участке (целое число).

Для формирования и работы с маршрутом в классе Track должны быть объявлены следующие методы:
add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
get_tracks(self) - получение кортежа из объектов класса TrackLine.

Также для объектов класса Track должны быть реализованные следующие операции сравнения:
track1 == track2  # маршруты равны, если равны их длины
track1 != track2  # маршруты не равны, если не равны их длины
track1 > track2   # True, если длина пути для track1 больше, чем для track2
track1 < track2   # True, если длина пути для track1 меньше, чем для track2
И функция:
n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track

Создайте два маршрута track1 и track2 с координатами:
1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.
P.S. На экран в программе ничего выводить не нужно.
"""

from math import sqrt


class Track:
    """Маршрут"""

    def __init__(self, start_x=0, start_y=0):
        if type(start_x) in (int, float) and type(start_y) in (int, float):
            # start_x, start_y - координаты начала маршрута (целые или вещественные числа)
            self.start_x = start_x
            self.start_y = start_y
        # список точек
        self.list_points = list()

    # метод подсчета длинны отрезков по формуле
    # x = sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2)) формула подсчёта длины маршрута
    def sum_len_points(self):
        distance = 0
        for _i in range(len(self.list_points)):
            # если это начало списка
            if _i == 0:
                distance += sqrt(pow(self.start_x - self.list_points[_i].to_x, 2) + \
                                 pow(self.start_y - self.list_points[_i].to_y, 2))
            # начало цикла со второго элемента, что бы просуммировать полное расстояние между точками.
            else:
                _a = self.list_points[_i].to_x, self.list_points[_i].to_y
                _b = self.list_points[_i - 1].to_x, self.list_points[_i - 1].to_y
                distance += sqrt(sum(pow(i[0] - i[1], 2) for i in zip(_b, _a)))

        return distance

    # Также для объектов класса Track должны быть реализованные следующие операции сравнения:
    def add_track(self, tr):
        """Добавление линейного сегмента маршрута (следующей точки)"""
        self.list_points.append(tr)

    def get_tracks(self):
        """Получение кортежа из объектов класса TrackLine"""
        return tuple(i for i in self.list_points)

    def __eq__(self, other):
        """track1 == track2  # маршруты равны, если равны их длины"""
        return Track.sum_len_points(self) == Track.sum_len_points(other)

    def __ne__(self, other):
        """track1 != track2  # маршруты не равны, если не равны их длины"""
        return Track.sum_len_points(self) != Track.sum_len_points(other)

    def __gt__(self, other):
        """track1 > track2  # True, если длина пути для track1 больше, чем для track2"""
        return Track.sum_len_points(self) > Track.sum_len_points(other)

    def __lt__(self, other):
        """track1 < track2  # True, если длина пути для track1 меньше, чем для track2"""
        return Track.sum_len_points(self) < Track.sum_len_points(other)

    def __len__(self):
        """n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track"""
        return int(Track.sum_len_points(self))


# line = TrackLine(to_x, to_y, max_speed)
# где to_x, to_y - координаты следующей точки маршрута (целые или вещественные числа);
# max_speed - максимальная скорость на данном участке (целое число).
class TrackLine:
    """Линейный сегмент маршрута"""

    def __init__(self, x, y, max_speed):
        if type(x) in (int, float) and type(y) in (int, float) and type(max_speed) == int:
            self.to_x = x
            self.to_y = y
            self.max_speed = int(max_speed)
        else:
            raise TypeError('Неверный тип данных.')


# TEST
# Создайте два маршрута track1 и track2 с координатами:
# 1-й маршрут: (0; 0), (2; 4), (5; -4) и max_speed = 100
track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))

# 2-й маршрут: (0; 1), (3; 2), (10; 8) и max_speed = 90
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

# Сравните их между собой на равенство. Результат сравнения сохраните в переменной res_eq.
# P.S. На экран в программе ничего выводить не нужно.
res_eq = track1 == track2

# # вычисляем длины маршрутов через метод (проверка)
# len_track1 = Track.sum_len_points(track1)
# len_track2 = Track.sum_len_points(track2)
#
# # маршруты равны, если равны их длины (вычисляем сравнивая длины объектов)
# # равны ?
# xTrue = track1 == track2  # False
#
# # не равны ?
# xFalse = track1 != track2  # True
#
# gt = track1 > track2  # True, если длина пути для track1 больше, чем для track2
# lt = track1 < track2  # True, если длина пути для track1 меньше, чем для track2
#
# # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
# track1_len = len(track1)
# track2_len = len(track2)
#
# # получение кортежа из объектов класса TrackLine.
# print(track1.get_tracks())
