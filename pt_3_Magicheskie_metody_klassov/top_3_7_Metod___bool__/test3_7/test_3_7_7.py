# TEST-TASK___________________________________
def test_7(Ellipse, lst_geom):
    el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
    assert len(el1.__dict__) == 0, "при el1 = Ellipse() в объекте не должно быть локальных атрибутов "

    el2 = Ellipse(1, 1, 2, 2)
    assert hasattr(el2, "x1") and hasattr(el2, "y1") and hasattr(el2, "x2") and hasattr(el2, "y2"), \
        "ошибка атрибутов"
    assert all(True if type(_) in (int, float) else False for _ in
               el2.__dict__.values()), "значениями могут быть только числа"

    assert hasattr(Ellipse, "__bool__"), "метод __bool__ необъявлен"
    assert hasattr(Ellipse, "get_coords"), "метод get_coords необъявлен"

    try:
        el1.get_coords()
    except AttributeError:
        assert True
    else:
        assert False, "если атрибуты отсутствуют должна генерироваться ошибка - AttributeError"

    assert el2.get_coords() == (1, 1, 2, 2), "метод get_coords вернул неправильное значение"

    assert len(lst_geom) == 4 and all(True if isinstance(_, Ellipse) else False for _ in lst_geom), "ошибка в lst_geom"

    temp = [_ for _ in lst_geom if bool(_)]
    assert len(temp) == 2 and all(True if len(_.__dict__) == 4 else False for _ in temp), "ошибка в методе __bool__"
    print("Правильное решение, молодец !")
