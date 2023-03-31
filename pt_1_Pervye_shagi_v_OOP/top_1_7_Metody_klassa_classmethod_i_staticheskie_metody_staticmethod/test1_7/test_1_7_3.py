# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 2 and "res = Math.sqrt(4)" in temp and "res = m.sqrt(2)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты...")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
