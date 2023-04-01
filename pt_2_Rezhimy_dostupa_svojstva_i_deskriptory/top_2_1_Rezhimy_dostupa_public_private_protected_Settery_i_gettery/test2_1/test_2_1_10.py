# TEST-TASK___________________________________
def test_10(EmailValidator):
    assert EmailValidator.check_email("sc_lib@list.ru") is True and \
           EmailValidator.check_email("sc_lib@list_ru") is False and \
           EmailValidator.check_email("sc@lib@list_ru") is False and \
           EmailValidator.check_email("sc.lib@list_ru") is False and \
           EmailValidator.check_email("sclib@list.ru") is True and \
           EmailValidator.check_email("sc.lib@listru") is False and \
           EmailValidator.check_email("sc..lib@list.ru") is False, "метод check_email отработал некорректно"

    m = EmailValidator.get_random_email()
    assert EmailValidator.check_email(m) is True, \
        "метод check_email забраковал сгенерированный email методом get_random_email"

    assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

    assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
    print("Правильный ответ !!")
