# TEST-TASK___________________________________
def test_4(elements, Line, Rect, Ellipse):
    assert len(elements) == 217

    for e in elements:
        assert isinstance(e, Line) or isinstance(e, Rect) or isinstance(e, Ellipse), \
            "в списке elements должны быть только объекты классов Line, Rect, Ellipse"

    l = Line(1, 2, 3, 4)
    assert l.sp == (1, 2) and l.ep == (3, 4), "неверные значения в атрибутах sp, ep класса Line"

    for e in elements:
        if isinstance(e, Line):
            assert e.sp == (0, 0) and e.ep == (0, 0), "в объектах класса Line координаты должны быть равны нулю"

    print("Правильно !")
