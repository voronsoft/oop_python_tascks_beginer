# TEST-TASK___________________________________
def test_8(CardCheck):
    assert issubclass(CardCheck, object), 'не объявлен класс CardCheck'
    assert hasattr(CardCheck, 'check_card_number'), 'Отсутствует метод check_card_number'
    assert hasattr(CardCheck, 'check_name'), 'Отсутствует метод check_name'

    assert CardCheck.check_card_number("1234-5678-9012-0000"), 'Метод работает неправильно'
    assert CardCheck.check_card_number("12345678-9012-0000") is False, 'Метод работает неправильно'

    assert CardCheck.check_name("SERGEI BALAKIREV"), 'Метод check_name работает неправильно'
    assert CardCheck.check_name("фы фвв") is False, 'Метод check_name работает неправильно'
    print('Правильный ответ !')
