"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/KV8T8JDtxW4

Подвиг 6.
В программе предполагается реализовать парсер (обработчик) строки с данными string в определенный выходной формат.
Для этого объявлен следующий класс:

class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq
И предполагается его использовать следующим образом:

res = Loader.parse_format("4, 5, -6", Factory)
На выходе (в переменной res) ожидается получать список из набора целых чисел.
Например, для заданной строки, должно получиться:
[4, 5, -6]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:
build_sequence() - для создания пустого списка (метод возвращает пустой список);
build_number(string) - для преобразования строки (string) в целое число
(метод возвращает полученное целочисленное значение).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""


# Здесь объявляется класс Factory:
# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:
class Factory:
    # build_sequence() - для создания пустого списка (метод возвращает пустой список);
    @staticmethod
    def build_sequence():
        lst = []
        return lst

    # build_number(string) - для преобразования строки (string) в целое число
    # (метод возвращает полученное целочисленное значение).
    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# На выходе (в переменной res) ожидается получать список из набора целых чисел.
# Например, для заданной строки, должно получиться:
# [4, 5, -6]

# TEST-TASK___________________________________
assert Factory.build_sequence() == [], 'Неправильно отработал метод build_sequence'
assert type(Factory.build_number('10')) is int, 'Неправильно отработал метод build_number'

try:
    assert res == [1, 2, 3, -5, 10]
except:
    print("Ошибка, в переменной res неправильный результат")

else:
    print("Правильно !")
