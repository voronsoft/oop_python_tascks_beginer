"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EEzEodYvoXc

Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так,
чтобы при вводе строки из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
P.S. На экран ничего выводить не нужно.
"""


# ваш код:
class InputDigits:

    def __init__(self, string):
        self.string = string

    def __call__(self, string):
        lst = list(map(int, string.split(' ')))
        return lst


@InputDigits
def input_dg(x):
    return x


st = input()
res = input_dg(st)
# end ваш код

# TEST-TASK___________________________________
from test3_2.test_3_2_9 import test_9

test_9(InputDigits, input_dg)

# END
