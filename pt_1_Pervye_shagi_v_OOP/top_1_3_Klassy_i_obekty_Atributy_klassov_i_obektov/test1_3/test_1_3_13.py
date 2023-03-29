# TEST-TASK___________________________________
def test_13(temp):
    try:
        assert len(temp) == 2 and "delattr(Point, 'tp')" in temp and "del Point.tp" in temp
    except:
        print("Пока неправильно....")
    else:
        [print(_) for _ in temp]
        print("Правильно !!")
