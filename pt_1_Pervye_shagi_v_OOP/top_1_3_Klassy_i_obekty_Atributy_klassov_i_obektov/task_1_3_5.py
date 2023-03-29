"""Объявите пустой класс с именем Car.
С помощью функции setattr() добавьте в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
Запустите файл на исполнение
"""


# ваш код
class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")
print(Car.__dict__['color'])
# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_5 import test_5

test_5(Car)

# END
