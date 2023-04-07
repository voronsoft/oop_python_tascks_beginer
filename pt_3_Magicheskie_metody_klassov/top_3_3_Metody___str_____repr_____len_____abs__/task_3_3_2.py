"""Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:
book = Book(title, author, pages)
где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).
Также при выводе информации об объекте на экран командой:
print(book)
должна отображаться строчка в формате:
"Книга: {title}; {author}; {pages}"
Например:
"Книга: Муму; Тургенев; 123"
Прочитайте строки с информацией по книге командой:
s = "Python ООП\nБалакирев С.М.\n1024"
lst_in = list(map(str.strip, s.splitlines()))
(строки идут в порядке: title, author, pages).
Создайте объект book класса Book и выведите его строковое представление в консоль.

Sample Input:
Python ООП
Балакирев С.М.
1024

Sample Output:
Книга: Python ООП; Балакирев С.М.; 1024
Напишите программу. Тестируется через s
"""
# не изменять !!
import io
import sys

console_out = io.StringIO()  # Создаем буфер
sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер

s = "Python ООП\nБалакирев С.М.\n1024"
lst_in = list(map(str.strip, s.splitlines()))


# end


# здесь пишите программу
# ваш код:


class Book:
    def __init__(self, title='', author='', pages=0):
        self.title = str(title)
        self.author = str(author)
        self.pages = int(pages)

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


book = Book(lst_in[0], lst_in[1], lst_in[2])
print(book)
# end ваш код

# TEST-TASK___________________________________
from test3_3.test_3_3_2 import test_2

output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
test_2(Book, book, output)
# END
