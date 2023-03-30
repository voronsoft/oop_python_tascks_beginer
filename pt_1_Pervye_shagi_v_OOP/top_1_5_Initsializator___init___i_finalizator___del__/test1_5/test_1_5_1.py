# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 1 and "__init__()" in temp
    except:
        print("Пока неправильно")
    else:
        print(temp[0])
        print("Правильно !")
