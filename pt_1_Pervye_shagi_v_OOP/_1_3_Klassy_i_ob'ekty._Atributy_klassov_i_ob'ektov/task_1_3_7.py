"""Объявите класс с именем Dictionary и определите в нем следующие атрибуты:

rus: "Питон"
eng: "Python"

Затем, с помощью функции getattr() прочитайте значение атрибута rus_word.
Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.
Полученное значение нужно присвоить переменной temp.
Выведете на экран значение переменной temp.
Запустите файл на исполнение.
"""


class Dictionary:
    rus = 'Питон'
    eng = 'Python'


temp = getattr(Dictionary, 'rus_word', False)
print(temp)

# TEST-TASK___________________________________
try:
    issubclass(Dictionary, object)
except NameError:
    print("Вы не создали класс - Dictionary")

assert hasattr(Dictionary, 'rus') and hasattr(Dictionary, 'eng'), "В классе должно быть два атрибута - rus, eng"
assert hasattr(Dictionary, 'rus_word') == False, "Переменно rus_word не должно быть в классе"
assert temp is False, "Значение присвоенное переменной temp неверное !!"
print('Всё правильно, так держать !')
