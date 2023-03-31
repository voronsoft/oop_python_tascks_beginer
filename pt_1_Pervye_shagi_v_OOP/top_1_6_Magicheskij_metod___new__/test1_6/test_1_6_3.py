# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 1 and "ссылка на класс, для которого создается объект" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
