"""
Подвиг 3. Ранее вы уже использовали делегирование методов,
когда вызывали инициализатор базового класса через функцию super().
Чаще всего делегирование в Python связано с вызовом магических методов базовых классов (так как их имена нельзя менять).
Выполним такой пример.
Объявите в программе базовый класс с именем Book, объекты которого создаются командой:
book = Book(title, author, pages, year)
где title - заголовок книги (строка);
author - автор книги (строка);
pages - число страниц (целое число);
year - год издания (целое число).
В каждом объекте класса Book должны формироваться соответствующие локальные атрибуты: title, author, pages, year.

Объявите дочерний класс DigitBook от класса Book, объекты которого создаются командой:
db = DigitBook(title, author, pages, year, size, frm)
где дополнительные параметры
size - размер книги в байтах (целое число);
frm - формат книги (строка: 'pdf', 'doc', 'fb2', 'txt').
В каждом объекте класса DigitBook должны формироваться соответствующие локальные атрибуты:
title, author, pages, year, size, frm.

Инициализация локальных атрибутов title, author, pages, year должна выполняться в базовом классе Book,
а параметры size, frm инициализируются в дочернем классе DigitBook.

P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.
"""


class Book:
    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title  # заголовок книги (строка)
        self.author = author  # автор книги (строка)
        self.pages = pages  # число страниц (целое число)
        self.year = year  # год издания (целое число)


class DigitBook(Book):
    def __init__(self, title: str, author: str, pages: int, year: int, size: int, frm: str):
        super().__init__(title, author, pages, year)
        self.size = size  # размер книги в байтах (целое число)
        self.frm = frm  # формат книги (строка: 'pdf', 'doc', 'fb2', 'txt')

# # TEST
# obj = DigitBook('Title', 'Norov', 155, 1977, 1333, 'doc')
