"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/AVh6hs06oCU

Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию.
Для этого вам поручается разработать базовый класс Test для всех видов тестов, объекты которого создаются командой:
test = Test(descr)
где descr - формулировка теста (строка). Если длина строки descr меньше 10 или больше 10 000 символов, то генерировать исключение командой:
raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
В самом классе Test должен быть объявлен абстрактный метод:
def run(self): ...
который должен быть переопределен в дочернем классе. Если это не так, то должно генерироваться исключение командой:
raise NotImplementedError

Далее, объявите дочерний класс с именем TestAnsDigit для тестирования правильного введенного числового ответа на вопрос теста.
Объекты класса TestAnsDigit должны создаваться командой:
test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность в указании числового ответа
(необходимо для проверки корректности вещественных чисел, по умолчанию принимает значение 0.01).
Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit больше или равно нулю),
то генерировать исключение командой:
raise ValueError('недопустимые значения аргументов теста')
В классе TestAnsDigit переопределите метод:
def run(self): ...
который должен читать строку из входного потока (ответ пользователя) командой:
ans = float(input()) # именно такой командой, ее прописывайте в методе run()
и возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону [ans_digit-max_error_digit; ans_digit+max_error_digit].
Иначе возвращается булево значение False.

Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается сам тест с помощью команд:
descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, а аргумент max_error_digit должен принимать значение по умолчанию 0.01.

Запустите тест командой run() и выведите на экран результат его работы (значение True или False).
Если в процессе создания объекта класса TestAnsDigit или в процессе работы метода run() возникли исключения,
то они должны быть обработаны и на экран выведено сообщение, содержащееся в исключении.

Sample Input:
Какое значение получим, при выполнении команды int(5.7)? | 5
6
Sample Output:
False
"""


class Test():
    def __init__(self, descr):
        if isinstance(descr, str) and 10 <= len(descr) <= 10000:
            self.description = descr
        else:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if all(True if type(i) in (int, float) else False for i in (ans_digit, max_error_digit)) and \
                max_error_digit >= 0:
            self.ans_digit = ans_digit
            self.max_error_digit = max_error_digit
        else:
            raise ValueError('недопустимые значения аргументов теста')

    def run(self):
        ans = float(input())  # именно такой командой, ее прописывайте в методе run()
        if self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit:
            return True
        else:
            return False


# MY TEST
descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
try:
    test = TestAnsDigit(descr, ans)
    print(test.run())
except ValueError as err:
    print(err)

# # TEST Balakirev
# try:
#     test = Test('descr')
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"
# 
# try:
#     test = Test('descr ghgfhgjg ghjghjg')
#     test.run()
# except NotImplementedError:
#     assert True
# else:
#     assert False
# #
# assert issubclass(TestAnsDigit, Test)
# #
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
# t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)
# #
# try:
#     t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
# except ValueError:
#     assert True
# else:
#     assert False
