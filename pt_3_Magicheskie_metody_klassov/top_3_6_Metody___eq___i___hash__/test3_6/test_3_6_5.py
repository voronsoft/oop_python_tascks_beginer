# TEST-TASK___________________________________
def test_5(temp):
    try:
        assert len(temp) == 1 and \
               "словарь будет успешно создан и к его значениям можно обращаться, например, командой: d[id1].id" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !!")
