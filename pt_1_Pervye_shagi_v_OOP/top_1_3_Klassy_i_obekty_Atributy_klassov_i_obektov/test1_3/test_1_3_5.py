# TEST-TASK___________________________________
def test_5(x):
    Car = x
    assert hasattr(Car, "model"), "В классе нет атрибута model"
    assert hasattr(Car, "color"), "В классе нет атрибута color"
    assert hasattr(Car, "number"), "В классе нет атрибута number"

    assert Car.model == "Тойота", "Значение атрибута неправильное"
    assert Car.color == "Розовый", "Значение атрибута неправильное"
    assert Car.number == "П111УУ77", "Значение атрибута неправильное"

    print("Правильно !")
