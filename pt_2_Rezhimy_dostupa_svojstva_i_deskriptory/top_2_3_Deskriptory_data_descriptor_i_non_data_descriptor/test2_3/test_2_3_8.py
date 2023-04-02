# TEST-TASK___________________________________
def test_8(SuperShop, Product):
    shop = SuperShop("У Балакирева")
    shop.add_product(Product("name", 100))
    shop.add_product(Product("name", 100))
    assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

    for p in shop.goods:
        assert p.price == 100, "дескриптор price вернул неверное значение"
        assert p.name == "name", "дескриптор name вернул неверное значение"

    t = Product("name 123", 1000)
    shop.add_product(t)
    shop.remove_product(t)
    assert len(
        shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

    assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

    t = Product(1000, "name 123")
    if hasattr(t, '_name'):
        assert type(t.name) == str, "типы поля name должнен быть str"
    if hasattr(t, '_price'):
        assert type(t.price) in (int, float), "тип поля price должнен быть int или float"
    print("Правильно !")
