# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 2 and "Stepik.get_certificate(st)" in temp and "st.get_certificate()" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
