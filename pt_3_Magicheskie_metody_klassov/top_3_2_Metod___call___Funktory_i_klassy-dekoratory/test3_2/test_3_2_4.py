# TEST-TASK___________________________________
def test_4(LengthValidator, CharsValidator, LoginForm):
    try:
        issubclass(LengthValidator, object)
    except NameError:
        print("Вы не создали класс - LengthValidator")

    try:
        issubclass(CharsValidator, object)
    except NameError:
        print("Вы не создали класс - CharsValidator")

    # проверка создания объекта LengthValidator
    lv = LengthValidator(2, 5)
    assert callable(lv), "валидатор LengthValidator не вызываться как функция"
    assert not lv('123456'), 'ошибка в LengthValidator, проверяемая строка выходит за заданный диапазон длины знаков'

    # проверка создания объекта CharsValidator
    cv = CharsValidator('abc')
    assert callable(cv), "валидатор CharsValidator не вызываться как функция"
    assert not cv('1'), "ошибка в CharsValidator, проверяемая строка содержит недопустимые знаки"
    print("Отлично, так держать !!")
