"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/pohpzoAbkrQ

Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел.
Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list и переопределить три метода:
__init__()
__setitem__()
append()
так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой другой тип данных,
генерировать исключение командой:
raise TypeError('можно передавать только целочисленные значения')

Пример использования класса ListInteger (эти строчки в программе не писать):
s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
s[0] = 10.5 # TypeError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно."""


class ListInteger(list):
    def __init__(self, lst):
        for _ in lst:
            if type(_) is not int:
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    def __setitem__(self, key, value):
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')
        else:
            super().__setitem__(key, value)

    def append(self, value):
        if type(value) is not int:
            raise TypeError('можно передавать только целочисленные значения')
        else:
            super().append(value)

# # TEST
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5  # TypeError
