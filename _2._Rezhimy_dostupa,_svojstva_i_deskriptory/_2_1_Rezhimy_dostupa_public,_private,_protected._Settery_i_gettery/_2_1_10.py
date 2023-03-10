"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HPgJtLb2NV8

Подвиг 10 (на повторение).
Объявите класс EmailValidator для проверки корректности email-адреса.
Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:
em = EmailValidator() # None

В самом классе реализовать следующие методы класса (@classmethod):
- get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
- check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.
Корректность строки email определяется по следующим критериям:
- допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
- длина email до символа @ не должна превышать 100 (сто включительно);
- длина email после символа @ не должна быть больше 50 (включительно);
- после символа @ обязательно должна идти хотя бы одна точка;
- не должно быть двух точек подряд.

Также в классе нужно реализовать приватный статический метод класса:
- is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
Если параметр email не является строкой, то check_email() возвращает False.

Пример использования класса EmailValidator (эти строчки в программе писать не нужно):
res = EmailValidator.check_email("sc_lib@list.ru") # True
res = EmailValidator.check_email("sc_lib@list_ru") # False
P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
"""
from string import ascii_lowercase, ascii_uppercase, digits
from random import randint, choice


class EmailValidator:
    chars_from_email = ascii_lowercase + ascii_uppercase + digits + '_.@'

    def __new__(cls, *args, **kwargs):
        return None

    # В самом классе реализовать следующие методы класса (@classmethod):
    # - get_random_email(cls) - для генерации случайного email-адреса по формату: xxxxxxx...xxx@gmail.com,
    # где x - любой допустимый символ в email (латинский буквы, цифры, символ подчеркивания и точка);
    #
    # S.join(список)	Сборка строки из списка с разделителем S
    # random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
    # S.replace(шаблон, замена[, max-count]) Замена шаблона на замену. max-count ограничивает количество замен
    # random.choice(sequence) - случайный элемент непустой последовательности.
    # random.sample(population, k) - список длиной k из последовательности population.
    @classmethod
    def get_random_email(cls):
        len_mail = randint(3, 100)
        email_random = ''.join([choice(cls.chars_from_email) for _ in range(len_mail)])
        email_random = email_random.replace('.', '')
        email_random = email_random.replace('@', '')
        return email_random + '@gmail.com'

    # - check_email(cls, email) - возвращает True, если email записан верно и False - в противном случае.
    # Корректность строки email определяется по следующим критериям:
    # - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
    # - длина email до символа @ не должна превышать 100 (сто включительно);
    # - длина email после символа @ не должна быть больше 50 (включительно);
    # - после символа @ обязательно должна идти хотя бы одна точка;
    # - не должно быть двух точек подряд.
    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            # - допустимые символы: латинский алфавит, цифры, символы подчеркивания, точки и собачка @ (одна);
            # sc_lib@list.ru
            if email.count('@') == 1 and email.count('.') == 1:
                for i in email:
                    if i not in cls.chars_from_email:
                        return False
                # - длина email до символа @ не должна превышать 100 (сто включительно);
                # - длина email после символа @ не должна быть больше 50 (включительно);
                # - не должно быть двух точек подряд
                if 0 < len(email.split('@')[0]) <= 100 and \
                        2 < len(email.split('@')[1]) <= 50 and \
                        email.index('@') < email.index('.'):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # Также в классе нужно реализовать приватный статический метод класса:
    # - is_email_str(email) - для проверки типа переменной email, если строка, то возвращается значение True, иначе - False.
    # Метод is_email_str() следует использовать в методе check_email() перед проверкой корректности email.
    # Если параметр email не является строкой, то check_email() возвращает False.
    @staticmethod
    def __is_email_str(email):
        return type(email) is str

# Проверка класса.
# Необходимо запретить создание объектов этого класса: при создании экземпляров должно возвращаться значение None, например:
# em = EmailValidator() # None
# Пример использования класса EmailValidator (эти строчки в программе писать не нужно):
# res = EmailValidator.check_email("sc_lib@list.ru")  # True
# res2 = EmailValidator.check_email("sc_lib@list_ru")  # False
# drand_mail = EmailValidator.get_random_email()
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.
