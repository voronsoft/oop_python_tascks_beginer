"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/lI99OdJt71w
Подвиг 3. Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
book = Book()
book = Book(название, автор, число страниц, год издания)

В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
title - заголовок книги (строка, по умолчанию пустая строка);
author - автор книги (строка, по умолчанию пустая строка);
pages - число страниц (целое число, по умолчанию 0);
year - год издания (целое число, по умолчанию 0).

Объявите в классе Book магический метод __setattr__ для проверки типов присваиваемых данных локальным свойствам
title, author, pages и year.
Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку, а pages - на целое число),
то генерировать исключение командой:
raise TypeError("Неверный тип присваиваемых данных.")

Создайте в программе объект book класса Book для книги:
автор: Сергей Балакирев
заголовок: Python ООП
pages: 123
year: 2022

P.S. На экран ничего выводить не нужно.
"""


class Book:
    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key == 'title' and type(value) is str:
            return object.__setattr__(self, key, value)

        elif key == 'author' and type(value) is str:
            return object.__setattr__(self, key, value)

        elif key == 'pages' and type(value) is int:
            return object.__setattr__(self, key, value)

        elif key == 'year' and type(value) is int:
            return object.__setattr__(self, key, value)

        else:
            raise TypeError("Неверный тип присваиваемых данных.")


# ПРОВЕРКА Создайте в программе объект book класса Book для книги
book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)

# TEST-TASK___________________________________
assert issubclass(Book, object), "Класс Book не является подклассом object, скорее всего не создан"

assert book.__dict__ == {
    'title': 'Python ООП',
    'author': 'Сергей Балакирев',
    'pages': 123,
    'year': 2022
}, " Ошибка в атрибутах"
# проверка что метод __setattr__ переопределенн в классе
# если методы не идентичны значит метод непереопределён в классе
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
