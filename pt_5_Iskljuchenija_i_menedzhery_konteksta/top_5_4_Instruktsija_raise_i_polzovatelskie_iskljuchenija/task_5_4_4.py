"""
Подвиг 4. Объявите класс-исключение с именем StringException, унаследованным от базового класса Exception.
После этого объявите еще два класса-исключения:

NegativeLengthString - ошибка, если длина отрицательная;
ExceedLengthString - ошибка, если длина превышает заданное значение;

унаследованные от базового класса StringException.

Затем, в блоке try (см. программу) пропишите команду генерации исключения
для перехода в блок обработки исключения ExceedLengthString.
"""


# здесь объявляйте классы
class StringException(Exception):
    """ошибка, если длина отрицательная"""


class NegativeLengthString(StringException):
    """ошибка, если длина превышает заданное значение"""


class ExceedLengthString(StringException):
    ...


# TEST
try:
    raise ExceedLengthString  # здесь команда для генерации исключения
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString111")
except StringException:
    print("StringException")
