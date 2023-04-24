# TEST-TASK___________________________________
def test_8(IntegerValidator, FloatValidator, Validator):
    integer_validator = IntegerValidator(-10, 10)
    float_validator = FloatValidator(-1, 1)
    assert issubclass(IntegerValidator, Validator), "IntegerValidator должен быть дочерним классом класса Validator"
    assert issubclass(FloatValidator, Validator), "класс FloatValidator должен быть дочерним классом класса Validator"
    assert callable(integer_validator), "экземпляр класса obj_I_V = IntegerValidator() должен быть вызываемым obj()"
    assert callable(float_validator), "экземпляр класса obj_F_V = FloatValidator() должен быть вызываемым obj()"
    assert integer_validator(10), "при проверке значения вернулся неправильный ответ"

    try:
        integer_validator(10)
    except ValueError:
        assert False, "некорректно прошла проверка допустимого значения"
    else:
        assert True

    try:
        integer_validator(10.0)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка недопустимого значения"

    try:
        integer_validator(-11)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка если значение меньше диапазона"

    try:
        integer_validator(11)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка если значение больше диапазона"

    try:
        float_validator(1.0)
    except ValueError:
        assert False, "некорректно прошла проверка допустимого значения"
    else:
        assert True

    try:
        float_validator(1)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка недопустимого значения"

    try:
        float_validator(-2)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка если значение меньше диапазона"

    try:
        float_validator(2)
    except ValueError:
        assert True
    else:
        assert False, "некорректно прошла проверка если значение больше диапазона"

    print("Правильно, так держать!")
