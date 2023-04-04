# TEST-TASK___________________________________
def test_9(InputDigits, input_dg):
    st = "12 -5 10 83"
    res = input_dg(st)
    assert type(res) == list, "ошибка должен вернуться список "
    assert res == [12, -5, 10, 83] and all(True if type(_) is int else False for _ in res), \
        "возвращаемые данные некорректны"

    print("Правильный ответ  )")
