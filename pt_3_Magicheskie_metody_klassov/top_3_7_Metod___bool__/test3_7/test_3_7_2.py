# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 2 and \
               "bool(user1) вернет значение True, так как будет вызван магический метод __bool__(), который вернет True" in temp and \
               "bool(user2) вернет значение False, так как будет вызван магический метод __bool__(), который вернет False" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно .")
