# TEST-TASK___________________________________
def test_8(temp):
    try:
        assert len(temp) == 1 and 'полиморфизм' in temp
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in temp]
        print()
        print('Правильно !')