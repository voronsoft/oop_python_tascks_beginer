# TEST-TASK___________________________________
def test_9(pt, pt_clone):
    assert id(pt) != id(pt_clone), "Ошибка, два объекта имеют одинаковый id. " \
                                   "Нужно что бы объекты были разные, но с одинаковыми данными"
    assert hasattr(pt, 'x') and hasattr(pt, 'y'), "в объекте должны быть 2 атрибута x и y"
    assert hasattr(pt_clone, 'x') and hasattr(pt_clone, 'y'), "в объекте должны быть 2 атрибута x и y"
    assert pt.x == pt_clone.x and pt.y == pt_clone.y, "Атрибуты имеют разные значения"
    print("Правильный ответ !")
