# TEST-TASK___________________________________
def test_10(Food, BreadFood, SoupFood, FishFood):
    assert issubclass(Food, object), "объявите базовый класс Food"
    test = Food("имя", "1.1", "10")
    assert hasattr(test, "_name") and hasattr(test, "_weight") and hasattr(test, "_calories"), "ошибка в атрибутах "

    # bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
    # sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
    # ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
    assert issubclass(BreadFood, Food), "BreadFood, должен быть дочерним классом класса Food"
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)  # white - True для белого хлеба, False - для остальных
    assert hasattr(bf, "_name") and type(bf._name) is str, "ошибка значения в атрибуте _name не тот тип данных"
    assert hasattr(bf, "_weight") and type(bf._weight) in (int, float) and bf._weight > 0, \
        "ошибка значения в атрибуте _weight"
    assert hasattr(bf, "_calories") and type(bf._calories) is int and bf._calories > 0, \
        "ошибка значения в атрибуте _calories"
    assert hasattr(bf, "_white") and type(bf._white) is bool, \
        "ошибка значения в атрибуте _white"

    sf = SoupFood("Черепаший суп", 520, 890.5, False)
    assert issubclass(SoupFood, Food), "SoupFood, должен быть дочерним классом класса Food"
    assert hasattr(sf, "_dietary") and type(sf._dietary) is bool, "ошибка значения в атрибуте _dietary"

    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
    assert issubclass(FishFood, Food), "FishFood, должен быть дочерним классом класса Food"
    assert hasattr(ff, "_fish") and ff._fish in ("семга", "окунь", "сардина"), "ошибка значения в атрибуте "

    print("Хорошие новости, верно!")
