"""
Подвиг 2. Пусть в программе объявлен следующий класс:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
И создаются его экземпляры:

v1 = Vector(1, 2)
v2 = Vector(2, 1)
Для каких операций сравнения будет вызван магический метод __eq__() класса Vector?


v1 <= v2
v1 >= v2
v1 == v2
v1 != v2
"""

# Вставьте правильные ответы в переменную
# Пример temp = ["__eq__()--оператор равенства ==", 'ответ' ]
temp = ["v1 == v2", "v1 != v2"]
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test3_5.test_3_5_2 import test_2

test_2(temp)
# END
