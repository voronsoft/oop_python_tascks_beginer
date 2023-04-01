# TEST-TASK___________________________________
def test_8(rect, Rectangle, Point):
    assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and \
           hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

    r = Rectangle(1, 2.6, 3.3, 4)
    r.set_coords(Point(1, 2), Point(3, 4))
    sp, ep = r.get_coords()
    a, b = sp.get_coords()
    c, d = ep.get_coords()
    assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

    r = Rectangle(Point(1, 2), Point(3, 4))
    sp, ep = r.get_coords()
    a, b = sp.get_coords()
    c, d = ep.get_coords()
    assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

    assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), \
        "атрибуты __sp и __ep должны ссылаться на объекты класса Point"
    print('Правильно )))) гы')
