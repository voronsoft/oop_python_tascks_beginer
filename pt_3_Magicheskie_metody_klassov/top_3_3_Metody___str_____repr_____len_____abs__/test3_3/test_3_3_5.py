# TEST-TASK___________________________________
def test_5(LinkedList, ObjList):
    ln = LinkedList()
    ln.add_obj(ObjList("Сергей"))
    ln.add_obj(ObjList("Балакирев"))
    ln.add_obj(ObjList("Python ООП"))
    ln.remove_obj(2)
    assert len(
        ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
    ln.add_obj(ObjList("Python"))
    assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
    assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
    assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

    n = 0
    h = ln.head
    while h:
        assert isinstance(h, ObjList)
        h = h._ObjList__next
        n += 1

    assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

    n = 0
    h = ln.tail
    while h:
        assert isinstance(h, ObjList)
        h = h._ObjList__prev
        n += 1

    assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
    print("Хорошая работа !")
