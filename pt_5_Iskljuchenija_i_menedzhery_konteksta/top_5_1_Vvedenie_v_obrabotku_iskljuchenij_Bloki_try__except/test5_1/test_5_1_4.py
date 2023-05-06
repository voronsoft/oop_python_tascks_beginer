# TEST-TASK___________________________________
def test_4(temp):
    try:
        assert len(temp) == 1 and \
               "ни в каких, так как класс ZeroDivisionError является дочерним по отношению к классу ArithmeticError" in temp

    except:
        print("Пока неправильно попробуйте другие варианты. 4")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
