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


# ваш код
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
# Присвойте переменной temp список всех локальных свойств (без значений) объекта fig1.
temp = [i for i in fig1.__dict__]
# end ваш код

# TEST-TASK___________________________________
from test1_3.test_1_3_9 import test_9

test_9(Figure, fig1, temp)

# END
