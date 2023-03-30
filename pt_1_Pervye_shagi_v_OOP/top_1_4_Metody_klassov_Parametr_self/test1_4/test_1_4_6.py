# TEST-TASK___________________________________
def test_6(temp):
    try:
        assert len(temp) == 2 and "my_st.next_task()" in temp and "Stepik.next_task(my_st)" in temp
    except:
        print("Неправильно, попробуйте снова")
    else:
        [print('-', _) for _ in temp]
        print("Правильно !")
