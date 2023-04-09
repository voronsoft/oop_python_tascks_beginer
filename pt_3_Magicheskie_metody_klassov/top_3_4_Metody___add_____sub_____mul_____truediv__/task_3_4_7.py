"""
Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

- class Lib - для представления библиотеки в целом;
Объекты класса Lib создаются командой:
lib = Lib()
Каждый объект должен содержать локальный публичный атрибут:
book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.
Также объекты класса Lib должны работать со следующими операторами:
lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx

-class Book - для описания отдельной книги.
Объекты класса Book должны создаваться командой:
book = Book(title, author, year)
где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).


При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
Также с объектами класса Lib должна работать функция:
n = len(lib) # n - число книг
которая возвращает число книг в библиотеке.

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""


# ваш код:
class Lib:
    """Представление библиотеки в целом"""

    def __init__(self):
        self.book_list = list()

    # Также объекты класса Lib должны работать со следующими операторами:
    # lib = lib + book # добавление новой книги в библиотеку
    # lib += book
    def __add__(self, other):
        self.book_list.append(other)
        return self

    # lib += book
    def __iadd__(self, other):
        self.book_list.append(other)
        return self

    # lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
    # lib -= book
    #
    # lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
    # lib -= indx
    def __sub__(self, other):
        # удаляем если other цифра
        if type(other) == int and 0 <= other < len(self.book_list):
            del self.book_list[other]
            return self
        # удаляем если это obj
        elif isinstance(other, Book):
            temp = self.book_list.index(other) - 1
            del self.book_list[temp]
            return self

    # Также с объектами класса Lib должна работать функция:
    # n = len(lib) # n - число книг
    # которая возвращает число книг в библиотеке.
    def __len__(self):
        return len(self.book_list)


# Объекты класса Book должны создаваться командой:
# book = Book(title, author, year)
# где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
class Book:
    """Описание отдельной книги"""

    def __init__(self, title: str, author: str, year: int):
        if type(title) == str and type(author) == str and type(year) == int:
            self.title = title
            self.author = author
            self.year = year
        else:
            raise 'Тип данных неверный'


# end ваш код

# TEST-TASK___________________________________
from test3_4.test_3_4_7 import test_7

test_7(Lib, Book)
# END
