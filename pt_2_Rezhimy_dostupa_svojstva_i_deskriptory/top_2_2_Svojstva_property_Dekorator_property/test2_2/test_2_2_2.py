# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 5 and \
               "pr = property(get_pr, set_pr)" in temp and \
               "pr = property(get_pr, set_pr, del_pr)" in temp and \
               "pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr)" in temp and \
               "pr = property(); pr = pr.setter(set_pr); pr = pr.getter(get_pr); pr = pr.deleter(del_pr)" in temp and \
               "pr = property(get_pr)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !!")
