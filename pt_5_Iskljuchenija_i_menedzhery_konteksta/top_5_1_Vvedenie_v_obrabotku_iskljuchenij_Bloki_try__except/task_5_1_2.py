"""
Подвиг 2. Имеется следующий фрагмент программы:

try:
    val = float(input())
except ValueError as e:
    print(e)
При каких входных данных выполнение программы перейдет в блок except?

при вводе любых не числовых значений
при вводе вещественных или целочисленных значений
при вводе не числовых или вещественных значений
при вводе не числовых или целочисленных значений
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = [""]
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test5_1.test_5_1_2 import test_2

test_2(temp)
# END