"""
Подвиг 1. Пусть в программе объявлен следующий класс:

class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    money = property(get_money, set_money)
И, затем, выполняются команды:

m = Money()
m.money = 10
Выберите верные утверждения, связанные с этими программными строчками.

в строчке money = property(get_money, set_money) создается объект-свойство с геттером set_money и сеттером get_money
если в программу после строчки m.money = 10 добавить строчку m.__dict__['money'] = 100, то при считывании значения res = m.money получим число 100
для считывания информации из локальной переменной __money достаточно записать res = m.money
в строчке money = property(get_money, set_money) создается объект-свойство с геттером get_money и сеттером set_money
в строчке m.money = 10 происходит вызов метода set_money и локальной переменной __money присваивается значение 10
в строчке m.money = 10 происходит создание локального свойства money в объекте m с присвоением значения 10
"""
# Создайте список temp с правильными ответами через запятую
# Пример temp = [ответ', 'ответ']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 3 and \
           "для считывания информации из локальной переменной __money достаточно записать res = m.money" in temp and \
           "в строчке money = property(get_money, set_money) создается объект-свойство с геттером get_money и сеттером set_money" in temp and \
           "в строчке m.money = 10 происходит вызов метода set_money и локальной переменной __money присваивается значение 10" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
