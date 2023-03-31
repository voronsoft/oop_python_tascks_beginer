# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 1 and "адрес нового созданного объекта" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
