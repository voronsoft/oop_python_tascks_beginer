# TEST-TASK___________________________________
def test_4(Digit, Integer, Float, Positive, Negative, PrimeNumber, FloatPositive, digits, lst_positive, lst_float):
    assert issubclass(Digit, object), "объявите базовый класс Digit"
    assert issubclass(Integer, Digit), " класс должен быть дочерним классом класса "
    assert issubclass(Float, Digit), " класс должен быть дочерним классом класса "
    assert issubclass(Positive, Digit), " класс должен быть дочерним классом класса "
    assert issubclass(Negative, Digit), " класс должен быть дочерним классом класса "

    assert issubclass(PrimeNumber, Integer) and issubclass(PrimeNumber, Positive), \
        "класс PrimeNumber должен быть унаследован от классов Integer и Positive"

    assert issubclass(FloatPositive, Float) and issubclass(FloatPositive, Positive), \
        "класс FloatPositive должен быть унаследован от классов Float и Positive"

    try:
        a1 = Digit('1')
    except TypeError:
        assert True
    else:
        assert False, "класс Digit не сгенерировал ошибку TypeError"

    try:
        a2 = Integer('1')
    except TypeError:
        assert True
    else:
        assert False, "класс Integer не сгенерировал ошибку TypeError"

    try:
        a3 = Float('1')
    except TypeError:
        assert True
    else:
        assert False, "класс Float не сгенерировал ошибку TypeError"

    try:
        a4 = Positive(-1)
    except TypeError:
        assert True
    else:
        assert False, "класс Positive не сгенерировал ошибку TypeError"

    try:
        a5 = Negative(1)
    except TypeError:
        assert True
    else:
        assert False, "класс Negative не сгенерировал ошибку TypeError"

    try:
        a5 = PrimeNumber(1)
    except TypeError:
        assert False, "класс PrimeNumber не сгенерировал ошибку TypeError"
    else:
        assert True

    try:
        a5 = FloatPositive(1.0)
    except TypeError:
        assert False, "класс FloatPositive не сгенерировал ошибку TypeError"
    else:
        assert True

    assert len(digits) == 8, "список digits содержит неправильное количество объектов"
    assert len([_ for _ in digits if issubclass(_.__class__, PrimeNumber)]) == 3 and \
           len([_ for _ in digits if issubclass(_.__class__, FloatPositive)]) == 5, "список digits ошибка"

    assert all(True if issubclass(_.__class__, Positive) else False for _ in lst_positive) and len(lst_positive) == 8, \
        "ошибка списка lst_positive, в списке должны быть объекты класса Positive"

    assert all(True if issubclass(_.__class__, Float) else False for _ in lst_float) and len(lst_float) == 5, \
        "ошибка списка lst_float, в списке должны быть объекты класса Float"

    print("Здорово, всё верно. 4")
