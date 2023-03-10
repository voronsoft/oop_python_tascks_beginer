"""
Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"
Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:

dlg = Dialog(<название>)
Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
Класс Dialog должен создавать объекты:
класса DialogWindows, если переменная TYPE_OS = 1
и объекты класса DialogLinux, если переменная TYPE_OS не равна 1.
При этом, переменная TYPE_OS может меняться в последующих строчках программы.
Имейте это в виду, при объявлении класса Dialog.

P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.
"""
TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
# dlg = Dialog(<название>)
# Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
# Класс Dialog должен создавать объекты:
# класса DialogWindows, если переменная TYPE_OS = 1
# и объекты класса DialogLinux, если переменная TYPE_OS не равна 1.
# При этом, переменная TYPE_OS может меняться в последующих строчках программы.
# Имейте это в виду, при объявлении класса Dialog.


class Dialog:
    def __new__(cls, *args, **qargs):
        temp = None
        if TYPE_OS == 1:
            temp = super().__new__(DialogWindows)
        else:
            temp = super().__new__(DialogLinux)
        temp.name = args[0]
        return temp


# Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
dlg = Dialog('очко')

# TEST-TASK___________________________________
TYPE_OS = 1
dlg_1 = Dialog("123")
TYPE_OS = 2
dlg_2 = Dialog("1234")

assert isinstance(dlg_1, DialogWindows) and isinstance(dlg_2, DialogLinux), \
    "создаваемые объекты не соответствуют нужным классам DialogWindows или DialogLinux"

assert dlg_1.name == "123", "неверное значение локального атрибута name класса DialogWindows"
assert dlg_2.name == "1234", "неверное значение локального атрибута name класса DialogLinux"

d1 = Dialog("12")
d2 = Dialog("123")

assert d1.name == "12" and d2.name == "123", "неверные значения в локальных атрибутах name разных объектов класса DialogLinux"
print("Правильно !")
