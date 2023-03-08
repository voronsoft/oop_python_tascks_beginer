"""Объявите пустой класс с именем Car.
С помощью функции setattr() добавьте в этот класс атрибуты:

model: "Тойота"
color: "Розовый"
number: "П111УУ77"

Присвойте переменной temp значение атрибута color
Выведите на экран значение атрибута color, используя словарь __dict__ класса Car.
Запустите файл на исполнение
"""


class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

temp = Car.color
print(Car.__dict__['color'])

# TEST-TASK___________________________________
assert hasattr(Car, "model"), "В классе нет атрибута model"
assert hasattr(Car, "color"), "В классе нет атрибута color"
assert hasattr(Car, "number"), "В классе нет атрибута number"

assert Car.model == "Тойота", "Значение атрибута неправильное"
assert Car.color == "Розовый", "Значение атрибута неправильное"
assert Car.number == "П111УУ77", "Значение атрибута неправильное"

assert temp == "Розовый", "Неправильное значение в переменной temp"
print("Правильно !")
