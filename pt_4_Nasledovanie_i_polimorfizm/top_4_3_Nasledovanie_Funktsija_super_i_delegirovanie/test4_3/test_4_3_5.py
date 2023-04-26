# TEST-TASK___________________________________
def test_5(SellItem, House, Flat, Land, Agency):
    item = SellItem("flower", 12345.5)
    assert issubclass(SellItem, object), "создайте базовый класс SellItem"
    assert "name" in item.__dict__ and "price" in item.__dict__, "ошибка локальных атрибутов в базовом классе"
    assert type(item.name) is str, "атрибут name должен быть строкой"
    assert type(item.price) in (int, float), "атрибут price должен быть int или float"

    assert issubclass(House, SellItem), "House, должен быть потомком SellItem"
    assert issubclass(Flat, SellItem), "Flat, должен быть потомком SellItem"
    assert issubclass(Land, SellItem), "Land, должен быть потомком SellItem"
    assert issubclass(Agency, object), "создайте класс Agency"

    house = House('дом, кирпичный', price=35000000, material='кирпич', square=186.5)
    assert isinstance(house, SellItem), "ошибка в наследовании"
    assert len(house.__dict__) == 4 and type(house.name) is str and house.name == 'дом, кирпичный', \
        "ошибка в атрибуте name"
    assert type(house.price) in (int, float) and house.price == 35000000, "ошибка в атрибуте price"
    assert type(house.material) is str and house.material == "кирпич", "ошибка в атрибуте material"
    assert type(house.square) is float and house.square == 186.5, "ошибка в атрибуте square"

    flat = Flat("квартира, 3к", 10000000, 121.5, 3)
    assert isinstance(flat, SellItem), "ошибка в наследовании"
    assert len(flat.__dict__) == 4 and type(flat.name) is str and flat.name == 'квартира, 3к', "ошибка в атрибуте name"
    assert type(flat.price) in (int, float) and flat.price == 10000000, "ошибка в атрибуте price"
    assert type(flat.rooms) is int and flat.rooms == 3, "ошибка в атрибуте material"
    assert type(flat.size) is float and flat.size == 121.5, "ошибка в атрибуте size"

    land = Land("участок под застройку", 3000000, 6.74)
    assert isinstance(land, SellItem), "ошибка в наследовании"
    assert len(land.__dict__) == 3 and type(
        land.name) is str and land.name == 'участок под застройку', "ошибка в атрибуте name"
    assert type(land.price) in (int, float) and land.price == 3000000, "ошибка в атрибуте price"
    assert type(land.square) is float and land.square == 6.74, "ошибка в атрибуте square"

    ag = Agency("Рога и копыта")
    assert ag.name == "Рога и копыта" and type(ag.name) is str, "ошибка в атрибуте square класса Agency"
    assert hasattr(ag, 'add_object') and callable(ag.add_object), "не объявлен метод add_object"
    assert hasattr(ag, 'get_objects') and callable(ag.get_objects), "не объявлен метод get_objects"
    assert hasattr(ag, 'remove_object') and callable(ag.remove_object), "не объявлен метод remove_object"

    try:
        ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
        ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
        ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
        ag.add_object(House("дом, кирпичный", price=35000000, material="кирпич", square=186.5))
        ag.add_object(Land("участок под застройку", 3000000, 6.74))
    except:
        assert False, "некорректно работает метод add_object"
    else:
        assert True

    try:
        temp = [obj.name for obj in ag.get_objects()]
    except:
        assert False, "некорректно работает метод get_objects"
    else:
        assert temp == ['квартира, 3к', 'квартира, 2к', 'квартира, 1к', 'дом, кирпичный', 'участок под застройку'], \
            "некорректно работает метод get_objects"

    assert len(
        [x for x in ag.get_objects() if isinstance(x, House)]) == 1 and "ошибка, при выделение списка домов House"
    assert len([x for x in ag.get_objects() if isinstance(x, Flat)]) == 3, "ошибка, при выделение списка квартир Flat"
    assert len([x for x in ag.get_objects() if isinstance(x, Land)]) == 1, "ошибка, при выделение списка квартир Land"

    print("Правильный ответ, так держать!")
