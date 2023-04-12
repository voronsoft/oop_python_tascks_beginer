# TEST-TASK___________________________________
def test_8(CentralBank, MoneyR, MoneyE, MoneyD):
    bank = CentralBank()
    assert bank is None, "объекты CentralBank создаваться не должны"
    assert hasattr(CentralBank, "rates"), "в классе нет атрибута rates"
    assert type(CentralBank.rates) is dict, "rates должен быть словарём"
    assert CentralBank.rates['rub'] == 72.5 and CentralBank.rates['dollar'] == 1.0 and \
           CentralBank.rates['euro'] == 1.15, "ошибка в значениях валют"
    assert hasattr(CentralBank, "register") and callable(CentralBank.register), "вы не объявили метод - register"

    # проверка значений по умолчанию
    rub = MoneyR()  # с нулевым балансом
    assert rub.__dict__['_MoneyR__cb'] is None, "изначально __cb == None"
    assert rub.__dict__['_MoneyR__volume'] == 0, "если сумма не указана, то  __volume == 0"
    dl = MoneyD()  # с нулевым балансом
    assert dl.__dict__['_MoneyD__cb'] is None, "изначально __cb == None"
    assert dl.__dict__['_MoneyD__volume'] == 0, "если сумма не указана, то  __volume == 0"
    euro = MoneyE()  # с нулевым балансом
    assert euro.__dict__['_MoneyE__cb'] is None, "изначально __cb == None"
    assert euro.__dict__['_MoneyE__volume'] == 0, "если сумма не указана, то  __volume == 0"

    # проверка записи и считывания значений
    rub.cb = 111
    assert rub.__dict__["_MoneyR__cb"] == 111, "некорректно работает запись в значение cb"
    assert rub.cb == 111, "некорректно работает считывание значения из cb"
    rub.volume = 111
    assert rub.__dict__["_MoneyR__volume"] == 111, "некорректно работает запись в значение volume"
    assert rub.volume == 111, "некорректно работает считывание значения из volume"

    dl.cb = 111
    assert dl.__dict__["_MoneyD__cb"] == 111, "некорректно работает запись в значение cb"
    assert dl.cb == 111, "некорректно работает считывание значения из cb"
    dl.volume = 111
    assert dl.__dict__["_MoneyD__volume"] == 111, "некорректно работает запись в значение volume"
    assert dl.volume == 111, "некорректно работает считывание значения из volume"

    euro.cb = 111
    assert euro.__dict__["_MoneyE__cb"] == 111, "некорректно работает запись в значение cb"
    assert euro.cb == 111, "некорректно работает считывание значения из cb"
    euro.volume = 111
    assert euro.__dict__["_MoneyE__volume"] == 111, "некорректно работает запись в значение volume"
    assert euro.volume == 111, "некорректно работает считывание значения из volume"
    # end проверка записи и считывания значений

    rub = MoneyR()  # с нулевым балансом
    dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
    euro = MoneyE(100)  # с балансом в 100 евро

    assert isinstance(rub, MoneyR) and isinstance(dl, MoneyD) and isinstance(euro, MoneyE), \
        "необходимо создать 3 объекта rub, dl, euro"
    # проверка атрибутов в классах
    assert hasattr(rub, '_MoneyR__cb') and hasattr(rub, '_MoneyR__volume'), \
        "ошибка атрибуты должны быть приватными в объекте rub"
    assert hasattr(dl, '_MoneyD__cb') and hasattr(dl, '_MoneyD__volume'), \
        "ошибка атрибуты должны быть приватными в объекте dl"
    assert hasattr(euro, '_MoneyE__cb') and hasattr(euro, '_MoneyE__volume'), \
        "ошибка атрибуты должны быть приватными в объекте euro"

    # проверяем есть ли объекты свойства в классах для обращения к приватным атрибутам __cb / __volume
    assert isinstance(MoneyR.cb, property) and isinstance(MoneyR.volume, property), \
        "в классе MoneyR ошибка в наличии объектов свойств"
    assert isinstance(MoneyD.cb, property) and isinstance(MoneyD.volume, property), \
        "в классе MoneyD ошибка в наличии объектов свойств"
    assert isinstance(MoneyE.cb, property) and isinstance(MoneyE.volume, property), \
        "в классе MoneyE ошибка в наличии объектов свойств"

    # проверка работы register
    try:
        # попытка регистрации кошельков
        CentralBank.register(rub)
        CentralBank.register(dl)
        CentralBank.register(euro)
    except:
        print("произошла ошибка при регистрации кошельков")
    else:
        assert rub.cb == CentralBank and euro.cb == CentralBank and dl.cb == CentralBank, \
            "\nпри регистрации кошелька в банке, произошла ошибка в каком-то из кошельков\n" \
            "стоит проверить атрибут __cb в ваших кошельках или сам метод register\n" \
            "При регистрации значение __cb объекта money должно ссылаться на класс CentralBank"

    # проверка объявления методов в MoneyR
    assert hasattr(MoneyR, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyR"
    assert hasattr(MoneyR, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyR"
    assert hasattr(MoneyR, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyR"
    assert hasattr(MoneyR, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyR"
    assert hasattr(MoneyR, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyR"
    assert hasattr(MoneyR, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyR"
    # проверка объявления методов в MoneyD
    assert hasattr(MoneyD, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyD"
    assert hasattr(MoneyD, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyD"
    assert hasattr(MoneyD, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyD"
    assert hasattr(MoneyD, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyD"
    assert hasattr(MoneyD, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyD"
    assert hasattr(MoneyD, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyD"
    # проверка объявления методов в MoneyE
    assert hasattr(MoneyE, "__gt__"), "не объявлен метод __gt__ (>) в классе MoneyE"
    assert hasattr(MoneyE, "__lt__"), "не объявлен метод __lt__ (<) в классе MoneyE"
    assert hasattr(MoneyE, "__eq__"), "не объявлен метод __eq__ (==) в классе MoneyE"
    assert hasattr(MoneyE, "__ne__"), "не объявлен метод __ne__ (!=) в классе MoneyE"
    assert hasattr(MoneyE, "__ge__"), "не объявлен метод __ge__ (>=) в классе MoneyE"
    assert hasattr(MoneyE, "__le__"), "не объявлен метод __le__ (<=) в классе MoneyE"

    # проверка работы методов сравнения и т.д.
    assert dl > rub, "метод > работает некорректно"
    assert not dl < rub, "метод < работает некорректно"
    assert dl >= euro, "метод > работает некорректно"
    assert not dl <= euro, "метод > работает некорректно"
    assert rub != euro, "метод != работает некорректно"
    assert euro > rub, "метод > работает некорректно"
    assert euro < dl, "метод < работает некорректно"
    assert not euro > dl, "метод > работает некорректно"
    assert not dl < euro, "метод < работает некорректно"

    assert not rub == euro, "метод == работает некорректно"
    assert not dl == euro, "метод == работает некорректно"
    assert euro == euro, "метод == работает некорректно"

    # проверка вывода ошибки если кошелёк не зарегистрирован банке
    rub_test = MoneyR(72.5)
    try:
        rub_test == dl
    except ValueError:
        assert True
    else:
        assert False, "\nВы забыли учесть условие из задачи:\n" \
                      "Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:" \
                      "raise ValueError('Неизвестен курс валют.')"

    rub_test = MoneyR(72.5)
    CentralBank.register(rub_test)
    dl_test = MoneyD(1)
    CentralBank.register(dl_test)
    assert rub_test == dl_test, "\nскорее всего у вас проблема в понятии условия:\n" \
                                "- Значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)\n" \
                                "Пояснение:\n" \
                                "Означает, что при сравнении значений с определенным курсом валют, который устанавливается центральным банком,\n" \
                                "допускается погрешность в размере 0.1.\n" \
                                "Это означает, что если значения отличаются друг от друга на 0.1 или менее, то они считаются одинаковыми или эквивалентными\n" \
                                "с точки зрения сравнения по текущему курсу центрального банка.\n" \
                                "Если же разница между значениями больше чем 0.1, то эти значения считаются различными."
    rub_test = MoneyR(79.75)
    CentralBank.register(rub_test)
    assert not rub_test == dl_test, "\nскорее всего у вас проблема в понятии условия:\n" \
                                    "- Значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)\n" \
                                    "Пояснение:\n" \
                                    "Означает, что при сравнении значений с определенным курсом валют, который устанавливается центральным банком,\n" \
                                    "допускается погрешность в размере 0.1.\n" \
                                    "Это означает, что если значения отличаются друг от друга на 0.1 или менее, то они считаются одинаковыми или эквивалентными\n" \
                                    "с точки зрения сравнения по текущему курсу центрального банка.\n" \
                                    "Если же разница между значениями больше чем 0.1, то эти значения считаются различными."

    print("Вы справились !!!!!! Я просто в шоке ))))")
