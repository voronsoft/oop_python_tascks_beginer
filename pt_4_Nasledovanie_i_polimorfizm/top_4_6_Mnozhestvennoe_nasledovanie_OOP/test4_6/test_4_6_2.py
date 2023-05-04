# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 1 and \
               "C A B" in temp

    except:
        print("Пока неправильно попробуйте другие варианты. 2")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
