# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 3 and \
               "в классе IPhone выполняется переопределение метода get_info()" in temp and \
               "класс IPhone расширяет класс SmartPhone" in temp and \
               "в методе get_info() класса IPhone выполняется делегированый вызов метода get_info() класса SmartPhone" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
