# TEST-TASK___________________________________
def test_7(RadiusVector):
    v = RadiusVector(1, 2, 3, 4, 5)
    v2 = RadiusVector(1, 1, 1)
    assert len(v.coords) == 5 and len(v2.coords) == 3, ""
    assert all(True if type(_) in (int, float) else False for _ in v.coords), \
        "ошибка, значения координат должны быть int или float"

    assert v[1] == 2, "ошибка, при получении значения i-й координаты (целое число, отсчет с нуля)"
    assert v[1:4] == (2, 3, 4), "ошибка при отображении среза координат v[start:stop]"
    assert v[0:5:2] == (1, 3, 5), "ошибка при отображении среза координат v[start:stop:step]"
    v[0:5:2] = [1, 1, 1]
    assert v[:] == (
        1, 2, 1, 4, 1), "ошибка, v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат"

    print("Правильный ответ.")
