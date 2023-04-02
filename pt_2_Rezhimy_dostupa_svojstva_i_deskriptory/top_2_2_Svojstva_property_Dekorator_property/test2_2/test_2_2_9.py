# TEST-TASK___________________________________
def test_9(PathLines, LineTo):
    assert isinstance(PathLines, object), "Не создан класс PathLines"
    assert hasattr(PathLines, 'get_path'), "Объявите метод get_path"
    assert hasattr(PathLines, 'get_length'), "Объявите метод get_length"
    assert hasattr(PathLines, 'add_line'), "Объявите метод add_line"

    assert isinstance(LineTo, object), "Не создан класс LineTo"
    lineto = LineTo(0, 0)
    assert hasattr(lineto, 'x'), "В экземпляре класса LineTo нет атрибута x"
    assert hasattr(lineto, 'y'), "В экземпляре класса LineTo нет атрибута y"

    p = PathLines(LineTo(1, 2))
    assert p.get_length() == 2.23606797749979, "неверный вывод должно быть: 2.23606797749979"

    p.add_line(LineTo(10, 20))
    p.add_line(LineTo(5, 17))
    assert p.get_length() == 28.191631669843197, "неверный вывод должно быть: 28.191631669843197"

    m = p.get_path()
    assert all(isinstance(i, LineTo) for i in m) and len(m) == 3, "неверный вывод должно быть: True"

    h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
    assert h.get_length() == 71.8992593599813, "неверный вывод должно быть: 71.8992593599813"

    k = PathLines()
    assert k.get_length() == 0, "неверный вывод должно быть: 0"

    assert k.get_path() == [], "неверный вывод должно быть: [] (пустой список)"
    print("Правильный ответ !")
