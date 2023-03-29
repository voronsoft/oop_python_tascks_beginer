# TEST-TASK___________________________________
def test_4(x):
    Goods = x
    assert hasattr(Goods, "title"), "В классе нет атрибута title"
    assert hasattr(Goods, "weight"), "В классе нет атрибута weight"
    assert hasattr(Goods, "tp"), "В классе нет атрибута tp"
    assert hasattr(Goods, "price"), "В классе нет атрибута price"
    assert hasattr(Goods, "inflation"), "В классе нет атрибута inflation"

    assert Goods.title == "Мороженое", "Значение атрибута неправильное"
    assert Goods.weight == 154, "Значение атрибута неправильное"
    assert Goods.tp == "Еда", "Значение атрибута неправильное"
    assert Goods.price == 2048, "Значение атрибута неправильное"
    assert Goods.inflation == 100, "Значение атрибута неправильное"
    print("Правильно !")
