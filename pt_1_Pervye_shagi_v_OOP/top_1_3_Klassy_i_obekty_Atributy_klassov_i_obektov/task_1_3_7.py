"""Объявите класс с именем Dictionary и определите в нем следующие атрибуты:

rus: "Питон"
eng: "Python"

Затем, с помощью функции getattr() прочитайте значение атрибута rus_word.
Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.
Полученное значение нужно присвоить переменной temp.
Выведете на экран значение переменной temp.
Запустите файл на исполнение.
"""


# ваш код
class Dictionary:
    rus = 'Питон'
    eng = 'Python'


temp = getattr(Dictionary, 'rus_word', False)
print(temp)
# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_7 import test_7

test_7(Dictionary, temp)

# END
