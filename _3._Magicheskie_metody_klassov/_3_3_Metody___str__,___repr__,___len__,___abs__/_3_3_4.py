"""Подвиг 4. Объявите класс WordString, объекты которого создаются командами:

w1 = WordString()
w2 = WordString(string)
где string - передаваемая строка. Например:

words = WordString("Курс по Python ООП")
Реализовать следующий функционал для объектов этого класса:

len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).

Также в классе WordString реализовать объект-свойство (property):

string - для передачи и считывания строки.

Пример пользования классом WordString (эти строчки в программе писать не нужно):
words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
"""


class WordString:

    def __init__(self, string=''):
        self.__string = string

    # property
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value

    # end property
    def __len__(self):
        """Должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами)"""
        self.__string = self.__string.strip()
        while '  ' in self.__string:
            self.__string = self.__string.replace('  ', ' ')

        return len(self.__string.split(' '))

    def __call__(self, indx, *args, **kwargs):
        """Должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0)"""
        return self.__string.split(' ')[indx]

# # TEST
# # Пример пользования классом WordString (эти строчки в программе писать не нужно):
# words = WordString()
# words.string = "       1 2 3       4 5 6 7  "
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
# # P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
