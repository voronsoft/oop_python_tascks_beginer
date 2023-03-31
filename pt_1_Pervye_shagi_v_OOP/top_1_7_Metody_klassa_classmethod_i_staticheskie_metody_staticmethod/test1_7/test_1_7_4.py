# TEST-TASK___________________________________
def test_4(temp):
    try:
        assert len(temp) == 1 and "Ссылка на класс Loader" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
