# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 6 and \
               "__eq__()--оператор равенства ==" in temp and \
               "__ne__()--оператор неравенства !=" in temp and \
               "__lt__()--оператор меньше <" in temp and \
               "__le__()--оператор меньше или равно <=" in temp and \
               "__gt__()--оператор больше >" in temp and \
               "__ge__()--оператор больше или равно >=" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
