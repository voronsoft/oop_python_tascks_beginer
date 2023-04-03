# TEST-TASK___________________________________
def test_8(Circle):
    assert type(Circle.x) == property and type(Circle.y) == property and \
           type(Circle.radius) == property, "в классе Circle должны быть объявлены объекты-свойства x, y и radius"

    try:
        cr = Circle(20, '7', 22)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при инициализации объекта с недопустимыми аргументами"

    cr = Circle(20, 7, 22)
    assert cr.x == 20 and cr.y == 7 and cr.radius == 22, "объекты-свойства x, y и radius вернули неверные значения"

    cr.radius = -10  # Прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
    assert cr.radius == 22, "при присваивании некорректного значения, прежнее значение изменилось"

    x, y = cr.x, cr.y
    assert x == 20 and y == 7, "объекты-свойства x, y вернули некорректные значения"
    assert cr.name == False, "при обращении к несуществующему атрибуту должно возвращаться значение False"

    try:
        cr.x = '20'
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    cr.y = 7.8
    cr.radius = 10.6
    print("Правильно, отлично !!")
