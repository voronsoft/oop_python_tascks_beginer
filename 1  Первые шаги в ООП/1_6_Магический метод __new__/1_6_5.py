"""
Подвиг 5. При переопределении метода __new__() объект создается командой super().__new__(cls):
class Point:
    def __new__(cls, *args, **kwargs):
       return super().__new__(cls)
Выберите верное утверждение для ее объяснения.
"""


# ОТВЕТ:
# print('Идет обращение к базовому классу, из которого вызывается конструктор \n- метод __new__(cls) с аргументом cls - ссылки на текущий класс')


class Point:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


pt = Point(1, 2)
