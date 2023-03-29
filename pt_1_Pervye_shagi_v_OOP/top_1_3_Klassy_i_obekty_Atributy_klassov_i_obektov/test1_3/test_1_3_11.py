# TEST-TASK___________________________________
def test_11(temp):
    try:
        assert len(temp) == 1 and 'red' in temp
    except:
        print("Пока не правильно")
    else:
        [print(_) for _ in temp]
        print("Правильно.")
