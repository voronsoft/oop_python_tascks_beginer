# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 2 and \
               "приватная переменная __model доступна только внутри класса Phone и недоступна в классе SmartPhone" in temp and \
               "в момент вызова метода get_info() произойдет ошибка, так как локальный атрибут __model отсутствует в классе SmartPhone" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
