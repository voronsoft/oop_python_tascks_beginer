"""Подвиг 2. Установите соответствия между магическими методами и их описаниями.

__setattr__() автоматически вызывается при удалении атрибута класса или объекта
__getattribute__() автоматически вызывается при обращении к несуществующему атрибуту класса или объекта
__getattr__() автоматически вызывается при обращении к атрибуту класса или объекта
__delattr__() автоматически вызывается при изменении атрибута класса или объекта
"""

# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ', 'ответ']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 4 and \
           "__setattr__() автоматически вызывается при изменении атрибута класса или объекта" in temp and \
           "__getattribute__() автоматически вызывается при обращении к атрибуту класса или объекта" in temp and \
           "__getattr__() автоматически вызывается при обращении к несуществующему атрибуту класса или объекта" in temp and \
           "__delattr__() автоматически вызывается при удалении атрибута класса или объекта" in temp
except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")