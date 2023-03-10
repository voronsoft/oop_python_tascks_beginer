"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/t8KuHjY71-o

Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами.
Объекты этого класса должны создаваться командой:

cm = Complex(real, img)
где real - действительная часть комплексного числа (целое или вещественное значение);
img - мнимая часть комплексного числа (целое или вещественное значение).
Объявите в этом классе следующие объекты-свойства (property):
real - для записи и считывания действительного значения;
img - для записи и считывания мнимого значения.
При записи новых значений необходимо проверять тип передаваемых данных.
Если тип не соответствует целому или вещественному числу, то генерировать исключение командой:
raise ValueError("Неверный тип данных.")

Также с объектами класса Complex должна поддерживаться функция:
res = abs(cm) возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img)
- корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).

Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8.
Затем, через объекты-свойства real и img измените эти значения на real = 3 и img = 4.
Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).

P.S. На экран ничего выводить не нужно.
"""
from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = self.validator(real)
        self.__img = self.validator(img)

    @staticmethod
    def validator(num):
        if type(num) in (int, float):
            return num
        else:
            raise ValueError("Неверный тип данных.")

    # PROPERTY   
    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.__real = self.validator(value)

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = self.validator(value)

    # END PROPERTY

    # Также с объектами класса Complex должна поддерживаться функция:
    # res = abs(cm) возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img)
    # - корень квадратный от суммы квадратов действительной и мнимой частей комплексного числа).   
    def __abs__(self):
        return abs(sqrt(self.real * self.real + self.img * self.img))


# TEST
# Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8.
# Затем, через объекты-свойства real и img измените эти значения на real = 3 и img = 4.
# Вычислите модуль полученного комплексного числа (сохраните результат в переменной c_abs).
cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
