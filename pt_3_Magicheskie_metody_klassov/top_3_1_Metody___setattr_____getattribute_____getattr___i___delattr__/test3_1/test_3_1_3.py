# TEST-TASK___________________________________
def test_3(Book, book):
    assert issubclass(Book, object), "Класс Book не является подклассом object, скорее всего не создан"

    assert book.__dict__ == {
        'title': 'Python ООП',
        'author': 'Сергей Балакирев',
        'pages': 123,
        'year': 2022
    }, " Ошибка в атрибутах"
    # проверка что метод __setattr__ переопределен в классе
    # если методы не идентичны значит метод не переопределён в классе
    assert Book.__setattr__ != object.__setattr__, "Метод __setattr__ не переопределен в классе MyClass"

    # проверка атрибутов объекта
    assert type(book.title) == str, "title не является строкой"
    assert type(book.author) == str, "title не является строкой"
    assert type(book.pages) == int, "pages не целое число"
    assert type(book.year) == int, "pages не целое число"

    # проверка принудительной генерации ошибки
    try:
        book.title = 111
    except  TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    try:
        book.pages = '111'
    except  TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    print("Правильный ответ !")
