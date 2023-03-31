"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/9766M0dS1qc

Подвиг 8.
Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
Этот класс должен иметь следующие методы:

check_card_number(number) - проверяет строку с номером карты и возвращает булево значение
True, если номер в верном формате и
False - в противном случае.
Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).

check_name(name) - проверяет строку name с именем пользователя карты.
Возвращает булево значение True, если имя записано верно и False - в противном случае.
Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.
Например, SERGEI BALAKIREV.

Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")

Для проверки допустимых символов в классе должен быть прописан атрибут:
CHARS_FOR_NAME = ascii_lowercase.upper() + digits
Подумайте, как правильнее объявить методы check_card_number и check_name
(декораторами @classmethod и @staticmethod).

P.S. В программе только объявить класс. На экран ничего выводить не нужно.
"""

from string import ascii_lowercase, digits


# ваш код:
class CardCheck:
    # Для проверки допустимых символов в классе должен быть прописан атрибут:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    def __init__(self, number, name):
        if self.check_card_number(number):
            self.number = number

        if self.check_name(name):
            self.name = name

    # check_card_number(number) - проверяет строку с номером карты и возвращает булево значение
    # True, если номер в верном формате и
    # False - в противном случае.
    # Формат номера следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9).
    @classmethod
    def check_card_number(cls, number):
        answer = False
        lst = [[k for k in i] for i in number.split('-')]
        if len(lst) == 4:
            for i in lst:
                if len(i) == 4:
                    for _ in i:
                        if _ in digits:
                            answer = True
                        else:
                            return False
                else:
                    return False
        return answer

    # check_name(name) - проверяет строку name с именем пользователя карты.
    # Возвращает булево значение True, если имя записано верно и False - в противном случае.
    # Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.
    # Например, SERGEI BALAKIREV.
    @classmethod
    def check_name(cls, name):
        answer = False
        lst = [i for i in name.split()]
        if len(name.split()) == 2:
            for i in lst:
                for _ in i:
                    if _ in cls.CHARS_FOR_NAME:
                        answer = True
                    else:
                        return False
        else:
            return False
        return answer


# Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# end ваш код

# TEST-TASK___________________________________
from test1_7.test_1_7_8 import test_8

test_8(CardCheck)
# END
