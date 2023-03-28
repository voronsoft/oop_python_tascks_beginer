# TEST-TASK___________________________________
def test_5(temp):
    try:
        assert len(temp) == 1 and 'да, описать каждую книгу как объект класса "Книга" хорошая идея' in temp
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in temp]
        print()
        print('Правильно !')