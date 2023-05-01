# TEST-TASK___________________________________
def test_9(Track, PointTrack):
    assert hasattr(Track, "start_x"), ""
    assert hasattr(Track, "start_y"), ""
    assert isinstance(Track.points, property), ""
    assert hasattr(Track, "add_back"), ""
    assert hasattr(Track, "add_front"), ""
    assert hasattr(Track, "pop_back"), ""
    assert hasattr(Track, "pop_front"), ""
    assert isinstance(Track.points, property), ""

    tr = Track(0, 0)
    assert "_Track__points" in tr.__dict__ and type(tr._Track__points) is list, ""
    assert tr.points == (), "объект свойство points отработал не верно"
    assert tr.start_x == 0, ""
    assert tr.start_y == 0, ""

    try:
        PointTrack(0, '0')
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError при вводе недопустимых значений"

    tr = Track(PointTrack(10, 10), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))

    x = PointTrack(1.4, 0)
    tr.add_back(x)  # - добавление новой точки в конец маршрута (pt - объект класса PointTrack);
    assert tr.points[-1] == x, "метод add_back работает некорректно"

    x1 = PointTrack(1.9, 1)
    tr.add_front(x1)  # - добавление новой точки в начало маршрута (pt - объект класса PointTrack);
    assert tr.points[0] == x1, "метод add_front работает некорректно"

    tr.pop_front()  # - удаление первой точки из маршрута.
    assert x1 not in tr.points, "метод pop_front работает некорректно"

    x = tr.points[-1]
    tr.pop_back()  # - удаление последней точки из маршрута;
    assert x not in tr.points, "метод pop_back работает некорректно"

    print("Правильное решение !")
