# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 4 and "ld.json_parse()" in temp and "res = ld.json_parse()" in temp and \
               "Loader.json_parse()" in temp and "res = Loader.json_parse()" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
