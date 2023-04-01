# TEST-TASK___________________________________
def test_6(Book):
    book = Book('автор', 'название', 'цена')
    assert '_Book__author' in book.__dict__ and '_Book__title' in book.__dict__ and '_Book__price' in book.__dict__, 'Ошибка локальных приватных свойств'

    assert book.get_author() == "автор", 'Ошибка в get_author'
    book.set_author('qq')
    assert book.get_author() == 'qq', 'Ошибка в set_author'

    assert book.get_title() == "название", 'Ошибка в get_title'
    book.set_title('назв')
    assert book.get_title() == 'назв', 'Ошибка в set_author'

    assert book.get_price() == "цена", 'Ошибка в get_price'
    book.set_price('100')
    assert book.get_price() == '100', 'Ошибка в set_price'
    print("Правильный ответ !")
