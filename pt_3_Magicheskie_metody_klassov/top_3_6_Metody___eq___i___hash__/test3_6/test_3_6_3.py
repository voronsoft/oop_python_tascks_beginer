# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 1 and \
               "будет ошибка, что объекты p1 и p2 не хэшируемые" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !!")
