# TEST-TASK___________________________________
def test_9(Dimensions, lst_dims, s_inp):
    d = Dimensions(1, 2, 3.0)
    assert type(d.a) in (int, float) and type(d.b) in (int, float) and type(d.c) in (int, float), \
        "ошибка, значения могут быть типа - int или float"

    assert d.a > 0 and d.b > 0 and d.c > 0, "не сгенерировалась ошибка ValueError"

    try:
        Dimensions(-1, 0, 3.0)
    except ValueError:
        assert True
    else:
        assert False, ("не сгенерировалась ошибка ValueError")

    assert d.__class__.__hash__ is not object.__class__.__hash__, "Метод __hash__() не был переопределен"

    assert len(lst_dims) == len(s_inp.split(";")), "количество объектов в списке lst_dims неправильное"

    x = 1
    for _ in [hash(i) for i in lst_dims]:
        if x is None:
            x = _
        elif _ >= x:
            x = _
        elif _ < x:
            assert False, "неправильно отсортирован список lst_dims"

    print("Правильный ответ !!")
