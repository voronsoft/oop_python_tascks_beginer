# TEST-TASK___________________________________
def test_8(DialogWindows, DialogLinux, Dialog, TYPE_OS):
    if TYPE_OS == 1:
        dlg_1 = Dialog("123")
        assert isinstance(dlg_1, DialogWindows), \
            "создаваемые объекты не соответствуют нужным классам DialogWindows или DialogLinux"

        assert dlg_1.name == "123", "неверное значение локального атрибута name класса DialogWindows"
        print("Правильно !")

    elif TYPE_OS == 2:
        dlg_2 = Dialog("1234")
        assert isinstance(dlg_2, DialogLinux), \
            "создаваемые объекты не соответствуют нужным классам DialogWindows или DialogLinux"

        assert dlg_2.name == "1234", "неверное значение локального атрибута name класса DialogLinux"
        print("Правильно !")
