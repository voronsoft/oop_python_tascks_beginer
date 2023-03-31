# TEST-TASK___________________________________
def test_6(Factory, Loader, res):
    assert Factory.build_sequence() == [], 'Неправильно отработал метод build_sequence'
    assert type(Factory.build_number('10')) is int, 'Неправильно отработал метод build_number'

    try:
        assert res == [1, 2, 3, -5, 10]
    except:
        print("Ошибка, в переменной res неправильный результат")

    else:
        print("Правильно !")
