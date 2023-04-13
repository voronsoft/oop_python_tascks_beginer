# TEST-TASK___________________________________
def test_8(BookStudy, lst_bs, unique_books):
    bs = BookStudy("Python", "Балакирев С.М.", 2020)
    assert hasattr(bs, "name") and hasattr(bs, "author") and hasattr(bs, "year"), "ошибка в атрибутах"
    assert type(bs.name) is str and bs.name == "Python", "значение атрибута name должно быть строкой"
    assert type(bs.author) is str and bs.author == "Балакирев С.М.", "значение атрибута author должно быть строкой"
    assert type(bs.year) is int and bs.year == 2020, "значение атрибута year должно быть целым числом"

    if bs.__class__.__eq__ is not object.__class__.__eq__ and bs.__class__.__hash__ == None:
        assert False, "вы не переопределили метод __hash__"

    assert bs.__class__.__eq__ is not object.__class__.__eq__, "вы не переопределили метод __eq__"

    assert len(lst_bs) == 5, "в списке lst_bs добавленны неправильное количество объектов"

    bs2 = BookStudy("Python", "Балакирев С.М.", 2020)

    assert bs.name == bs2.name and bs.author == bs2.author and hash(bs) - hash(bs2) == 0, "ошибка в методе hash"
    assert unique_books == len(set([hash(i) for i in lst_bs])), \
        "ошибка в подсчёте книг с уникальным хешем, стоит перепроверить метод __hash__"
    print("Правильное решение, так держать !")
