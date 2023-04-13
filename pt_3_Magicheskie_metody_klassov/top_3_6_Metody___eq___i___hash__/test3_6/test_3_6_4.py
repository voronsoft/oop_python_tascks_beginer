# TEST-TASK___________________________________
def test_4(Rect):
    r1 = Rect(10, 5, 100, 50)
    r2 = Rect(-10, 4, 100, 50)
    assert r1.__dict__ == {'x': 10, 'y': 5, 'width': 100, 'height': 50}, "ошибка атрибутов"
    assert r2.__dict__ == {'x': -10, 'y': 4, 'width': 100, 'height': 50}, "ошибка атрибутов"

    if r1.__class__.__eq__ is not object.__class__.__eq__ and r1.__class__.__hash__ == None:
        assert False, "вы не переопределили метод __hash__"

    assert r1.__class__.__eq__ is not object.__class__.__eq__, "вы не переопределили метод __eq__"

    # хэши объектов класса Rect с равными width, height были равны.
    assert r1.width == r2.width and r1.height == r2.height and hash(r1) == hash(r2), \
        "ошибка, у двух объектов одинаковые width и height, но хеш разный"

    print("Правильный ответ, хеш одинаковый потому что величины у двух объектов имеют равные значения")
