# TEST-TASK___________________________________
def test_2(Book, book, output):
    try:
        issubclass(Book, object)
    except:
        print("Book класс не объявлен")

    assert hasattr(book, "title") and hasattr(book, "author") and hasattr(book, "pages"), "ошибка атрибутов"

    if output == "Книга: Python ООП; Балакирев С.М.; 1024\n":
        print(output)
        print("Правильный ответ. ")
    else:
        print(f"Ваш ответ: {output}")
        print(f"Правильный ответ: Книга: Python ООП; Балакирев С.М.; 1024")
        print("\nошибка, формат строки неправильный")
