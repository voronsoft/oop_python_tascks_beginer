"""
Объявите класс с именем DataBase, который бы хранил в себе следующую информацию:
pk: 1
title: "Классы и объекты"
author: "Сергей Балакирев"
views: 14356
comments: 12
Имена переменных (атрибутов класса) используйте такие же (pk, title, author, views и comments) с соответствующими значениями.
Запустите файл на исполнение
"""


# ваш код
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_3 import test_3

test_3(DataBase)

# END
