"""Объявите класс с именем Notes и определите в нем следующие атрибуты:
uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2

Присвойте переменной temp значение атрибута author с помощью функции getattr().
Затем, выведите на экран значение атрибута temp.
Запустите файл на исполнение
"""


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


temp = getattr(Notes, 'author')
print(getattr(Notes, 'author'))

# TEST-TASK___________________________________
assert hasattr(Notes, 'uid'), "В классе отсутствует атрибут - uid"
assert hasattr(Notes, 'title'), "В классе отсутствует атрибут - title"
assert hasattr(Notes, 'author'), "В классе отсутствует атрибут - author"
assert hasattr(Notes, 'pages'), "В классе отсутствует атрибут - pages"

assert Notes.uid == 1005435 and Notes.title == "Шутка" and Notes.author == "И.С. Бах" and Notes.pages == 2, "Значение в каком то атрибуте несоответствуют заданию"
assert getattr(Notes, "author") == "И.С. Бах", 'Неправильное значение атрибута author '
assert temp == "И.С. Бах", "Неверное значение в переменной temp"
print("Правильно !")
