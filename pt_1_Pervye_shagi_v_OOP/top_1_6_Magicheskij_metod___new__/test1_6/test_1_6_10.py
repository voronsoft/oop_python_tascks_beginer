# TEST-TASK___________________________________
def test_10(Loader, Factory):
    ld = Loader()
    s = '4, 5, -6.5, -0.5'
    res = ld.parse_format(s, Factory())
    #
    assert hasattr(Factory, "build_sequence")
    assert hasattr(Factory, "build_number")
    #
    x = Factory()
    assert x.build_sequence() == [] and len(x.build_sequence()) == 0, \
        "ошибка, метод build_sequence должен возвращать пустой список"
    assert type(x.build_number('4.5')) == float and type(x.build_number('4')) == float, \
        "ошибка, метод build_number работает неправильно"
    print(f"Результат: {res}")
    print("Правильно, так держать !")
