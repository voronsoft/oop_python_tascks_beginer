"""
Подвиг 2. Пусть в некотором классе определены три метода:

get_pr() - геттер;
set_pr() - сеттер;
del_pr() - делитер.

Выберите все верные варианты использования класса property для создания объектов-свойств на основе этих методов.

pr = property(get_pr, set_pr)
pr = property(get_pr, set_pr, del_pr)
pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr)
pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr); pr = pr.deleter(del_pr)
pr = property(get_pr)
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test2_2.test_2_2_2 import test_2

test_2(temp)
# END
