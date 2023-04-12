# TEST-TASK___________________________________
def test_3(Track, TrackLine, track1, track2, res_eq):
    # ВНИМАНИЕ - тест работает только в случае, что у экземпляра класса Track будут локальные атрибуты с именами start_x, start_y
    from math import sqrt

    # метод подсчета длинны отрезков по формуле
    # sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2)) формула подсчёта длины маршрута
    def sum_len_points(obj):
        distance = 0
        # определяем название списка координат
        key = str(*(i for i, v in track1.__dict__.items() if type(v) is list or type(v) is tuple))

        for _i in range(len(obj.__dict__[key])):
            # если это начало списка
            if _i == 0:
                distance += sqrt(pow(obj.start_x - obj.__dict__[key][_i].to_x, 2) +
                                 pow(obj.start_y - obj.__dict__[key][_i].to_y, 2))
                # начало цикла со второго элемента, что бы просуммировать полное расстояние между точками.
            else:
                _a = obj.__dict__[key][_i].to_x, obj.__dict__[key][_i].to_y
                _b = obj.__dict__[key][_i - 1].to_x, obj.__dict__[key][_i - 1].to_y
                distance += sqrt(sum(pow(i[0] - i[1], 2) for i in zip(_b, _a)))

        return distance

    track3 = Track(0, 0)
    assert hasattr(track3, "add_track") and hasattr(track3, "get_tracks"), "не все методы объявлены в экземпляре класса"
    assert hasattr(track3, "start_x") and hasattr(track3, "start_y"), "ошибка локальных атрибутах start_x и start_y"
    assert type(track3.start_x) in (int, float) and type(track3.start_y) in (
        int, float), "начальные координаты могут быть только int или float"

    p1 = TrackLine(2, 4, 100)
    assert type(p1.__dict__['to_x']) in (int, float) and type(p1.__dict__['to_y']) in (
        int, float), "to_x и to_y могут быть толко int или float"
    assert type(p1.__dict__["max_speed"]) is int, "max_speed может бsть только типом int"

    # add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
    track3.add_track(p1)
    assert len(track3.get_tracks()) == 1 and track3.get_tracks()[0] == p1, "метод add_track работает неверно"

    # get_tracks(self) - получение кортежа из объектов класса TrackLine.
    assert len(track3.get_tracks()) == 1 and type(
            track3.get_tracks()) is tuple, "метод get_tracks должен вернуть кортеж"
    assert all(True if isinstance(_, TrackLine) else False for _ in track3.get_tracks()), \
        "метод get_tracks вернул кортеж, но в коллекции должны быть только объекты класса TrackLine"

    # Также для объектов класса Track должны быть реализованные следующие операции сравнения:
    # track1 == track2  # маршруты равны, если равны их длины
    assert (track1 == track2) is False and (sum_len_points(track1) == sum_len_points(track2)) is False, \
        "ошибка при операции =="

    # track1 != track2  # маршруты не равны, если не равны их длины
    assert (track1 != track2) is True and sum_len_points(track1) != sum_len_points(track2), "ошибка при операции !="

    # track1 > track2   # True, если длина пути для track1 больше, чем для track2
    assert (track1 > track2) is True and sum_len_points(track1) > sum_len_points(track2), "ошибка при операции  >"

    # track1 < track2   # True, если длина пути для track1 меньше, чем для track2
    assert (track1 < track2) is False and (sum_len_points(track1) < sum_len_points(track2)) is False, \
        "ошибка при операции  <"

    # И функция:
    # n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
    assert type(len(track1)) is int and len(track1) == 13, "ошибка в методе len()"

    assert res_eq is False, "при сравнени вернулся неверный результат"

    print("Правильный ответ )!")
