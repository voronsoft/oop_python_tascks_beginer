"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/7aVqWfrAdqw

Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать. При выполнении команды:

obj = AbstractClass()
переменная obj должна ссылаться на строку с содержимым:

"Ошибка: нельзя создавать объекты абстрактного класса"

P.S. В программе объявить только класс, выводить на экран ничего не нужно.
"""


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return 'Ошибка: нельзя создавать объекты абстрактного класса'

    def __init__(self, a):
        self.a = a


obj = AbstractClass(1)

# TEST-TASK___________________________________
assert obj == "Ошибка: нельзя создавать объекты абстрактного класса", "ошибка, переменная obj должна ссылаться на строку с содержимым - Ошибка: нельзя создавать объекты абстрактного класса"
print("Правильно !")