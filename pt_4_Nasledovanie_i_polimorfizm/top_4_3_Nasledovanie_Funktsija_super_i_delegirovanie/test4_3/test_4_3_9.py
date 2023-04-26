# TEST-TASK___________________________________
def test_9(StringDigit):
    sd = StringDigit("2455752345950")
    sd1 = sd + "123"
    sd2 = "123" + sd

    sd = StringDigit("123")
    assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

    try:
        sd2 = StringDigit("123a")
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    sd = sd + "345"
    assert sd == "123345", "неверно отработал оператор +"

    sd = "0" + sd
    assert sd == "0123345", "неверно отработал оператор +"

    try:
        sd = sd + "12d"
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

    try:
        sd = "12d" + sd
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

    print("Прекрасный ответ.")
