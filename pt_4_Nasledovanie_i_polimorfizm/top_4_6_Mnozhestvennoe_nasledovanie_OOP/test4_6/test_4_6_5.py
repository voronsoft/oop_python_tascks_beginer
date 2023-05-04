# TEST-TASK___________________________________
def test_5(Book, Jornal):

    import io
    import sys
    # не изменять !!
    # 1 вариант
    book = Book("Python ООП", "Балакирев", 2022)

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер

    print(book)
    output1 = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    assert output1 == '_title: Python ООП\n_author: Балакирев\n_year: 2022\n', \
        "при наследовании ShopItem, ShopUserView вывод был некорректным"
    # на экране увидим строчки:
    # _id: 1
    # _title: Python ООП
    # _author: Балакирев
    # _year: 2022

    # 2 вариант использования классов:
    jornal = Jornal('Hustler', 'Doe', 2023)
    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    print(jornal)
    output2 = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
    assert output2 == '_id: 2\n_title: Hustler\n_author: Doe\n_year: 2023\n', \
        "при наследовании ShopItem, ShopGenericView вывод был некорректным"
    print("Здорово, всё верно. 5")
