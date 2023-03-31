# TEST-TASK___________________________________
def test_7(objs):
    assert len(set(objs)) == 5, "ошибка, попробуйте ещё раз"
    assert all(True if objs[4] == _ else False for _ in objs[5:]), "ошибка последние 5 объектов должны быть одинаковые"

    [print(_) for _ in objs]
    print("Правильно !")
