# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 2 and "v1 == v2" in temp and "v1 != v2" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
