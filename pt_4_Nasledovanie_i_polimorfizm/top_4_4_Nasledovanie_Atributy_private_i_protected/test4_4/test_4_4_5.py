# TEST-TASK___________________________________
def test_5(Animal, animals):
    temp = Animal('Васька', 'дворовый кот', 5)
    assert '_Animal__name' in temp.__dict__ and \
           '_Animal__kind' in temp.__dict__ and \
           '_Animal__old' in temp.__dict__, \
        "в экземпляре класса Animal должны быть 3 приватных локальных атрибута __name, __kind, __old"

    assert type(temp.__dict__['_Animal__name']) is str, "ошибка значение __name должно быть строкой"
    assert type(temp.__dict__['_Animal__kind']) is str, "ошибка значение __kind должно быть строкой"
    assert type(temp.__dict__['_Animal__old']) is int, "ошибка значение __old должно быть целым числом"

    assert type(Animal.name) == property and \
           type(Animal.kind) == property and \
           type(Animal.old) == property, "класс Animal должен содержать объекты-свойства name, kind, old"

    try:
        assert len(animals) == 3
        assert type(animals) is list
    except:
        assert False, "необходимо создать список animals"
    else:
        assert True

    assert animals[0].name == "Васька" and animals[0].old == 5 and animals[0].kind == 'дворовый кот', \
        "ошибка при попытке прочитать значение из приватных атрибутов"
    try:
        animals[0].name = "не васька"
        assert animals[0].name == "не васька"

        animals[0].kind = "домашний"
        assert animals[0].kind == "домашний"

        animals[0].old = 15
        assert animals[0].old == 15
    except:
        assert False, "при попытке записать(изменить) значение в приватном локальном атрибуте возникла ошибка"
    else:
        assert True

    print("Верно. Так держать!")
