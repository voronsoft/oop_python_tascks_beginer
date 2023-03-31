"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/uE1uf7Qtbh4
Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:

a = SingletonFive(<наименование>)
Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.

Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
должны быть ссылкой на последний (пятый) созданный объект.

Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:

objs = [SingletonFive(str(n)) for n in range(10)]
P.S. В программе на экран ничего выводить не нужно.
"""


# ваш код:
class SingletonFive:
    temp = None

    def __new__(cls, *args, **kwargs):
        if int(*args) <= 4:
            cls.temp = super().__new__(cls)

        return cls.temp

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
# end ваш код

# TEST-TASK___________________________________
from test1_6.test_1_6_7 import test_7

test_7(objs)
# END
