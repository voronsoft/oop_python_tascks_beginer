# TEST-TASK___________________________________
def test_9(Thing, Bag):
    x_thing = Thing("Книга по Python", 100)
    assert hasattr(x_thing, 'name') and hasattr(x_thing, 'weight'), "В классе не созданны локальные атрибуты"
    assert type(x_thing.name) is str, "Название должно быть строкой"
    assert type(x_thing.weight) is float or type(x_thing.weight) is int, "Вес должен быть числом"

    bag = Bag(1000)
    assert hasattr(bag, 'max_weight'), "Не создан атрибут max_weight"
    assert type(bag.max_weight) is int, "Максимальный суммарный вес вещей должен быть целым числом"
    assert '_Bag__things' in bag.__dict__, "Не создан локальный приватный атрибут __things"

    assert bag.things == [], "Нет доступа к локальному приватному атрибуту __things"
    assert type(bag.things) is list, "__things должен быть списком"
    assert len(bag.things) == 0, "__things изначально должен быть пустым"

    # проверка add_thing добавление вещей

    assert hasattr(bag, "add_thing"), "Не создан метод add_thing"
    assert bag.max_weight >= sum(_.weight for _ in bag.things), "Некоректно отработал метод add_thing"

    # проверка get_total_weight вес предметов в рюкзаке
    assert hasattr(bag, "get_total_weight"), "Не создан метод get_total_weight"
    bag.add_thing(Thing("Палатка", 500))
    assert bag.get_total_weight() == sum(_.weight for _ in bag.things), "Некоректно отработал метод get_total_weight"
    print("Умница правильный ответ !")
