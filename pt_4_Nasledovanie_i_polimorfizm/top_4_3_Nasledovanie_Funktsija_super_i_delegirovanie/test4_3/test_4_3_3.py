# TEST-TASK___________________________________
def test_3(DigitBook, Book):
    assert issubclass(DigitBook, Book), "DigitBook должен унаследовать все от Book"

    try:
        obj = DigitBook('Title', 'Norov', 155, 1977, 1333, 'doc')
    except:
        assert False, "при создании экземпляра класса возникла ошибка"

    assert 'title' in obj.__dict__ and type(obj.title) is str and \
           'author' in obj.__dict__ and type(obj.author) is str and \
           'pages' in obj.__dict__ and type(obj.pages) is int and \
           'year' in obj.__dict__ and type(obj.year) is int and \
           'size' in obj.__dict__ and type(obj.size) is int and \
           'frm' in obj.__dict__ and type(obj.frm) is str, "ошибка локальных атрибутов"

    try:
        obj_book = Book('Title', 'Norov', 155, 1977, 1333, 'doc')
    except:
        assert True
    else:
        assert False, "ошибка при создании экземпляра класса Book"

    try:
        obj_book = Book('Title', 'Norov', 155, 1977)
    except:
        assert False, "ошибка при создании экземпляра класса Book"
    else:
        assert True

    assert len(obj.__dict__) == 6, "в дочернем классе должны быть 2 дополнительных атрибута: size, frm"
    assert len(obj_book.__dict__) == 4, "в родительском классе должны быть только атрибуты: title, author, pages, year"

    print("Правильное решение !!")
