# TEST-TASK___________________________________
def test_10(FileDialogFactory, WindowsFileDialog, LinuxFileDialog):
    assert hasattr(FileDialogFactory, "create_windows_filedialog"), "не найден метод create_windows_filedialog"

    dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))

    assert isinstance(dlg, WindowsFileDialog), "ошибка, вернулся объект не того класса"


def test_10a(FileDialogFactory, WindowsFileDialog, LinuxFileDialog):
    assert hasattr(FileDialogFactory, "create_linux_filedialog"), "не найден метод create_linux_filedialog"

    dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))

    assert isinstance(dlg, LinuxFileDialog), "ошибка, вернулся объект не того класса"

    print("Правильно, вы закончили главу, поздравляю!")
