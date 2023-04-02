# TEST-TASK___________________________________
def test_6(Stack, StackObj):
    s = Stack()
    top = StackObj("obj_1")
    s.push(top)
    s.push(StackObj("obj_2"))
    s.push(StackObj("obj_3"))
    s.pop()

    res = s.get_data()
    assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
    assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

    h = s.top
    while h:
        res = h.data
        h = h.next

    s = Stack()
    top = StackObj("obj_1")
    s.push(top)
    s.pop()
    assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

    n = 0
    h = s.top
    while h:
        h = h.next
        n += 1

    assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

    s = Stack()
    top = StackObj("name_1")
    s.push(top)
    obj = s.pop()
    assert obj == top, "метод pop() должен возвращать удаляемый объект"
    print("Правильный ответ !!")
