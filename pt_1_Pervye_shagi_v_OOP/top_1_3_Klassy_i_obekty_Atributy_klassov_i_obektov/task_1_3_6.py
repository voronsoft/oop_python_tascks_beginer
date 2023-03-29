"""Объявите класс с именем Notes и определите в нем следующие атрибуты:
uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2

Присвойте переменной temp значение атрибута author с помощью функции getattr().
Затем, выведите на экран значение атрибута temp.
Запустите файл на исполнение
"""


# ваш код
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


temp = getattr(Notes, 'author')
print(getattr(Notes, 'author'))

# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_6 import test_6

test_6(Notes, temp)

# END
