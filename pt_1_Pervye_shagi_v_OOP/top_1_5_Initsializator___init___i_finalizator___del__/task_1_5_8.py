"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/HbtVara1GPI

Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
cart = Cart()
Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
(объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.

В классе Cart объявить методы:
add(self, gd) - добавление в корзину товара, представленного объектом gd;
remove(self, indx) - удаление из корзины товара по индексу indx;
get_list(self) - получение из корзины товаров в виде списка из строк:

['<наименовние_1>: <цена_1>',
'<наименовние_2>: <цена_2>',
...
'<наименовние_N>: <цена_N>']

Объявите в программе следующие классы для описания товаров:
Table - столы;
TV - телевизоры;
Notebook - ноутбуки;
Cup - кружки.

Объекты этих классов должны создаваться командой:
gd = ИмяКласса(name, price)
Каждый объект классов товаров должен содержать локальные свойства:
name - наименование;
price - цена.

Создайте в программе объект cart класса Cart.
Добавьте в него:
два телевизора (TV),
один стол (Table),
два ноутбука (Notebook)
одну кружку (Cup).
Названия и цены придумайте сами.

P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.
"""


# ваш код:
# Объявите в программе класс Cart (корзина), объекты которого создаются командой:
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
# (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
class Cart:
    def __init__(self):
        self.goods = []

    # В классе Cart объявить методы:
    # add(self, gd) - добавление в корзину товара, представленного объектом gd;
    def add(self, gd):
        self.goods.append(gd)

    # remove(self, indx) - удаление из корзины товара по индексу indx;
    def remove(self, indx):
        self.goods.pop(indx)

    # get_list(self) - получение из корзины товаров в виде списка из строк:
    # ['<наименовние_1>: <цена_1>', '<наименовние_N>: <цена_N>']
    def get_list(self):
        # ["Память: " + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
        return list(map(lambda x: f'{x.name}: {x.price}', self.goods))


# Объявите в программе следующие классы для описания товаров:
# Объекты этих классов должны создаваться командой:
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
# name - наименование;
# price - цена.

# Table - столы;
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# TV - телевизоры;
class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Notebook - ноутбуки;
class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Cup - кружки.
class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Создайте в программе объект cart класса Cart.
cart = Cart()
# Добавьте в него:
# два телевизора (TV),
for i in ('tv1 1000', 'tv2 2000'):
    cart.add(TV(*i.split()))
# один стол (Table),
cart.add(Table('Стол', '555'))
# два ноутбука (Notebook)
for i in ('nout1 3000', 'nout2 4000'):
    cart.add(Notebook(*i.split()))
# одну кружку (Cup).
cart.add(Cup('Кружка', '100'))
# Названия и цены придумайте сами.
# Проверка сгенерированного списка товаров
# print(cart.get_list())
# end ваш код

# TEST-TASK___________________________________
from test1_5.test_1_5_8 import test_8

test_8(Cart, Table, TV, Notebook, Cup)
# END
