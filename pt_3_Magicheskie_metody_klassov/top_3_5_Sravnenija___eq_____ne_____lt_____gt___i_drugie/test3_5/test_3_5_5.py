# TEST-TASK___________________________________
def test_5(stich, lst_text, StringText, lst_text_sorted):
    assert all([[True if i in _ else False for i in "–?!,.;"] for _ in stich]), \
        "в stich есть знаки которые нужно удалить - (–?!,.;)"
    assert len(lst_text) == 7 and all(
            True if isinstance(_, StringText) else False for _ in lst_text), "ошибка в lst_text"

    assert lst_text_sorted == ['Я к вам пишу чего же боле',
                               'Теперь я знаю в вашей воле',
                               'Но вы к моей несчастной доле',
                               'Что я могу еще сказать',
                               'Хоть каплю жалости храня',
                               'Вы не оставите меня',
                               'Меня презреньем наказать'], "неверно отсортирован список lst_text_sorted"

    assert lst_text[0] > lst_text[4] and lst_text[4] > lst_text[1], "метод > работает неверно"
    assert lst_text[1] < lst_text[4], "метод < работает неверно"

    assert lst_text[2] >= lst_text[4], "метод >= работает неверно"
    assert lst_text[2] <= lst_text[4], "метод >= работает неверно"

    print("Правильный ответ.")
