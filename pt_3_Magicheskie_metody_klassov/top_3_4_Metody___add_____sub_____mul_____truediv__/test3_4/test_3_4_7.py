# TEST-TASK___________________________________
def test_7(Lib, Book):
    lib = Lib()
    assert 'book_list' in lib.__dict__, "список книг должен быть изначально пустым"

    book = Book('Парус', 'Чаплин', 100)
    assert hasattr(book, "title") and hasattr(book, "author") and hasattr(book, "year"), "ошибка локальных атрибутов"

    b = Book('Гайка', 'Делон', 200)
    c = Book('Ключ', 'Закия', 300)

    lib = lib + book
    assert len(lib.book_list) == 1, "при сложении библиотеки и книги произошла ошибка"

    lib += book
    assert len(lib.book_list) == 2, "при добавлении книги в библиотеку произошла ошибка"

    lib = lib + b
    lib = lib + c
    lib = lib - 2  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
    assert len(lib.book_list) == 3, "при удалении книги по номеру из библиотеки произошла ошибка"
    lib = lib - book
    lib -= book
    assert len(lib.book_list) == 1 and book in lib.book_list, "при удалении по ранее добавленной книге произошла ошибка"

    assert len(lib) == 1, "метод len() работает некорректно"
    lib -= book
    assert len(lib) == 0, "метод len() работает некорректно"

    # При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

    print("Правильный ответ !")
