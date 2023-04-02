# TEST-TASK___________________________________
def test_6(Cell, table, TableSheet):
    a = Cell()

    assert isinstance(table, TableSheet)
    assert len(table.cells) == 5 and len(table.cells[0]) == 3

    assert type(table.cells) == list

    res = [int(x.value) for row in table.cells for x in row]
    assert res == list(range(1, 16))

    table.cells[0][0].value = 1.0
    x = table.cells[1][0].value

    try:
        table.cells[0][0].value = 'a'
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"
    print("Правильно !")
