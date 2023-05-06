"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/IexoPrHUSaA
Подвиг 4. Объявите класс с именем ValidatorString, объекты которого создаются командой:
vs = ValidatorString(min_length, max_length, chars)
где min_length, max_length - минимально и максимально допустимая длина строки
(целые числа, формируемые диапазон [min_length; max_length]);
chars - строка из набора символов (хотя бы один из них должен присутствовать в проверяемой строке).
Если chars - пустая строка, то проверку на вхождение символов не делать.

В самом классе ValidatorString объявите метод:

def is_valid(self, string): ...

который проверяет строку string на соответствие критериям: string должна быть строкой,
с длиной в диапазоне [min_length; max_length] и в string присутствует хотя бы один символ из chars.
Если хотя бы один из этих критериев не выполняется, то генерируется исключение командой:
raise ValueError('недопустимая строка')

Затем, объявите класс с именем LoginForm, объекты которого создаются командой:
lg = LoginForm(login_validator, password_validator)
где login_validator - валидатор для логина (объект класса ValidatorString);
password_validator - валидатор для пароля (объект класса ValidatorString).
В самом классе LoginForm объявите следующий метод:
def form(self, request): ...
где request - объект запроса (словарь).
В словаре request должен быть ключ 'login' со значением введенного логина (строки) и
ключ 'password' со значением введенного пароля (строка). Если хотя бы одного ключа нет,
то генерировать исключение командой:
raise TypeError('в запросе отсутствует логин или пароль')
В противном случае (если проверка для request прошла),
проверять корректность полученного формой логина и пароля с помощью валидаторов,
указанных в параметрах login_validator и password_validator, при создании объекта формы.
Если логин/пароль введены верно, то в объекте класса LoginForm локальным атрибутам _login и _password
присвоить соответствующие значения.

Пример использования классов (эти строчки должны быть в программе):

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
Sample Input:

sergey balakirev!
Sample Output:

sergey
"""


# здесь объявляйте классы
class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = str(chars)

    def is_valid(self, string):

        if len(self.chars) > 0 and any([True if i in self.chars else False for i in string]) and isinstance(string,
                                                                                                            str) and self.min_length <= len(
            string) <= self.max_length:
            return string
        elif len(self.chars) == 0 and isinstance(string, str) and self.min_length <= len(string) <= self.max_length:
            return string
        else:
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator  # валидатор для логина (объект класса ValidatorString)
        self.password_validator = password_validator  # валидатор для пароля (объект класса ValidatorString)

    def form(self, request):
        if isinstance(request, dict) and all([True if i in request else False for i in ('login', 'password')]) and all(
                True if type(i) is str else False for i in request.values()):
            self._login = self.login_validator.is_valid(request['login'])
            self._password = self.password_validator.is_valid(request['password'])
        else:
            raise TypeError('в запросе отсутствует логин или пароль')


# TEST
login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
