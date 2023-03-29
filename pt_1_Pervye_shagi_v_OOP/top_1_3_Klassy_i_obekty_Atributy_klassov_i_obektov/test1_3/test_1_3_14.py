# TEST-TASK___________________________________
def test_14(temp):
    try:
        assert len(temp) == 1 and "Ошибка, так как атрибут id отсутствует в классе Magazine" in temp
    except:
        print("Пока неправильно....")
    else:
        [print(_) for _ in temp]
        print("Правильно !!")
