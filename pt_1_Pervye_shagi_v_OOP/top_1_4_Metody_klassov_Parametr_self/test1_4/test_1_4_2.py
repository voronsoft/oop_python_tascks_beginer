# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 1 and "Переменные и имена методов (ссылки на методы) класса" in temp
    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print("Правильно так держать !")
