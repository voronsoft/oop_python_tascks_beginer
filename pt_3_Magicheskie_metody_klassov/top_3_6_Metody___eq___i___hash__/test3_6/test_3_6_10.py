# TEST-TASK___________________________________
def test_10(Triangle):
    tr = Triangle(5, 4, 3)
    assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

    try:
        tr = Triangle(-5, 4, 3)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        tr = Triangle(10, 1, 1)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    tr = Triangle(5, 4, 3)
    assert len(tr) == 12, "функция len вернула неверное значение"
    assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"

    print("Отличное решение !!")
