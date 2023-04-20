# TEST-TASK___________________________________
def test_9(TableValues):
    tb = TableValues(3, 2)
    n = m = 0
    for row in tb:
        n += 1
        for value in row:
            m += 1
            assert type(
                    value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

    assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

    tb[0, 0] = 10
    assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

    try:
        tb[2, 0] = 5.2
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    try:
        a = tb[2, 4]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    print("Отличная работа !!")
