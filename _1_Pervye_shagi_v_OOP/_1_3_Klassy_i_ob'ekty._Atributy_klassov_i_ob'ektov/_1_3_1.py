"""
Отметьте все верные, с точки зрения стандарта PEP8, имена классов.

SergeyBalakirev
Data123
DataBase
data_base
dataBase
Sergey_Balakirev
"""
# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 3 and "SergeyBalakirev" in temp and "Data123" in temp and "DataBase" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
