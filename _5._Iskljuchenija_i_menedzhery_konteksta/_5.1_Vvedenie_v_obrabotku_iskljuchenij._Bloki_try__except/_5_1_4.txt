Подвиг 4. Имеется следующая иерархия классов исключений:

смотреть 5_1_4.docx

И записан фрагмент программы:

try:
    x, y = map(float, input().split())
    d = x / y
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('ZeroDivisionError')
В каких случаях выполнение программы перейдет в блок обработки исключения ZeroDivisionError?

если значение y будет равно нулю
всегда будет переходить при возникновении исключения типа ZeroDivisionError
если значение x будет равно нулю
если ввести хотя бы одно не числовое значение
    ни в каких, так как класс ZeroDivisionError является дочерним по отношению к классу ArithmeticError