# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(temp) == 3 and "if book: ..." in temp and "while book: ..." in temp and "res = bool(book)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно .")
