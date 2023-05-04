# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 1 and \
               "это когда один дочерний класс непосредственно наследуется от нескольких базовых" in temp

    except:
        print("Пока неправильно попробуйте другие варианты. 1")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
