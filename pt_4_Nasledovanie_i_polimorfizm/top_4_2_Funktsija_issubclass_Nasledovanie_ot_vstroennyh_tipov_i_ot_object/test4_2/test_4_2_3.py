# TEST-TASK___________________________________
def test_3(ListInteger):
    assert issubclass(ListInteger, list), "ListInteger должен быть унаследован от list"
    assert "__setitem__" in ListInteger.__dict__, "вы не переопределили метод __setitem__"
    assert "__init__" in ListInteger.__dict__, "вы не переопределили метод __init__"
    assert "append" in ListInteger.__dict__, "вы не объявили метод append"

    s = ListInteger((1, 2, 3))
    try:
        ListInteger(('a'))
    except TypeError:
        assert True
    else:
        assert False, "ошибка не сгенерировалась ошибка TypeError при попытке присвоить списку не целочисленное значение"

    try:
        ListInteger((1.0))
    except TypeError:
        assert True
    else:
        assert False, "ошибка не сгенерировалась ошибка TypeError при попытке присвоить списку не целочисленное значение"

    assert all(True if type(_) is int else False for _ in s), "в списке могут быть только целые числа"

    s[1] = 10
    assert s[1] == 10, "некорректно отработал метод __setitem__ при операции s[1] = 10"

    s.append(11)
    assert s[-1] == 11, "некорректно отработал метод append при операции s.append(11)"

    try:
        s[0] = 10.5  # TypeError
    except TypeError:
        assert True
    else:
        assert False, "некорректно отработал метод __setitem__ при операции s[1] = s[0] = 10.5"

    print("Правильно, умница !")
