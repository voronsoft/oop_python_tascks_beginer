# TEST-TASK___________________________________
def test_10(Box, Thing):
    b1 = Box()
    b2 = Box()
    assert hasattr(Box, "add_thing") and callable(b1.add_thing), "объявите метод add_thing"
    assert hasattr(Box, "get_things") and callable(b1.get_things), "объявите метод get_things"

    temp = Thing('мел', 100)
    temp2 = Thing('мел', 100)
    temp3 = Thing('мел', 101)
    assert hasattr(temp, "name"), "ошибка в объекте класса Thing - name"
    assert hasattr(temp, "mass"), "ошибка в объекте класса Thing - mass"
    assert type(temp.name) is str, "значение в name должно быть строкой"
    assert type(temp.mass) in (int, float), "значение в mass должно быть (int, float)"

    assert hasattr(temp, "__eq__"), "ошибка в объекте класса Thing отсутствует метод __eq__"
    assert temp == temp2, "ошибка в методе сравнения obj == obj1 (__eq__)"
    assert temp != temp3, "ошибка в методе сравнения obj != obj1"

    b1.add_thing(Thing('мел', 100))
    b1.add_thing(Thing('тряпка', 200))
    b1.add_thing(Thing('доска', 2000))
    #
    b2.add_thing(Thing('тряпка', 200))
    b2.add_thing(Thing('мел', 100))
    b2.add_thing(Thing('доска', 2000))

    assert hasattr(b2, "__eq__"), "ошибка в объекте класса Box отсутствует метод __eq__"
    assert b1 == b2, "ошибка при сравнении двух ящиков box1 == box2\n" \
                     "Ящики считаются равными, если одинаковы их содержимое\n" \
                     "(для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика)"

    b2.add_thing(Thing('доска', 2001))
    assert b1 != b2, "ошибка при сравнении двух ящиков box1 != box2"
    print("Правильный ответ )")
