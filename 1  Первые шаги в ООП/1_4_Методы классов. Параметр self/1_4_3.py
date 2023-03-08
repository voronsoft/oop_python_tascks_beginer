"""
Какую роль играет параметр self в методах класса?
"""

# это ссылка на класс, которому принадлежит метод
# это ссылка на объект класса, из которого был вызван метод
# это просто обязательный (зарезервированный) параметр для методов класса, через который можно передавать произвольные данные
# это ссылка на текущий метод класса

# Вставьте правильные ответы в переменную
# После запустите файл на исполнение )
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 1 and "это ссылка на объект класса, из которого был вызван метод" in temp
except:
    print("Пока неправильно попробуйте другие варианты")
else:
    print("Правильно !")
