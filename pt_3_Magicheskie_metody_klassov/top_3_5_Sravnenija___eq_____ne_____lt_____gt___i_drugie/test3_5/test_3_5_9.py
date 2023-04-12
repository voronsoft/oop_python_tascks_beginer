# TEST-TASK___________________________________
def test_9(Body):
    a = Body('Lora', 10, 10)
    b = Body('Dora', 20, 20)
    assert hasattr(a, "name") and hasattr(a, "ro") and hasattr(a, "volume"), "ошибка в локальных атрибутах"
    assert type(a.name) is str, "name может быть только строкой"
    assert type(a.ro) in (int, float), "ro  должно быть int или float"
    assert type(a.volume) in (int, float), "volume  должно быть int или float"
    assert not a > b, "ошибка при сравнении объектов >"
    assert a < b, "ошибка при сравнении объектов <"
    assert 10 < a, "ошибка при сравнении число < объект"
    assert not 10 > a, "ошибка при сравнении число > объект"
    assert not a == 5, "ошибка при сравнении объект == число"
    assert a != 5, "ошибка при сравнении объект != число"
    print("Правильное решение.")
