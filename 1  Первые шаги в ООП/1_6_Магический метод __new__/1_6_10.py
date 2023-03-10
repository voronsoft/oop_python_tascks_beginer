"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/5aJVuJ5jGqk

Подвиг 10 (на повторение материала).
В программе предполагается реализовать парсер (обработчик) строки (string) в определенный выходной формат.
Для этого объявлен следующий класс:

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

И предполагается его использовать следующим образом:

ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
На выходе (в переменной res) ожидается получить список из набора вещественных чисел.
Например, для заданной строки, должно получиться:
[4.0, 5.0, -6.5]

Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:
build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
build_number(self, string) - для преобразования переданной в метод строки (string)
в вещественное значение (метод должен возвращать полученное вещественное число).

Объявите класс с именем Factory, чтобы получать на выходе искомый результат.

P.S. В программе на экран ничего выводить не нужно.
"""


# Здесь объявляется класс Factory
# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:
# build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
# build_number(self, string) - для преобразования переданной в метод строки (string)
# в вещественное значение (метод должен возвращать полученное вещественное число).
class Factory:
    def build_sequence(self):
        """для создания начального пустого списка (метод должен возвращать пустой список)"""
        lst = []
        return lst

    def build_number(self, string):
        """build_number(self, string) - для преобразования переданной в метод строки (string)
        в вещественное значение (метод должен возвращать полученное вещественное число)."""
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# TEST-TASK___________________________________
ld = Loader()
s = '4, 5, -6.5, -0.5'
res = ld.parse_format(s, Factory())
#
assert hasattr(Factory, "build_sequence")
assert hasattr(Factory, "build_number")
#
x = Factory()
assert x.build_sequence() == [] and len(x.build_sequence()) == 0, \
    "ошибка, метод build_sequence должен возвращать пустой список"
assert type(x.build_number('4.5')) == float and type(x.build_number('4')) == float, \
    "ошибка, метод build_number работает неправильно"
print(f"Результат: {res}")
print("Правильно, так держать !")
