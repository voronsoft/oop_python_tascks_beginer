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


# TEST
class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


# TEST-TASK___________________________________
assert hasattr(DataBase, 'pk'), "В классе нет атрибута - pk"
assert hasattr(DataBase, 'title'), "В классе нет атрибута - title"
assert hasattr(DataBase, 'author'), "В классе нет атрибута - author"
assert hasattr(DataBase, 'views'), "В классе нет атрибута - views"
assert hasattr(DataBase, 'comments'), "В классе нет атрибута - comments"

assert DataBase.pk == 1, "Значение атрибута неправильное"
assert DataBase.title == "Классы и объекты", "Значение атрибута неправильное"
assert DataBase.author == "Сергей Балакирев", "Значение атрибута неправильное"
assert DataBase.views == 14356, "Значение атрибута неправильное"
assert DataBase.comments == 12, "Значение атрибута неправильное"
print("Правильно !")
