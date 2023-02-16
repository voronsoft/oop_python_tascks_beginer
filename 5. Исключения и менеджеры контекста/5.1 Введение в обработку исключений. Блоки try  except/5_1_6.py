# Подвиг 6. Имеется следующий фрагмент программы:

try:
    x, y = map(float, input().split())
    d = x / y
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('except')

# В каких случаях выполнение программы перейдет во второй блок except?
 
    # при вводе хотя бы одного не числового значения
# никогда не перейдет, т.к. общий блок except следует записывать первым
# ни в каких, программа не будет выполнена, т.к. записывать два блока except для одного блока try нельзя
    # при возникновении любых исключений, кроме исключения ZeroDivisionError