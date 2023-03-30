# TEST-TASK___________________________________
def test_9(DataBase, lst_in):
    db = DataBase()
    assert hasattr(DataBase, 'FIELDS')
    assert hasattr(DataBase, 'lst_data')
    assert hasattr(DataBase, "select"), 'не определен метод- select'
    assert hasattr(DataBase, "insert"), 'не определён метод - insert'

    db.insert(lst_in)
    assert type(db.lst_data[0]) == dict, "Данные в списке lst_data должны быть словарями"
    assert db.lst_data == [{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}, \
                           {'id': '2', 'name': 'Федор', 'old': '23', 'salary': '12000'}, \
                           {'id': '3', 'name': 'Иван', 'old': '13', 'salary': '1200'}], \
        "ошибка в методе - insert"

    # доделать тесты !!!
    res1 = db.select(0, 50)

    lstgfghj8gh9jg2 = []
    for d in lst_in:
        lstgfghj8gh9jg2.append(dict(zip(DataBase.FIELDS, d.split())))

    assert res1 == lstgfghj8gh9jg2, "метод select вернул неверные данные"

    res2 = db.select(0, 1)
    assert res2 == lstgfghj8gh9jg2[0:2], \
        "некорректно работает метод select \n" \
        "Условие - select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне[a; b]\n" \
        "(включительно) по их индексам (не id, а индексам списка)"

    print("Правильно !")
