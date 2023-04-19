# TEST-TASK___________________________________
def test_8(TicTacToe, Cell):
    g = TicTacToe()
    g.clear()
    assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
    g[1, 1] = 1
    g[2, 1] = 2
    assert g[1, 1] == 1 and g[2, 1] == 2, \
        "неверно отработала операция присваивания новых значений клеткам игрового поля " \
        "(или, некорректно работает считывание значений)"

    try:
        res = g[3, 0]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    try:
        g[3, 0] = 5
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

    g.clear()
    g[0, 0] = 1
    g[1, 0] = 2
    g[2, 0] = 3

    assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
        1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

    cell = Cell()
    assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
    res = cell.is_free
    cell.is_free = True
    assert bool(cell), "функция bool вернула False для свободной клетки"
    print("Правильный ответ )")
