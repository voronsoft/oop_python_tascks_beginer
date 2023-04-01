"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/w0SAD6zNLlw

Подвиг 6. Объявите класс Book со следующим набором сеттеров и геттеров:

set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
get_price(self) - получение значения локального приватного свойства __price объектов класса Book;

Объекты класса Book предполагается создавать командой:
book = Book(автор, название, цена)

При этом, в каждом объекте должны создаваться приватные локальные свойства:
__author - строка с именем автора;
__title - строка с названием книги;
__price - целое число с ценой книги.

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""


# ваш код:
class Book:
    # При этом, в каждом объекте должны создаваться приватные локальные свойства:
    # __author - строка с именем автора;
    # __title - строка с названием книги;
    # __price - целое число с ценой книги.
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    # set_title(self, title) - запись в локальное приватное свойство __title объектов класса Book значения title;
    def set_title(self, title):
        self.__title = title

    # set_author(self, author) - запись в локальное приватное свойство __author объектов класса Book значения author;
    def set_author(self, author):
        self.__author = author

    # set_price(self, price) - запись в локальное приватное свойство __price объектов класса Book значения price;
    def set_price(self, price):
        self.__price = price

    # get_title(self) - получение значения локального приватного свойства __title объектов класса Book;
    def get_title(self):
        return self.__title

    # get_author(self) - получение значения локального приватного свойства __author объектов класса Book;
    def get_author(self):
        return self.__author

    # get_price(self) - получение значения локального приватного свойства __price объектов класса Book;
    def get_price(self):
        return self.__price


# end ваш код

# TEST-TASK___________________________________
from test2_1.test_2_1_6 import test_6

test_6(Book)
# END
