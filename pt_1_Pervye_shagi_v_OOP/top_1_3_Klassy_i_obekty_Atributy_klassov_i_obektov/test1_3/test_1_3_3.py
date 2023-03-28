from top_1_3_Klassy_i_obekty._Atributy_klassov_i_obektov.task_1_3_3 import DataBase

# TEST-TASK___________________________________
def test_3():
    assert hasattr(DataBase, 'pk'), "В классе нет атрибута - pk"
    assert hasattr(DataBase, 'title'), "В классе нет атрибута - title"
    assert hasattr(DataBase, 'author'), "В классе нет атрибута - author"
    assert hasattr(DataBase, 'views'), "В классе нет атрибута - views"
    assert hasattr(DataBase, 'comments'), "В классе нет атрибута - comments"

    assert DataBase.pk == 1, "Значение атрибута неправильное"
    assert DataBase.title == "Классы и объекты", "Значение атрибута неправильное"
    assert DataBase.author == "Сергей Балакирев", "Значение атрибута неправильное"
    assert DataBase.views == 14356, "Значение атрибута неправильное"
    assert DataBase.comments == 12, "Значение атрибута неправильное"
    print("Правильно !")
