# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 3 and \
               "класс RoundTable наследуется от класса Table" in temp and \
               "в созданном объекте rt формируются четыре локальных свойства: model, color, radius, height" in temp and \
               "параметры self в инициализаторе класса RoundTable и в инициализаторе класса Table ссылаются на один и тот же объект rt" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
