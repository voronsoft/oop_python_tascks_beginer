# TEST-TASK___________________________________
def test_7(x, temp):
    Dictionary = x
    try:
        issubclass(Dictionary, object)
    except NameError:
        print("Вы не создали класс - Dictionary")

    assert hasattr(Dictionary, 'rus') and hasattr(Dictionary, 'eng'), "В классе должно быть два атрибута - rus, eng"
    assert hasattr(Dictionary, 'rus_word') is False, "Атрибута rus_word не должно быть в классе"
    assert temp is False, "Значение присвоенное переменной temp неверное !!"
    print('Всё правильно, так держать !')
