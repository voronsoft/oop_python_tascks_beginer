# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 2 and \
               "исключения в процессе компиляции программы (синтаксические)" in temp and \
               "исключения в процессе выполнения программы (момента исполнения)" in temp


    except:
        print("Пока неправильно попробуйте другие варианты. 1")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
