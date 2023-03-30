# TEST-TASK___________________________________
def test_3(Point, points):
    p1 = Point(10, 20)
    p2 = Point(12, 5, 'red')
    assert isinstance(p1, Point), "p1 не создан"
    assert isinstance(p2, Point), "p2 не создан"

    assert hasattr(p1, 'x') and hasattr(p1, "y") and hasattr(p1, "color"), "В объекте должно быть 3 атрибута"
    assert p1.color == "black", "color по умолчанию должен принимать значение black"
    assert len(points) == 1000, "длина points не равна 1000"
    assert points[1].color == 'yellow', "ошибка, для второго объекта в списке points укажите цвет 'yellow'"
    assert points[10].x - points[11].x == -2, "ошибка, в каждом следующем объекте x и y должны увеличиваться на 2 !!"
    print("Правильно !!")
