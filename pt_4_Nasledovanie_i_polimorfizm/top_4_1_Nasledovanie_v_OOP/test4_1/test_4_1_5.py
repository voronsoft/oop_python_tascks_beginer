# TEST-TASK___________________________________
def test_5(Table, Thing, ElBook):
    assert issubclass(Table, Thing), "ошибка, Table должен быть дочерним классом от Thing"
    assert issubclass(ElBook, Thing), "ошибка, ElBook должен быть дочерним классом от Thing"

    th1 = Thing('Phone1', 20)
    th2 = Thing('Phone2', 20)
    th3 = Thing('Phone3', 20)
    assert hasattr(th1, "id"), "отсутствует атрибут id"
    assert hasattr(th1, "name"), "отсутствует атрибут name"
    assert hasattr(th1, "price"), "отсутствует атрибут price"
    assert hasattr(th1, "weight"), "отсутствует атрибут weight"
    assert hasattr(th1, "dims"), "отсутствует атрибут dims"
    assert hasattr(th1, "memory"), "отсутствует атрибут memory"
    assert hasattr(th1, "frm"), "отсутствует атрибут frm"
    assert th1.name == "Phone1" and type(th1.name) is str, "ошибка, неправильное значение в атрибуте"
    assert th1.price == 20.0 and type(th1.price) is float, "ошибка, неправильное значение в атрибуте"
    assert type(th1.id) is int, "ошибка, неправильное значение в атрибуте"
    # Наконец, в базовом классе Thing объявите метод:
    # get_data() - для получения кортежа в формате (id, name, price, weight, dims, memory, frm)
    assert hasattr(Thing, "get_data") and callable(Thing.get_data), "ошибка, в классе Thing необъявлен метод get_data()"
    assert th1.get_data() == (1, 'Phone1', 20.0, None, None, None, None), "ошибка, метод get_data работает некорректно"

    table1 = Table('Стол1', 250, 20.5, (1.0, 0.6, 0.4))
    table2 = Table('Стол2', 250, 20.5, (1.0, 0.6, 0.4))
    table3 = Table('Стол3', 250, 20.5, (1.0, 0.6, 0.4))
    assert hasattr(table1, "id"), "отсутствует атрибут id"
    assert hasattr(table1, "name"), "отсутствует атрибут name"
    assert hasattr(table1, "price"), "отсутствует атрибут price"
    assert hasattr(table1, "weight"), "отсутствует атрибут weight"
    assert hasattr(table1, "dims"), "отсутствует атрибут dims"
    assert hasattr(table1, "memory"), "отсутствует атрибут memory"
    assert hasattr(table1, "frm"), "отсутствует атрибут frm"
    assert table1.name == 'Стол1' and type(table1.name) is str, "ошибка, неправильное значение в атрибуте"
    assert table1.price == 250.0 and type(table1.price) is float, "ошибка, неправильное значение в атрибуте"
    assert type(th1.id) is int, "ошибка, неправильное значение в атрибуте"
    assert table1.weight == 20.5 and type(table1.weight) is float, "ошибка, неправильное значение в атрибуте"
    assert table1.dims == (1.0, 0.6, 0.4) and len(table1.dims) == 3, "ошибка, неправильное значение в атрибуте"
    assert table1.frm is None and table1.memory is None, \
        "ошибка неиспользуемые локальные атрибуты должны иметь значение None"
    assert table1.get_data() == (4, 'Стол1', 250.0, 20.5, (1.0, 0.6, 0.4), None, None), \
        "ошибка, метод get_data работает некорректно"

    book1 = ElBook('Книга1', 115.3, 200, 'txt')
    book2 = ElBook('Книга2', 115.3, 200, 'txt')
    book3 = ElBook('Книга3', 115.3, 200, 'txt')
    assert hasattr(book1, "id"), "отсутствует атрибут id"
    assert hasattr(book1, "name"), "отсутствует атрибут name"
    assert hasattr(book1, "price"), "отсутствует атрибут price"
    assert hasattr(book1, "weight"), "отсутствует атрибут weight"
    assert hasattr(book1, "dims"), "отсутствует атрибут dims"
    assert hasattr(book1, "memory"), "отсутствует атрибут memory"
    assert hasattr(book1, "frm"), "отсутствует атрибут frm"
    assert book1.name == 'Книга1' and type(book1.name) is str, "ошибка, неправильное значение в атрибуте"
    assert book1.price == 115.3 and type(book1.price) is float, "ошибка, неправильное значение в атрибуте"
    assert type(book1.id) is int, "ошибка, неправильное значение в атрибуте"
    assert book1.weight is None, "ошибка, неиспользуемое значение должно быть None"
    assert book1.dims is None, "ошибка, неиспользуемое значение должно быть None"
    assert book1.frm == 'txt' and type(book1.frm) is str, "ошибка, неправильное значение в атрибуте"
    assert book1.get_data() == (7, 'Книга1', 115.3, None, None, 200, 'txt'), \
        "ошибка, метод get_data работает некорректно"

    lst = [th1.id, th2.id, th3.id, book1.id, book2.id, book3.id, table1.id, table2.id, table3.id]
    assert len(lst) == len(set(lst)), "ошибка, id должны быть уникальными"
    print("Правильное решение )")
