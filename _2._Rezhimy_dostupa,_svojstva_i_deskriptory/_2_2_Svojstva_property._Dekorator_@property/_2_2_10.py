"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/TMPPmryMKD0

Подвиг 10 (на закрепление).
Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:
p = PhoneBook()
А сам класс должен иметь следующий набор методов:
add_phone(phone) - добавление нового номера телефона (в список);
remove_phone(indx) - удаление номера телефона по индексу списка;
get_phone_list() - получение списка из объектов всех телефонных номеров.

Каждый номер телефона должен быть представлен классом PhoneNumber.
Объекты этого класса должны создаваться командой:
note = PhoneNumber(number, fio)
где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
fio - Ф.И.О. владельца номера (строка).

В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
number - номер телефона (число);
fio - ФИО владельца номера телефона.

Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.

Пример использования классов (эти строчки в программе писать не нужно):
p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.
"""


# Класс PhoneBook
class PhoneBook:
    def __init__(self):
        self.phone_list = list()

    # А сам класс должен иметь следующий набор методов:
    def add_phone(self, phone):
        """add_phone(phone) - добавление нового номера телефона (в список)"""
        if phone.fio not in self.phone_list:
            self.phone_list.append(phone)

    def remove_phone(self, indx):
        """remove_phone(indx) - удаление номера телефона по индексу списка;"""
        del self.phone_list[indx]

    def get_phone_list(self):
        """Получение списка из объектов всех телефонных номеров."""
        return [_i for _i in self.phone_list]


# Класс классом PhoneNumber
class PhoneNumber:
    # В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
    # number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
    # fio - Ф.И.О. владельца номера (строка).
    def __init__(self, number=int(), fio=str()):
        if self.veryfi_number(number) and self.veryfi_fio(fio):
            self.number = number
            self.fio = fio
        else:
            self.number = int()
            self.fio = str()

    @classmethod
    def veryfi_number(cls, number):
        """Проверка number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра)"""
        return len(str(number)) == 11 and type(number) is int

    @classmethod
    def veryfi_fio(cls, fio):
        """Проверка fio - Ф.И.О. владельца номера (строка)"""
        return type(fio) is str and 0 < len(fio.split(' ')) <= 3


# ПРОВЕРКА

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
