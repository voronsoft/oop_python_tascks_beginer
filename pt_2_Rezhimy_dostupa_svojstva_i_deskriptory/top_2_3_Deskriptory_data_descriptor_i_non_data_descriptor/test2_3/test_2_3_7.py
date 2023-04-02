# TEST-TASK___________________________________
def test_7(ValidateString, RegisterForm, StringValue):
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

    print("Правильно, так держать !")
