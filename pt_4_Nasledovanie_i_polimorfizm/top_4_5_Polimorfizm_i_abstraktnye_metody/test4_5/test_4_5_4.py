# TEST-TASK___________________________________
def test_4(ShopItem, ShopInterface):
    assert issubclass(ShopInterface, object), "объявите базовый класс ShopInterface"
    assert "get_id" in dir(ShopInterface), "не найден метод get_id в абстрактном классе ShopInterface"

    try:
        x = ShopInterface()
        x.get_id()
    except NotImplementedError:
        assert True
    else:
        assert False, "метод get_id() не сгенерировал ошибку NotImplementedError"

    assert issubclass(ShopItem, ShopInterface), "ShopItem должен быть подклассом класса ShopInterface"

    sh1 = ShopItem('имя', 0.10, 100)
    assert "_name" in sh1.__dict__ and "_weight" in sh1.__dict__ and "_price" in sh1.__dict__, \
        "в экземпляре класса ShopItem ошибка локальных атрибутов _name, _weight, _price"

    assert type(sh1._name) is str, "название товара (строка)"
    assert type(sh1._weight) in (int, float) and sh1._weight > 0, "вес товара (любое положительное число)"
    assert type(sh1._price) in (int, float) and sh1._price > 0, "цена товара (любое положительное число)"

    assert "_ShopItem__id" in sh1.__dict__, "в экземплярах класса не найден приватный атрибут __id"
    temp1 = [k._ShopItem__id for k in [ShopItem('test', 0.10, 100) for _ in range(5)]]
    assert len(temp1) == 5 and len(set(temp1)) == 5, "__id должен быть уникальным в каждом экземпляре класса"

    # В классе ShopItem необходимо переопределить метод get_id() базового класса так,
    # чтобы он (метод) возвращал значение атрибута __id.
    assert ShopItem.get_id != ShopInterface.get_id, "в дочернем классе необходимо переопределить метод get_id"

    assert sh1.get_id() == sh1._ShopItem__id, "метод get_id работает не корректно"

    print("Правильный ответ !!")
