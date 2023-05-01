# TEST-TASK___________________________________
def test_7(Stack, StackInterface, StackObj):
    assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

    try:
        a = StackInterface()
        a.pop_back()
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"

    st = Stack()
    assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

    obj_top = StackObj("obj")
    st.push_back(obj_top)

    assert st._top == obj_top, "неверное значение атрибута _top"

    obj = StackObj("obj")
    st.push_back(obj)

    n = 0
    h = st._top
    while h:
        assert h._data == "obj", "неверные данные в объектах стека"
        h = h._next
        n += 1

    assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

    del_obj = st.pop_back()
    assert del_obj == obj, "метод pop_back возвратил неверный объект"

    del_obj = st.pop_back()
    assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

    assert st._top is None, "неверное значение атрибута _top"

    print("У вас все получилось !!")
