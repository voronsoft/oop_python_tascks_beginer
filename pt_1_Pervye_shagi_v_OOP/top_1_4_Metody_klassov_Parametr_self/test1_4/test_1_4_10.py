# TEST-TASK___________________________________
def test_10(Translator, tr, output):
    assert hasattr(Translator, 'add'), 'объявите метод - add'
    assert hasattr(Translator, 'remove'), 'объявите метод - remove'
    assert hasattr(Translator, 'translate'), 'объявите метод - translate'

    assert tr.translate('go') == ['идти', 'ехать', 'ходить'] and len(tr.translate('go')) == 3, \
        "не все связки добавленны"

    tr.add(*'go - ехать'.split(' - '))
    assert tr.translate('go') == ['идти', 'ехать', 'ходить'], "метод add отработал некорректно"

    tr.add(*'go - нестись'.split(' - '))
    assert tr.translate('go') == ['идти', 'ехать', 'ходить', 'нестись'] and len(tr.translate('go')) == 4, \
        "не все связки добавленны"

    try:
        tr.translate('car')
    except KeyError:
        assert True
    else:
        assert False, "вы неудалили связку для car"

    assert output == 'идти ехать ходить\n', \
        "Формат вывода неправильный.\nВ консоль должна напечататься строка:\nидти ехать ходить"

    print(output)
    print("Правильно !")
