# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 2 and \
               "если объекты a == b, то hash(a) == hash(b)" in temp and \
               "если hash(a) != hash(b), то a != b" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
