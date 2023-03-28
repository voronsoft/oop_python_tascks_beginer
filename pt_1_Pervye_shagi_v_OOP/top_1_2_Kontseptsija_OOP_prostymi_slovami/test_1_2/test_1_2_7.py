# TEST-TASK___________________________________
def test_7(temp):
    try:
        assert len(temp) == 1 and 'да, ООП здесь может заметно упростить программный код' in temp
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in temp]
        print()
        print('Правильно !')