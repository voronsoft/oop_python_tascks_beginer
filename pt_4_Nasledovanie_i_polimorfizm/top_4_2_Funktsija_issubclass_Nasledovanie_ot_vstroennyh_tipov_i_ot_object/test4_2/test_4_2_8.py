# TEST-TASK___________________________________
def test_8(temp):
    try:
        assert len(temp) == 4 and \
               "функция isinstance(obj, cls) возвращает True, если объект obj является объектом класса cls" in temp and \
               "функция issubclass(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
