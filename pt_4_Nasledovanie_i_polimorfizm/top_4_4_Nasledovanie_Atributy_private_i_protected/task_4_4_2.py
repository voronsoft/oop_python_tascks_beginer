"""
Подвиг 2. В программе объявлены два класса следующим образом:

class Phone:
    def __init__(self, model):
        self.__model = model


class SmartPhone(Phone):
    def __init__(self, model, memory):
        super().__init__(model)
        self.__memory = memory

    def get_info(self):
        return self.__model, self.__memory
И выполняются команды:

phone = SmartPhone('iPhone 123', 1024)
print(phone.get_info())

Выберите все верные утверждения о приведенной программе.


приватная переменная __model доступна только внутри класса Phone и недоступна в классе SmartPhone
в момент создания объекта phone произойдет ошибка, так как приватная переменная __model должна объявляться в классе SmartPhone
программа будет работать без ошибок, если метод get_info() поместить в базовый класс Phone
в момент вызова метода get_info() произойдет ошибка, так как локальный атрибут __model отсутствует в классе SmartPhone
программа отработает без ошибок и в консоль будет выведена информация по модели и размеру памяти
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test4_4.test_4_4_2 import test_2

test_2(temp)
# END
