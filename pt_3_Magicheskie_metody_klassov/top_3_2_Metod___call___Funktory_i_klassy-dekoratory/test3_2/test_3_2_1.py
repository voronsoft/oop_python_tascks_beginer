# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 1 and \
               "позволяет вызывать объекты класса подобно функциям, в котором определен метод __call__()" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно ! )")
