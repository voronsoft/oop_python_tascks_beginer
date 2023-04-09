# TEST-TASK___________________________________
def test_6(Stack, StackObj):
    assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

    st = Stack()
    top = StackObj("1")
    st.push_back(top)
    assert st.top == top, "неверное значение атрибута top"

    st = st + StackObj("2")
    st = st + StackObj("3")
    obj = StackObj("4")
    st += obj

    st = st * ['data_1', 'data_2']
    st *= ['data_3', 'data_4']

    d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
    h = top
    i = 0
    while h:
        assert h._StackObj__data == d[
            i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
        h = h._StackObj__next
        i += 1

    assert i == len(d), "неверное число объектов в стеке"

    print("Правильный ответ, браво !")
