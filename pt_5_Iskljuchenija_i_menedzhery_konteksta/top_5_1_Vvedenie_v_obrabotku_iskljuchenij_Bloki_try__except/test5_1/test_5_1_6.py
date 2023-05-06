# TEST-TASK___________________________________
def test_6(temp):
    try:
        assert len(temp) == 2 and \
               "при вводе хотя бы одного не числового значения" in temp and \
               "при возникновении любых исключений, кроме исключения ZeroDivisionError" in temp

    except:
        print("Пока неправильно попробуйте другие варианты. 6")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
