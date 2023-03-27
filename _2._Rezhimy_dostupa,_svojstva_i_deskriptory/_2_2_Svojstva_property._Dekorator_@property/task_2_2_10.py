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


# TEST-TASK___________________________________
p = PhoneBook()
assert hasattr(p, 'add_phone'), 'ошибка метод add_phone не существует в объекте класса'
assert hasattr(p, 'get_phone_list'), 'ошибка метод get_phone_list не существует в объекте класса'
assert hasattr(p, 'remove_phone'), 'ошибка метод remove_phone не существует в объекте класса'

p_num_1 = PhoneNumber(12345678901, "Фамилия")
assert str(p_num_1.number).isdigit() and len(str(p_num_1.number)) == 11, "Длинна телефонного номера должна быть 11 цифр"
assert type(p_num_1.fio) is str and len(p_num_1.fio) >= 3, "Ф.И.О должна быть строкой, длинна не меньше 3 букв"

a = PhoneNumber(21345678901, "Панда")
b = PhoneNumber(12345678901, "Фамилия")
p.add_phone(a)
p.add_phone(b)
# проверяем что все добавленные объекты в списке
lst_user = tuple(p.__dict__.keys())[0]  # определяем имя пользовательского списка с телефонами
assert len(p.__dict__[lst_user]) == 2, "Метод add_phone отработал не правильно"

# проверка получение списка из объектов всех телефонных номеров
assert len(p.get_phone_list()) == 2 and all(isinstance(_, PhoneNumber) for _ in p.get_phone_list()), \
    "метод get_phone_list отработал не правильно"

# проверка удаления по индексу
rmv_obj = p.__dict__[lst_user][1]  # определяем удаляемый объект
p.remove_phone(1)  # удаляем некий объект по индексу
# сравниваем удалили тот же объект или нет если в списке нет объекта rmv_obj то удаление работает правильно
assert rmv_obj not in p.__dict__[lst_user], "Метод remove_phone некорректно отработал !"

print("Правильный ответ !")
