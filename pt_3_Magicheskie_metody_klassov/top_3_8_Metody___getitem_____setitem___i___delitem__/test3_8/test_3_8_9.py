# TEST-TASK___________________________________
def test_9(Bag, Thing):
    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))

    try:
        b.add_thing(Thing('рубашка', 500))
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    assert b[0].name == 'книга' and b[0].weight == 100, \
        "атрибуты name и weight объекта класса Thing принимают неверные значения"

    t = Thing('Python', 20)
    b[1] = t
    assert b[1].name == 'Python' and b[1].weight == 20, \
        "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

    del b[0]
    assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

    try:
        t = b[2]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))

    b[0] = Thing('рубашка', 500)

    try:
        b[0] = Thing('рубашка', 800)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
    print("Правильный ответ")
