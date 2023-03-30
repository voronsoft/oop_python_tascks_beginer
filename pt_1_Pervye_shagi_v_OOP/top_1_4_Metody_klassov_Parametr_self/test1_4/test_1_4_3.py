# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 1 and "это ссылка на объект класса, из которого был вызван метод" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print("Правильно !")
