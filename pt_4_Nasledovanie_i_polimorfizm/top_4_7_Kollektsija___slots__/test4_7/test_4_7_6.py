# TEST-TASK___________________________________
def test_6(Star, WhiteDwarf, YellowDwarf, RedGiant, Pulsar, stars, white_dwarfs):
    temp = Star('Альдебаран', 5, 3600)
    assert "__slots__" in dir(temp), "не найден __slots__"

    assert temp.__slots__ == ['_name', '_massa', '_temp'], \
        "в базовом классе должы быть только атрибуты '_name', '_massa', '_temp'"

    try:
        temp.__dict__
    except AttributeError:
        assert True
    else:
        assert False, "__doct__ должен отсутствовать при объявлении __slots__"

    assert issubclass(WhiteDwarf, Star), "WhiteDwarf, должен быть подклассом класса Star"
    assert issubclass(YellowDwarf, Star), "YellowDwarf, должен быть подклассом классаStar"
    assert issubclass(RedGiant, Star), "RedGiant, должен быть подклассом класса Star"
    assert issubclass(Pulsar, Star), "Pulsar, должен быть подклассом класса Star"

    assert WhiteDwarf.__slots__ == ['_type_star', '_radius'] and "__slots__" in WhiteDwarf.__dict__, \
        "WhiteDwarf не найдена коллекция __slots__"

    assert YellowDwarf.__slots__ == ['_type_star', '_radius'] and "__slots__" in YellowDwarf.__dict__, \
        "YellowDwarf не найдена коллекция __slots__"

    assert RedGiant.__slots__ == ['_type_star', '_radius'] and "__slots__" in RedGiant.__dict__, \
        "RedGiant не найдена коллекция __slots__"

    assert Pulsar.__slots__ == ['_type_star', '_radius'] and "__slots__" in Pulsar.__dict__, \
        "Pulsar не найдена коллекция __slots__"

    assert len(stars) == 4 and type(stars) is list, "не найден список stars "

    assert len(white_dwarfs) == 2 and all(True if isinstance(_, WhiteDwarf) else False for _ in white_dwarfs), \
        "в списке white_dwarfs должны быть обекты класса WhiteDwarf"

    print("Правильно, еще чуть-чуть остлось до конца главы! 6")
