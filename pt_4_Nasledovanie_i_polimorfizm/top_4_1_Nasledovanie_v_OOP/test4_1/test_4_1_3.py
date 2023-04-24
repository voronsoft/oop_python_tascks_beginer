# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 4 and \
               "m = tb.model" in temp and \
               "rt.set_params('Home', 'red', 700, 1000)" in temp and \
               "color = rt.color" in temp and \
               "rt.set_model_and_color('Home', 'red')" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
