# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 2 and \
               "res = next(g); res = next(g)" in temp and \
               "res = next(g)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно )")
