# TEST-TASK___________________________________
def test_2(rnd, lst_pass):
    assert len(lst_pass) == 3, "lst_pass содержит не 3 объекта"

    chrs, mi, ma = [_ for _ in rnd.__dict__.values()]
    assert all(all([True if i in chrs else False for i in _]) for _ in lst_pass), "пароль содержит недопустимые символы"

    assert all(mi <= len(_) <= ma for _ in lst_pass), " длинна пароля не в диапазоне допустимых величин"
    print("Правильный ответ все условия соблюдены !!")
