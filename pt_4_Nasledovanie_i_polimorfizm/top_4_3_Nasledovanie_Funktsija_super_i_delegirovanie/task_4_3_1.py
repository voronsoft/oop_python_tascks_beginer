"""
Подвиг 1. В программе записаны следующие классы:

class Phone:
    def get_info(self):
        return "Phone"


class SmartPhone(Phone):
    def call(self):
        pass

    def get_info(self):
        return "SmartPhone"


Выберите все верные утверждения, связанные с этой программой.

дочерний класс SmartPhone расширяет базовый класс Phone
в классе SmartPhone выполняется переопределение метода get_info()
класс Phone расширяет класс SmartPhone
класс SmartPhone лишь переопределяет класс Phone
класс SmartPhone наследуется от класса Phone
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test4_3.test_4_3_1 import test_1

test_1(temp)
# END
