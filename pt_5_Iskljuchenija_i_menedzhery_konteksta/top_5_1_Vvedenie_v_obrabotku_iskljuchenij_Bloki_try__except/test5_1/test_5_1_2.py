# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 1 and \
               "при вводе любых не числовых значений" in temp

    except:
        print("Пока неправильно попробуйте другие варианты. 2")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
