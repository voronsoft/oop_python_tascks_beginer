# TEST-TASK___________________________________
def test_8(Stack, StackObj):
    st = Stack()
    st.push_back(StackObj("1"))
    st.push_front(StackObj("2"))

    assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

    st[0] = "0"
    assert st[
               0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

    for obj in st:
        assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

    try:
        a = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"
    print("Вы справились !!")
