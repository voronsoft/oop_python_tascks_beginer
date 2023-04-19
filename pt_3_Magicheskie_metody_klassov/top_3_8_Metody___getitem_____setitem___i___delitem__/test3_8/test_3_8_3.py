# TEST-TASK___________________________________
def test_3(Track):
    tr = Track(10, -5.4)
    assert hasattr(tr, "add_point"), " объявите метод add_point"

    tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
    assert tr[0] == ((20, 0), 100), "метод add_point работает некорректно"
    tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
    assert tr[1] == ((50, -20), 80), "метод add_point работает некорректно"

    coord, speed = tr[0]  # получение координаты (кортеж с двумя числами) и скорости (число)
    assert coord == (20, 0), \
        "в переменной coord сохранен неправильный формат координат. Должно быть (кортеж с двумя числами)"
    assert speed == 100 and type(speed) is int, "в переменной speed сохранено неправильное значение"

    # - tr[indx] = speed # изменение средней скорости линейного участка маршрута по индексу indx
    tr[1] = 220
    coord, speed = tr[1]
    assert speed == 220, "ошибка, при выполнении операции tr[indx] = speed"

    tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

    try:
        tr[3]  # IndexError
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка IndexError"

    print("Правильное решение !")
