"""
Объявите класс с именем Figure и двумя атрибутами:
type_fig: 'ellipse'
color: 'red'

Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color.
Присвойте переменной temp список всех локальных свойств (без значений) объекта fig1.
Запустите файл на исполнение
"""


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

# Удалите из экземпляра класса свойство color
del fig1.color
#
## Присвойте переменной temp список всех локальных свойств (без значений) объекта fig1.
temp = [i for i in fig1.__dict__]

# TEST-TASK___________________________________
try:
    issubclass(Figure, object)
except NameError:
    print("Вы не создали класс - Figure")

assert hasattr(Figure, "type_fig") and hasattr(Figure, "color")
assert isinstance(fig1, Figure), "не создан екземпляр класса fig1 с требуемыми параметрами"
assert len(temp) == 2 and "start_pt" in temp and "end_pt" in temp, \
    "В объекте fig1 неправильное количество локальных переменных или  имена переменных не соответствуют заданным "

assert len(fig1.__dict__) == 2 and fig1.start_pt == (10, 5) and fig1.end_pt == (
    100, 20), "В экземпляре класса должно быть 2 локальных атрибута start_pt и end_pt"

assert 'color' not in fig1.__dict__, "Локальный атрибут color должен быть удален из fig1"
print("Правильно !")
