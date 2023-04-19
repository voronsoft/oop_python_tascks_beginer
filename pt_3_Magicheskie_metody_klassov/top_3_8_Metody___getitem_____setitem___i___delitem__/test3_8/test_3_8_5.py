# TEST-TASK___________________________________
def test_5(TableValues, CellInteger):
    tb = TableValues(3, 2, cell=CellInteger)
    tb[0, 0] = 1
    assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

    try:
        tb[2, 1] = 1.5
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    for row in tb.cells:
        for x in row:
            assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

    cell = CellInteger(10)
    assert cell.value == 10, "дескриптор value вернул неверное значение"
    print("Правильный ответ ))")
