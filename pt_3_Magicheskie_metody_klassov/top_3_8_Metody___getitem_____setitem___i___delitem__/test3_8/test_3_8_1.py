# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 6 and \
               "__getitem__()--получение значения по ключу item" in temp and \
               "__setitem__()--запись значения value по ключу key" in temp and \
               "__delitem__()--удаление элемента по ключу key" in temp and \
               "__setattr__()--вызывается при изменении атрибута класса или объекта" in temp and \
               "__getattribute__()--вызывается при обращении к атрибуту класса или объекта" in temp and \
               "__delattr__()--вызывается при удалении атрибута класса или объекта" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
