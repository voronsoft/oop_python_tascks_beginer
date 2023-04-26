# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 3 and \
               "дочерний класс SmartPhone расширяет базовый класс Phone" in temp and \
               "в классе SmartPhone выполняется переопределение метода get_info()" in temp and \
               "класс SmartPhone наследуется от класса Phone" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.1")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
