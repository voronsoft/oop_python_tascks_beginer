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

# Создайте список temp с правильными ответами через запятую
# Пример temp = [ответ', 'ответ']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 5 and \
           "pr = property(get_pr, set_pr)" in temp and \
           "pr = property(get_pr, set_pr, del_pr)" in temp and \
           "pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr)" in temp and \
           "pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr); pr = pr.deleter(del_pr)" in temp and \
           "pr = property(get_pr)" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
