# TEST-TASK___________________________________
def test_6(temp):
    try:
        assert len(temp) == 1 and 'инкапсуляция' in temp
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in temp]
        print()
        print('Правильно !')
