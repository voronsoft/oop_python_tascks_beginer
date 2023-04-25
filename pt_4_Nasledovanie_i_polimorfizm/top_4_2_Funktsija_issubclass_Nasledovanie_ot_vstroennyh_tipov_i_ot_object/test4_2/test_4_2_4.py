# TEST-TASK___________________________________
def test_4(Thing, DictShop):
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)
    th_3 = Thing('Книга', 1500, 256)
    assert "name" in th_1.__dict__ and "price" in th_1.__dict__ and "weight" in th_1.__dict__, \
        "в экземпляре класса должны быть локальные атрибуты name, price, weight"

    assert type(th_1.name) is str, "значение name должно быть строкой"
    assert type(th_1.price) is float, "значение price должно быть вещественное число"
    assert type(th_1.weight) is float, "значение weight должно быть вещественное число"

    assert issubclass(DictShop, dict), "DictShop должен быть дочерним классом dict"

    dict_things = DictShop()
    assert dict_things == {} and len(
        dict_things) == 0, "при операции dict_things = DictShop() должен быть пустой словарь"

    try:
        dict_things["1"] = th_1
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError. Ключами могут быть только объекты класса Thing"

    try:
        dict_things[th_1] = th_1
        dict_things[th_2] = th_2
        dict_things[th_3] = th_3
    except:
        assert False, "возникла ошибка при добавлении в словарь ключей класса Thing"

    try:
        DictShop({'1': "sdf"})
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError. Ключами могут быть только объекты класса Thing"

    try:
        DictShop('things')
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError. Аргумент должен быть словарем"

    assert [_.name for _ in dict_things] == ['Лыжи', 'Книга', 'Книга'], \
        "при переборе объектов в словаре возникла ошибка"

    print("Правильно, приступайте к следующему заданию !")
