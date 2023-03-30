# TEST-TASK___________________________________
def test_9(head_obj, ListObject, lst_in):
    assert isinstance(head_obj, ListObject) and hasattr(ListObject, 'link')

    lst_data = []
    h = head_obj
    while h:
        lst_data.append(h.data)
        h = h.next_obj

    assert lst_in == lst_data, "данные в объектах ListObject не совпадают с прочитанными данными (списком lst_in)"
    print("Правильно !")
