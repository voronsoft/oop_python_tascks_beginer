# TEST-TASK___________________________________
def test_8(PassengerAircraft, Aircraft, WarPlane):
    assert issubclass(PassengerAircraft, Aircraft), "PassengerAircraft, должен быть дочерним классом класса Aircraft"
    assert issubclass(WarPlane, Aircraft), "WarPlane, должен быть дочерним классом класса Aircraft"

    try:
        PassengerAircraft(21, 1250, 8000, 12000.5, 140)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError когда тип значения не соответствует условию задачи"

    try:
        PassengerAircraft('МС-21', 0, 8000, 12000.5, 140)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError когда тип значения не соответствует условию задачи"

    try:
        PassengerAircraft('МС-21', 1250, 0, 12000.5, 140)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError когда тип значения не соответствует условию задачи"

    try:
        PassengerAircraft('МС-21', 1250, 1, 0, 140)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError когда тип значения не соответствует условию задачи"

    try:
        PassengerAircraft('МС-21', 1250, 1, 1, 0)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError когда тип значения не соответствует условию задачи"

    temp1 = PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140)
    assert "_chairs" in temp1.__dict__, "не найден _chairs атрибут"

    temp2 = WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10})
    assert '_weapons' in temp2.__dict__, "не найден _weapons атрибут"
    assert type(temp2.__dict__['_weapons']) is dict, "'_weapons' должен быть словарем"

    print("Всё получилось!")
