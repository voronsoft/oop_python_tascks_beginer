"""
Подвиг 2. Имеется следующая программа, в которой объявлены три класса:

class A:
    def __init__(self):
        print("A")
        super().__init__()


class B:
    def __init__(self):
        print("B")
        super().__init__()


class C(A, B):
    def __init__(self):
        print("C")
        super().__init__()
И создается экземпляр класса C:

c = C()


В какой последовательности будут выведены буквы A, B, C в консоль
(то есть, в какой последовательности будут вызваны инициализаторы этих классов):

C A B
C B A
A B C
B A C
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test4_6.test_4_6_2 import test_2

test_2(temp)
# END
