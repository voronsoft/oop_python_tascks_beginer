"""
Подвиг 4. Имеется следующая иерархия классов исключений:
смотреть файл  task_5_1_4.docx

    ArithmeticError                 EOFError
        |
        |-ZeroDivisionError
        |
        |-FloatingPointError
        |
        |-OverflowError

И записан фрагмент программы:

try:
    x, y = map(float, input().split())
    d = x / y
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')

В каких случаях выполнение программы перейдет в блок обработки исключения ZeroDivisionError?

всегда будет переходить при возникновении исключения типа ZeroDivisionError
если значение y будет равно нулю
ни в каких, так как класс ZeroDivisionError является дочерним по отношению к классу ArithmeticError
если ввести хотя бы одно не числовое значение
если значение x будет равно нулю
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = []
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test5_1.test_5_1_4 import test_4

test_4(temp)
# END
