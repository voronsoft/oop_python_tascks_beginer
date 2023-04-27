# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 3 and \
               "метод __verify_weight() класса BMW недоступен по этому имени в базовом классе Auto" in temp and \
               "метод __verify_model() класса Auto недоступен по этому имени в дочернем классе BMW" in temp and \
               "атрибуты __MIN_WEIGHT и __MAX_WEIGHT доступны только внутри класса Auto" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
