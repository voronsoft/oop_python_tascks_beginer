# TEST-TASK___________________________________
def test_4(temp):
    try:
        assert len(temp) == 4 and \
               "it = iter(g); res = next(g)" in temp and \
               "res = next(g); res = next(g)" in temp and \
               "for x in g: print(x)" in temp and \
               "res = next(g)" in temp and \
               "for x in g: print(x); for x in g: print(x)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно )")
