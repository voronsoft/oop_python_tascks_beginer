"""Объявите класс с именем TravelBlog и объявите в нем атрибут:
total_blogs: 0

Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
name: 'Франция'
days: 6

Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.

Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:
name: 'Италия'
days: 5

Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.

P.S. На экран ничего выводить не нужно.
Запустите файл на исполнение
"""


# ваш код
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = 'Франция'
tb1.days = 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
TravelBlog.total_blogs += 1
# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_8 import test_8

test_8(TravelBlog, tb1, tb2)

# END
