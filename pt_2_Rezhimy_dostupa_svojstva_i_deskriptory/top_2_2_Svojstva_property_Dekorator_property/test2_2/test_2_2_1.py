# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 3 and \
               "для считывания информации из локальной переменной __money достаточно записать res = m.money" in temp and \
               "в строчке money = property(get_money, set_money) создается объект-свойство с геттером get_money и сеттером set_money" in temp and \
               "в строчке m.money = 10 происходит вызов метода set_money и локальной переменной __money присваивается значение 10" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
