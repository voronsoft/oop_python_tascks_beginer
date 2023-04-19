# TEST-TASK___________________________________
def test_6(Stack, StackObj):
    st = Stack()
    st.push(StackObj("obj11"))
    st.push(StackObj("obj12"))
    st.push(StackObj("obj13"))
    st[1] = StackObj("obj2-new")
    assert st[0].data == "obj11" and st[
        1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

    try:
        obj = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    obj = st.pop()
    assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

    n = 0
    h = st.top
    while h:
        assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
        n += 1
        h = h.next

    assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

    print("Правильный ответ, так держать !")
