# TEST-TASK___________________________________
def test_9(temp):
    try:
        assert len(temp) == 2 and \
               "на экране будет отображено значение 0" in temp and \
               "в строчке sp.ID_SHOP_ITEM += 1 создается новая локальная переменная ID_SHOP_ITEM со значением 1" in temp
    except:
        print("Пока неправильно попробуйте другие варианты. 9")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
