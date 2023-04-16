# TEST-TASK___________________________________
def test_5(MailBox, lst_in, MailItem, inbox_list_filtered):
    mail_box = MailBox()
    assert hasattr(mail_box, "inbox_list"), "в каждом объекте должен быть публичный атрибут inbox_list"
    assert hasattr(mail_box, "receive") and callable(mail_box.receive), "необходимо объявить метод - receive"

    mail_box.receive(lst_in)
    assert len(mail_box.inbox_list) == 3 and all(
            True if isinstance(_, MailItem) else False for _ in mail_box.inbox_list), \
        "метод receive отработал с ошибкой"

    temp = mail_box.inbox_list[0]
    assert hasattr(temp, "mail_from") and hasattr(temp, "title") and hasattr(temp, "content")
    assert hasattr(temp, "is_read") and type(temp.is_read) is bool, "что-то не так с атрибутом is_read"
    assert hasattr(temp, "set_read") and callable(temp.set_read), "что-то не так с set_read "
    assert hasattr(MailItem, "__bool__"), "метод bool не объявлен"

    assert mail_box.inbox_list[0].is_read is False, \
        "начальное значение is_read, у первого и последнего объектов должны быть False если не прочитаны"
    assert mail_box.inbox_list[-1].is_read is False, \
        "начальное значение is_read, у первого и последнего объектов должны быть False если не прочитаны"
    mail_box.inbox_list[0].set_read(True)
    mail_box.inbox_list[-1].set_read(True)
    assert mail_box.inbox_list[0].is_read is True, \
        "ошибка в методе set_read при установке значения что письмо прочитано "
    assert mail_box.inbox_list[-1].is_read is True, \
        "ошибка в методе set_read при установке значения что письмо прочитано "

    assert mail_box.inbox_list[0].is_read is True, "значение атрибута is_read неверное в первом объекте почтового ящика"
    assert mail_box.inbox_list[
               -1].is_read is True, "значение атрибута is_read неверное в последнем объекте почтового ящика"

    # Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных писем,
    # используя стандартную функцию filter() совместно с функцией bool() языка Python.
    assert all(_.is_read for _ in inbox_list_filtered), \
        "при фильтрации функцией filter список содержит объекты которые не прочитаны"
    print("Правильное решение.")
