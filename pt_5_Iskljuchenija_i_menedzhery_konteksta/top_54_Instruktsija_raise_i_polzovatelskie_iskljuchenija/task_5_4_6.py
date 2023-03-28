"""
Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:
date = DateString(date_string)
где date_string - строка с датой в формате: "DD.MM.YYYY"
здесь DD - день (целое число от 1 до 31);
MM - месяц (целое число от 1 до 12);
YYYY - год (целое число от 1 до 3000).
Например:
date = DateString("26.05.2022")
или
date = DateString("26.5.2022") # незначащий ноль может отсутствовать
Если указанная дата в строке записана неверно (не по формату), то генерировать исключение с помощью собственного класса:

DateError - класс-исключения, унаследованный от класса Exception.
В самом классе DateString переопределить магический метод __str__() для формирования строки даты в формате:
"DD.MM.YYYY"
(здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна формироваться строка "26.05.2022").

Далее, в программе выполняется считывание строки из входного потока командой:
date_string = input()
Ваша задача создать объект класса DateString с аргументом date_string и вывести объект на экран командой:
print(date) # date - объект класса DateString
Если же произошло исключение, то вывести сообщение (без кавычек):
"Неверный формат даты"

Sample Input:
1.2.1812
Sample Output:
01.02.1812
"""


# здесь объявляйте классы
class DateString:
    """Представление дат"""

    def __init__(self, date_string):
        # где date_string - строка с датой в формате: "DD.MM.YYYY"
        # здесь DD - день (целое число от 1 до 31);
        # MM - месяц (целое число от 1 до 12);
        # YYYY - год (целое число от 1 до 3000).
        DD, MM, YYYY = map(int, date_string.split('.'))
        if (type(DD) == int and 1 <= DD <= 31) and (type(MM) == int and 1 <= MM <= 12) and (
                type(YYYY) == int and 1 <= YYYY <= 3000):
            self.DD = DD
            self.MM = MM
            self.YYYY = YYYY
            self.date_string = f'{self.DD}.{self.MM}.{self.YYYY}'
        else:
            raise DateError("Неверный формат даты")

    def __str__(self):
        return f"{str(self.DD).rjust(2, '0')}.{str(self.MM).rjust(2, '0')}.{self.YYYY}"


class DateError(Exception):
    """Проверка формата даты"""


# здесь создавайте объект класса DateString и выполняйте обработку исключений
date_string = input()

try:
    d_s = DateString(date_string)
    print(d_s)
except DateError:
    print("Неверный формат даты")
