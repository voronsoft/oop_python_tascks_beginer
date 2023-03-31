# TEST-TASK___________________________________
def test_11(Viber, Message):
    assert hasattr(Viber, 'show_last_message'), "отсутствует метод show_last_message"

    msg = Message("Всем привет!")
    Viber.add_message(msg)
    assert Viber.total_messages() == 1, "сообщение не было добавлено: некорректно работает метод add_message"

    Viber.add_message(Message("Это курс по Python ООП."))
    Viber.add_message(Message("Что вы о нем думаете?"))
    assert Viber.total_messages() == 3, "неверное число сообщений: некорректно работает метод add_message"

    assert msg.fl_like == False, "лайка по умолчанию не должно быть - значение False"
    Viber.set_like(msg)
    assert msg.fl_like == True, "лайк не проставился: некорректно работает метод set_like"
    Viber.set_like(msg)
    assert msg.fl_like == False, "лайк не убрался при повторном вызове метода set_like"
    Viber.remove_message(msg)

    assert Viber.total_messages() == 2, "неверное число сообщений: некорректно работает метод remove_message"
    print('Правильный ответ !!')
