# TEST-TASK___________________________________
def test_4(temp):
    try:
        assert len(temp) == 1 and "сначала всегда вызывается метод __new__(), затем метод __init__()" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
