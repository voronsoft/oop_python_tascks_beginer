# TEST-TASK___________________________________
def test_2(Record):
    assert hasattr(Record, "__getitem__"), "необъявлен метод __getitem__"
    assert hasattr(Record, "__setitem__"), "необъявлен метод __setitem__"

    r = Record(pk=1, title='Python ООП', author='Балакирев')
    assert len(r.__dict__) == 3, "неверное сформировано количество атрибутов"
    assert hasattr(r, "pk") and hasattr(r, "title") and hasattr(r, "author"), \
        "в объекте неправильно формируются локальные атрибуты"

    assert r.pk == 1 and r.title == "Python ООП" and r.author == "Балакирев", "ошибка атрибутам присвоены неверные значения"

    assert r[0] == 1 and r[1] == "Python ООП" and r[2] == "Балакирев", "ошибка при доступе методом - obj[0]"

    temp = Record(pk=1, title='Python ООП', author='Балакирев')
    temp[0] = 1000
    temp[2] = "ssss"
    assert temp.__dict__["pk"] == 1000 and temp.__dict__[
        "author"] == "ssss", "ошибка при записи методом - obj[0] = 1111"

    try:
        r[3]
        r[2.5]
        r['ee']
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка - IndexError"

    print("Правильно, кстати это еще не сложная задача")
