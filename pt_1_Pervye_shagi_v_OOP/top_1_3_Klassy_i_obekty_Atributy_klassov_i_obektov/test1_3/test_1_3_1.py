# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 3 and "SergeyBalakirev" in temp and "Data123" in temp and "DataBase" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
