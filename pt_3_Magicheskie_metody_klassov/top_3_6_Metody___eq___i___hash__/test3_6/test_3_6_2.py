# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 4 and \
               "hash('Balakirev')" in temp and \
               "hash((5, 4, 3.5))" in temp and \
               "hash(True)" in temp and \
               "hash(1024.56)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !!")
