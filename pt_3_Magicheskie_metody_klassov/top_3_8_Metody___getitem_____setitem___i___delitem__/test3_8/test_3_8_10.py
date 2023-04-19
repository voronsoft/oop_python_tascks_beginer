# TEST-TASK___________________________________
def test_10(SparseTable, Cell):
    st = SparseTable()
    st.add_data(2, 5, Cell(25))
    st.add_data(1, 1, Cell(11))
    assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

    try:
        v = st[3, 2]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    st[3, 2] = 100
    assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
    assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

    st.remove_data(1, 1)
    try:
        v = st[1, 1]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        st.remove_data(1, 1)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    d = Cell('5')
    assert d.value == '5', \
        "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"
    print("Правильно.")
