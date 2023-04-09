# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 2 and "w = w1 + w2" in temp and "w1 += w2" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !!")
