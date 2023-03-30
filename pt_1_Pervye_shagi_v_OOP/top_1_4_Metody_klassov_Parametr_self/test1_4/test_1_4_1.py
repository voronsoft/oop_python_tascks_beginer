# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 1 and "Любая (не статическая) функция, объявленная внутри класса" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print("Правильно так держать !")
