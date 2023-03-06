"""
Объявите класс с именем Figure и двумя атрибутами:
type_fig: 'ellipse'
color: 'red'

Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
start_pt: (10, 5)
end_pt: (100, 20)
color: 'blue'
Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств
(без значений) объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
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

# выведите на экран список всех локальных свойств
# (без значений) объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
for i in fig1.__dict__:
    print(i, end=' ')

# TEST-TASK___________________________________
assert issubclass(Figure, object), "Создайте класс - Figure"
assert hasattr(Figure, "type_fig") and hasattr(Figure, "color")
assert isinstance(fig1, Figure), "не создан екземпляр класса fig1 "
assert len(fig1.__dict__) and fig1.start_pt == (10, 5) and fig1.end_pt == (
100, 20), "В экземпляре класса должно быть 2 локальных атрибута start_pt и end_pt"
assert 'color' not in fig1.__dict__, "Локальный атрибут color должен быть удален из fig1"
