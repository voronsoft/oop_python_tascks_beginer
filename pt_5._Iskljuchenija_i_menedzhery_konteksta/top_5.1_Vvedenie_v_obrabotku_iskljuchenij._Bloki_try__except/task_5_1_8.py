"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/zQDvmHlS6wg

Подвиг 8. В программе вводятся в одну строчку через пробел некоторые данные, например:
"1 -5.6 True abc 0 23.56 hello"
Эти данные разбиваются по пробелу и представляются в виде списка строк:
lst_in = input().split()
Ваша задача сформировать новый список с именем lst_out,
в котором строки с целыми числами будут представлены как целые числа (тип int),
строки с вещественными числами, как вещественные (тип float), а остальные данные - без изменений.

Например:
lst_out = [1, -5.6, 'True', 'abc', 0, 23.56, 'hello']  # после обработки введенной строки "1 -5.6 True abc 0 23.56 hello"
Реализовать эту задачу следует с помощью функции map()
и объявления вспомогательной функции с механизмом обработки исключений для непосредственного преобразования данных
в целые или вещественные числа.

P.S. В программе нужно только сформировать список lst_out. На экран ничего выводить не нужно.

Sample Input:
hello 1 world -2 4.5 True
Sample Output:
"""


# считывание строки и разбиение ее по пробелам
# lst_in = input().split()

def verify(value):
    try:
        if int(value):
            return int(value)
        else:
            return int(value)
    except:
        try:
            if float(value):
                return float(value)
        except:
            return value


lst_in = input().split()
lst_out = list(map(verify, lst_in))