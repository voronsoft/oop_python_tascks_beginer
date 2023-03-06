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
"""


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

# TEST-TASK___________________________________
assert isinstance(tb1, TravelBlog) and isinstance(tb2, TravelBlog), "Вы не создали 2 экземпляра класса - tb1 и tb2"
assert len(
    tb1.__dict__) == 2 and "name" in tb1.__dict__ and "days" in tb1.__dict__, "Должно быть только два локальных свойства name и days"
assert len(
    tb2.__dict__) == 2 and "name" in tb2.__dict__ and "days" in tb2.__dict__, "Должно быть только два локальных свойства name и days"
assert TravelBlog.total_blogs == 2, "Атрибут класса total_blogs должен быть равен 2м"
