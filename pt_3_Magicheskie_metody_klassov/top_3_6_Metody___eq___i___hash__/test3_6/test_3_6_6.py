# TEST-TASK___________________________________
def test_6(ShopItem, lst_in, shop_items):
    it1 = ShopItem('name', 10, 11)
    it2 = ShopItem('name', 10, 11)
    assert hash(it1) == hash(it2), "1разные хеши у равных объектов"
    #
    it2 = ShopItem('name', 10, 12)
    assert hash(it1) != hash(it2), "2равные хеши у разных объектов"
    #
    it2 = ShopItem('name', 11, 11)
    assert hash(it1) != hash(it2), "3равные хеши у разных объектов"
    #
    it2 = ShopItem('NAME', 10, 11)
    assert hash(it1) == hash(it2), "4разные хеши у равных объектов"
    #
    name = lst_in[0].split(':')
    for sp in shop_items.values():
        assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, \
            "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"
    #
    v = list(shop_items.values())
    if v[0][0].name.strip() == "Системный блок":
        assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"
    #
    if v[0][0].name.strip() == "X-box":
        assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"
    print("Правильный ответ ))")
