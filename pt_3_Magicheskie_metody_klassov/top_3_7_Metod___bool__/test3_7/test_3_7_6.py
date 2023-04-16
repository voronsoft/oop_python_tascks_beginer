# TEST-TASK___________________________________
def test_6(Line):
    # TEST
    line = Line(0, -2, 0, 1.0)
    assert hasattr(line, "x1") and hasattr(line, "x2") and hasattr(line, "y1") and hasattr(line, "y2"), \
        "ошибка в локальных атрибутах"

    assert type(line.x1) in (int, float) and type(line.x2) in (int, float) and type(line.y1) in (int, float) and type(
            line.y2) in (int, float), \
        "тип значений в локальных атрибутах может быть только int или float"
    assert hasattr(line, "__len__"), "метод __len__ не объявлен"

    from math import sqrt

    temp = sqrt((line.x1 - line.x2) ** 2 + (line.y1 - line.y2) ** 2) > 1

    assert temp == bool(line), "ошибка при операции bool(line), вернулся некорректный ответ" \
                               "перепишите логику метода __len__"

    if hasattr(line, "__bool__"):
        assert False, "эту задачу желательно решить без объявления метода __bool__"

    print("Правильное решение )!")
