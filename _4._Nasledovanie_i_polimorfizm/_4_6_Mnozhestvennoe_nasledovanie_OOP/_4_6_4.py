"""
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам.
Выполним такой пример.
Определите в программе классы в соответствии с их иерархией, представленной на схеме ниже:
                Digit(число)
                |
Integer,   Float,     Positive,      Negative
                   (положительное) (отрицательное)

Digit, Integer, Float, Positive, Negative
Каждый объект этих классов должен создаваться однотипной командой вида:
obj = Имя_класса(value)
где value - числовое значение.
В каждом классе следует делать свою проверку на корректность значения value:
- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:
raise TypeError('значение не соответствует типу объекта')

После этого объявите следующие дочерние классы:
PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями.
Сохраните все эти объекты в виде списка digits.
Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.
"""


class Digit:  # (число)
    def __init__(self, value):  # где value - числовое значение.
        self.value = value if self.verify_num(value) else None

    # В каждом классе следует делать свою проверку на корректность значения value:
    # - в классе Digit: value - любое число;
    def verify_num(self, num):
        """ проверка что число int или float"""
        if type(num) in (int, float):
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):  # int число
    # В каждом классе следует делать свою проверку на корректность значения value:
    # - в классе Integer: value - целое число;
    def verify_num(self, num):
        """Проверка, что число целое"""
        if type(num) == int:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):  # float число
    # В каждом классе следует делать свою проверку на корректность значения value:
    # - в классе Float: value - вещественное число;
    def verify_num(self, num):
        """Проверка, что число вещественное"""
        if type(num) == float:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):  # (положительное)
    # В каждом классе следует делать свою проверку на корректность значения value:
    # - в классе Positive: value - положительное число;
    def verify_num(self, num):
        """ Проверка, что число положительное"""
        if type(num) in (int, float) and num >= 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):  # (отрицательное)
    # В каждом классе следует делать свою проверку на корректность значения value:
    # - в классе Negative: value - отрицательное число.
    def verify_num(self, num):
        """Проверка, что число отрицательное"""
        if type(num) in (int, float) and num < 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


# После этого объявите следующие дочерние классы:
#
#
class PrimeNumber(Integer, Positive):  # - простые числа; наследуется от классов Integer и Positive;
    def verify_num(self, num):
        """Проверка, что число простое и положительное"""
        if type(num) in (int, float) and num >= 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


class FloatPositive(Float, Positive):  # - наследуется от классов Float и Positive.
    def verify_num(self, num):
        """Проверка, что float и положительное"""
        if type(num) in (int, float) and num >= 0:
            return True
        else:
            raise TypeError('значение не соответствует типу объекта')


# TEST
# a_int_float = Digit(10)
# b_int = Integer(5)
# c_float = Float(10.10)
# d_int_float_positive = Positive(6.6)
# e_nt_float_negative = Negative(-10.3)
# f_PrimeNumber = PrimeNumber(4)
# g_FloatPositive = FloatPositive(8.8)

# Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями.
# Сохраните все эти объекты в виде списка digits.
digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4),
          FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5), FloatPositive(3.5), FloatPositive(8.9)
          ]

# Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:
# - filter(function, iterable) - Возвращает итератор из тех элементов, для которых function возвращает истину.
# - isinstance(object, ClassInfo) - Истина, если объект является экземпляром ClassInfo или его подклассом.
# Если объект не является объектом данного типа, функция всегда возвращает ложь.

# lst_positive - все объекты, относящиеся к классу Positive;
lst_positive = list(filter(lambda x: x if isinstance(x, Positive) else None, digits))

# lst_float - все объекты, относящиеся к классу Float.
lst_float = list(filter(lambda x: x if isinstance(x, Float) else None, digits))
