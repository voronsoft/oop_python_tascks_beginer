# TEST-TASK___________________________________
def test_4(Person, persons):
    assert '__slots__' in Person.__dict__, "в классе не определён __slots__"
    assert all(True if _ in Person.__dict__['__slots__'] else False for _ in ['_fio', '_old', '_job']), \
        "в коллекции __slots__ ошибка локальный атрибутов"

    assert len(persons) == 4 and type(persons) is list, "ошибка в persons"
    print("Правильное решение ! 4")
