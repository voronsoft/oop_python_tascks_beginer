"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/zCD5_APRzes

Подвиг 7.
- Объявите класс ValidateString для проверки корректности переданной строки.
Объекты этого класса создаются командой:
validate = ValidateString(min_length=3, max_length=100)
где min_length - минимальное число символов в строке;
max_length - максимальное число символов в строке.
В классе ValidateString должен быть реализован метод:
validate(self, string) - возвращает True, если string является строкой (тип str) и длина строки в пределах [min_length; max_length].
Иначе возвращается False.

- Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:
st = StringValue(validator=ValidateString(min_length, max_length))
При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString)
и с помощью метода validate() проверяться корректность присваиваемых данных.
Если данные некорректны, то присвоение не выполняется (игнорируется).

- Объявите класс RegisterForm с тремя объектами дескриптора StringValue:
login = StringValue(...) - для ввода логина;
password = StringValue(...)  - для ввода пароля;
email = StringValue(...)  - для ввода Email.
Объекты класса RegisterForm создаются командой:
form = RegisterForm(логин, пароль, email)
где логин, пароль, email - начальные значения логина, пароля и Email.
В классе RegisterForm также должны быть объявлены методы:
get_fields() - возвращает список из значений полей в порядке [login, password, email];
show() - выводит в консоль многострочную строку в формате:

<form>
Логин: <login>
Пароль: <password>
Email: <email>
</form>

P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


class ValidateString:
    """Проверка, что значение является str, и в пределах допустимой длинны"""

    def __init__(self, min_length=3, max_length=100):
        """Инициализатор параметров длинны строки"""
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        """Возвращает True, если string является строкой (тип str) и длина 3-100 знаков. Иначе возвращается False."""
        return type(string) is str and self.min_length <= len(string) <= self.max_length


# descriptor
class StringValue:
    """Объявите дескриптор данных StringValue для работы со строками, объекты которого создаются командой:
    st = StringValue(validator=ValidateString(min_length, max_length))
    При каждом присвоении значения объекту st должен вызываться валидатор (объект класса ValidateString)
    и с помощью метода validate() проверяться корректность присваиваемых данных.
    Если данные некорректны, то присвоение не выполняется (игнорируется)."""

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        """Создает имя переменной"""
        self.name = "_" + name

    def __get__(self, instance, owner):
        """Getter descriptor"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Setter descriptor"""
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    """Объявите класс RegisterForm с тремя объектами дескриптора StringValue:
    login = StringValue(...) - для ввода логина;
    password = StringValue(...)  - для ввода пароля;
    email = StringValue(...)  - для ввода Email.
    Объекты класса RegisterForm создаются командой:
    form = RegisterForm(логин, пароль, email)
    где логин, пароль, email - начальные значения логина, пароля и Email.
    В классе RegisterForm также должны быть объявлены методы:
    get_fields() - возвращает список из значений полей в порядке [login, password, email];
    show() - выводит в консоль многострочную строку в формате:"""

    login = StringValue(validator=ValidateString())  # - для ввода логина;
    password = StringValue(validator=ValidateString())  # - для ввода пароля;
    email = StringValue(validator=ValidateString())  # - для ввода Email.

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        """Возвращает список из значений полей в порядке [login, password, email]:"""
        return [self.login, self.password, self.email]

    def show(self):
        """show() - выводит в консоль многострочную строку"""
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


# TEST-TASK___________________________________
assert hasattr(ValidateString, 'validate'), "в классе ValidateString отсутствует метод validate"

r = RegisterForm('11111', '1111111', '11111111')
assert hasattr(r, 'login') and hasattr(r, 'password') and hasattr(r,
                                                                  'email'), "в классе RegisterForm должны быть дескрипторы login, password, email"

assert hasattr(RegisterForm, 'show'), "в классе RegisterForm отсутствует метод show"

frm = RegisterForm("123", "2345", "sc_lib@list.ru")
assert frm.get_fields() == ["123", "2345", "sc_lib@list.ru"], "метод get_fields вернул неверные данные"

frm.login = "root"
assert frm.login == "root", "дескриптор login вернул неверные данные"

v = ValidateString(5, 10)
assert v.validate("hello"), "метод validate вернул неверное значение"
assert v.validate("hell") == False, "метод validate вернул неверное значение"
assert v.validate("hello world!") == False, "метод validate вернул неверное значение"


class A:
    st = StringValue(validator=ValidateString(3, 10))


a = A()
a.st = "hello"

assert a.st == "hello", "дескриптор StringValue вернул неверное значение"
a.st = "d"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной меньше min_length"
a.st = "dапарпаропропропропр"
assert a.st == "hello", "дескриптор StringValue сохранил строку длиной больше max_length"
a.st = "dапарпароп"
assert a.st == "dапарпароп", "дескриптор StringValue сохранил строку длиной больше max_length"

# код не менять !!!
import io
import sys

# Создаю объект StringIO
output = io.StringIO()
# Перенаправляю стандартный вывод в StringIO
sys.stdout = output
# END !!!
r.show()
# Получите данные из StringIO
output_str = output.getvalue()
# Верните стандартный вывод
sys.stdout = sys.__stdout__

assert output_str == '<form>\nЛогин: 11111\nПароль: 1111111\nEmail: 11111111\n</form>\n', "Метод show вывел данные в неправильном формате"

print("Правильно !")
