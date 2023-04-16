# TEST-TASK___________________________________
def test_8(GamePole, Cell):
    p1 = GamePole(5, 20, 10)
    p2 = GamePole(10, 20, 10)
    assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
    # print(p1.pole)
    p = p1

    cell = Cell()
    assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
            Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

    cell.is_mine = True
    cell.number = 5
    cell.is_open = True
    assert bool(cell) == False, "функция bool() вернула неверное значение"

    try:
        cell.is_mine = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        cell.number = 10
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    p.init_pole()
    m = 0
    for row in p.pole:
        for x in row:
            assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
            if x.is_mine:
                m += 1

    assert m == 10, "на поле расставлено неверное количество мин"
    p.open_cell(0, 1)
    p.open_cell(9, 19)

    try:
        p.open_cell(10, 20)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    def count_mines(pole, i, j):
        n = 0
        for k in range(-1, 2):
            for l in range(-1, 2):
                ii, jj = k + i, l + j
                if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                    continue
                if pole[ii][jj].is_mine:
                    n += 1
        return n

    for i, row in enumerate(p.pole):
        for j, x in enumerate(row):
            if not p.pole[i][j].is_mine:
                m = count_mines(p.pole, i, j)
                assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"

    p.show_pole()
    print("Правильно, умница !!")
