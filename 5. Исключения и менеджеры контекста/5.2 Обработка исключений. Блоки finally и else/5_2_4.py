"""
Подвиг 4. В программе вводятся два значения в одну строчку через пробел.
Значениями могут быть числа, слова, булевы величины (True/False).
Необходимо прочитать эти значения из входного потока.
Если оба значения являются числами, то вычислить их сумму,
иначе соединить их в одну строку с помощью оператора + (конкатенации строк).
Результат вывести на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.
Sample Input:
8 11
Sample Output:
19
"""
vol1, vol2 = input().split()

try:
    ans = int(vol1) + int(vol2)
except:
    try:
        ans = int(vol1) + float(vol2)
    except:
        try:
            ans = float(vol1) + int(vol2)
        except:
            try:
                ans = float(vol1) + float(vol2)
            except:
                ans = vol1 + vol2
finally:
    print(ans)

