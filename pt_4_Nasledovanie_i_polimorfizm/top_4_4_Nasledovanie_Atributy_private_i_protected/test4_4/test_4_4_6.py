# TEST-TASK___________________________________
def test_6(Furniture, Closet, Chair, Table):
    # # TEST
    f = Furniture('Стол', 1.0)
    assert hasattr(f, "_name") and hasattr(f, "_weight"), "в экземпляре класса должны быть атрибуты _name и _weight"
    assert "_Furniture__verify_name" in dir(Furniture), "ошибка, необходимо объявить приватный метод __verify_name"
    assert "_Furniture__verify_weight" in dir(Furniture), "ошибка, необходимо объявить приватный метод __verify_weight"

    try:
        f._Furniture__verify_name(1)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError при проверке типа методом __verify_name"

    try:
        f._Furniture__verify_weight(0)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError при проверке типа методом __verify_weight"

    try:
        f._name = 2
    except TypeError:
        assert True
    else:
        assert False, "TypeError не работает проверка записи некорректного значения в переменную _name"

    try:
        f._weight = -1
    except TypeError:
        assert True
    else:
        assert False, "TypeError не работает проверка записи некорректного значения в переменную _weight"

    try:
        temp = Furniture(1, 1.0)
    except TypeError:
        assert True
    else:
        assert False, "при создании экземпляра класса с некорректными значениями не сгенерировалась ошибка TypeError"

    try:
        temp = Furniture("Стол ", 0)
    except TypeError:
        assert True
    else:
        assert False, "при создании экземпляра класса с некорректными значениями не сгенерировалась ошибка TypeError"

    # На основе базового класса Furniture объявить следующие дочерние классы:
    # Closet - для представления шкафов;
    # Chair - для представления стульев;
    # Table - для представления столов.
    assert issubclass(Closet, Furniture), "Closet должен быть подклассом класса Furniture"
    assert issubclass(Chair, Furniture), "Chair должен быть подклассом класса Furniture"
    assert issubclass(Table, Furniture), "Table должен быть подклассом класса Furniture"

    closet = Closet('шкаф-купе', 342.56, True, 3)
    assert '_name' in closet.__dict__ and \
           '_weight' in closet.__dict__ and \
           '_tp' in closet.__dict__ and type(closet._tp) is bool and \
           '_doors' in closet.__dict__ and type(closet._doors) is int, \
        "ошибка в атрибутах экз класса Closet. Проверьте названия и типы"

    chair = Chair('стул', 14, 55.6)
    assert '_name' in chair.__dict__ and \
           '_weight' in chair.__dict__ and \
           '_height' in chair.__dict__ and type(chair._height) in (int, float) and chair._height > 0, \
        "ошибка в атрибутах экз класса Chair. Проверьте названия и типы"

    table = Table('стол', 34.5, 75, 10)
    assert '_name' in table.__dict__ and \
           '_weight' in table.__dict__ and \
           '_height' in table.__dict__ and \
           '_square' in table.__dict__ and type(table._square) in (int, float) and table._square > 0, \
        "ошибка в атрибутах экз класса Chair. Проверьте названия и типы"

    assert hasattr(Closet, "get_attrs") and callable(Closet.get_attrs), "в классе не найден метод get_attrs()"
    assert hasattr(Chair, "get_attrs") and callable(Chair.get_attrs), "в классе не найден метод get_attrs()"
    assert hasattr(Table, "get_attrs") and callable(Table.get_attrs), "в классе не найден метод get_attrs()"

    assert closet.get_attrs() == ('шкаф-купе', 342.56, True, 3), "метод get_attrs() работает некорректно"
    assert chair.get_attrs() == ('стул', 14, 55.6), "метод get_attrs() работает некорректно"
    assert table.get_attrs() == ('стол', 34.5, 75, 10), "метод get_attrs() работает некорректно"

    print("Верно. Так держать!")
