# TEST-TASK___________________________________
def test_5(Validator, FloatValidator):
    assert issubclass(Validator, object), "объявите базовый класс Validator"
    assert hasattr(Validator, "_is_valid") and callable(
        Validator._is_valid), "в классе Validator не найден метод _is_valid"

    try:
        temp = Validator._is_valid("abc", "abc")
    except NotImplementedError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка NotImplementedError"

    assert issubclass(FloatValidator, Validator), "объявите дочерний класс FloatValidator класса Validator"
    assert FloatValidator._is_valid != Validator, "в классе не переопределен метод _is_valid"

    float_validator = FloatValidator(0, 10.5)
    assert "min_value" in float_validator.__dict__ and "max_value" in float_validator.__dict__, \
        "не найдены локальные атрибуты min_value и max_value"

    assert callable(float_validator), "экземпляр класса FloatValidator должен быть вызываемым obj_float_validator(5)"
    assert float_validator(1) == False, "при проверке значения экземпляр класса вернул не правильный ответ"
    assert float_validator(1.0) == True, "при проверке значения экземпляр класса вернул не правильный ответ"
    assert float_validator(-1.0) == False, "при проверке значения экземпляр класса вернул не правильный ответ"

    print("Правильное решение !!")
