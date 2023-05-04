# TEST-TASK___________________________________
def test_9(MoneyOperators, Money, MoneyR, MoneyD):
    assert issubclass(Money, object), "объявите Money как базовый класс"

    try:
        money = Money(10)
        money1 = Money(5.0)
    except:
        assert False, "ошибка при создании экземпляра класса с данными 10 или 10.0"
    else:
        assert True

    try:
        money_error = Money('qw')
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError"

    assert isinstance(Money.money, property), "в классе Money не найден объект-свойство money"
    assert '_money' in money.__dict__ and money._money == 10, "в экземпляре класса не найден локальный атрибут _money"

    assert money.money == 10, "при считывании значения атрибута _money произошла ошибка"

    money.money = 3
    assert money.money == 3, "при изменении значения атрибута _money произошла ошибка"

    m1 = MoneyR(100)
    m2 = MoneyD(2)

    assert isinstance(m1, Money) and isinstance(m1, MoneyOperators), \
        "MoneyR должен быть дочерним классом классов Money-MoneyOperators"

    try:
        m = m1 + 10
    except:
        assert False, "при операции m = m1 + 10 произошла ошибка"
    else:
        assert True

    try:
        m = m1 - 5.4
    except:
        assert False, "при операции m = m1 - 5.4 произошла ошибка"
    else:
        assert True

    try:
        m = m1 + m2  # TypeError
    except:
        assert True
    else:
        assert False, "при операции m = m1 + m2 произошла ошибка"

    import io
    import sys
    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    print(m)  # MoneyR: 11
    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    assert output == 'MoneyR: 94.6\n', "при операции print() получена неверная строка"
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние

    print("Здорово, всё верно. 9")
