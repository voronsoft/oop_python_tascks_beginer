"""Объявите класс с именем Dictionary и определите в нем следующие атрибуты:

rus: "Питон"
eng: "Python"
Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word.
Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.
"""


class Dictionary:
    rus = 'Питон'
    eng = 'Python'

    def __getattr__(self, item):
        print("был вызов")


print(getattr(Dictionary, 'rus_word', False))

# TEST-TASK___________________________________
try:
    issubclass(Dictionary, object)
except NameError:
    print("Вы не создали класс - Dictionary")

assert hasattr(Dictionary, 'rus') and hasattr(Dictionary, 'eng'), "В классе должно быть два атрибута - rus, eng"
assert getattr(Dictionary, 'rus_word', False) is False
