"""
Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета.
Для этого в программе объявите два класса с именами:

-Budget - для управления семейным бюджетом;
-Item - пункт расходов бюджета.

Объекты класса Item должны создаваться командой:
it = Item(name, money)
name - название статьи расхода;
money - сумма расходов (вещественное или целое число).
Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты
name и money с переданными значениями.

Объекты класса Budget создаются командой:
my_budget = Budget()
А сам класс Budget должен иметь следующие методы:
-add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
-remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
-get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).

Также с объектами класса Item должны выполняться следующие операторы:
-s = it1 + it2 # сумма для двух статей расходов
и в общем случае:
-s = it1 + it2 + ... + itN # сумма N статей расходов
При суммировании оператор + должен возвращать число
(вычисленную сумму по атрибутам money соответствующих объектов класса Item).

Пример использования классов (эти строчки в программе писать не нужно):
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.
"""


class Budget:
    """Для управления семейным бюджетом"""

    def __init__(self):
        self.lst_budget = list()

    def add_item(self, it):
        """Добавление статьи расхода в бюджет (it - объект класса Item)"""
        self.lst_budget.append(it)

    def remove_item(self, indx):
        """Удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля)"""
        del self.lst_budget[indx]

    def get_items(self):
        """Возвращает список всех статей расходов (список из объектов класса Item)"""
        return self.lst_budget


class Item:
    """Пункт расходов бюджета"""

    def __init__(self, name, money):
        if type(name) == str and type(money) in (int, float):
            self.name = name  # название статьи расхода;
            self.money = money  # сумма расходов (вещественное или целое число).

    # Также с объектами класса Item должны выполняться следующие операторы:
    # -s = it1 + it2 # сумма для двух статей расходов
    # и в общем случае:
    # -s = it1 + it2 + ... + itN # сумма N статей расходов
    # При суммировании оператор + должен возвращать число
    # (вычисленную сумму по атрибутам money соответствующих объектов класса Item).
    def __add__(self, other):
        # если объект
        if isinstance(other, Item):
            return self.money + other.money

        if isinstance(other, int):
            return self.money + other

    # если число слева от объекта
    def __radd__(self, other):
        return self.money + other

# # TEST
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
# #
# a = Item("Курс по Python ООП", 2000)
# b = Item("Курс по Django", 5000.01)
# x = a + b
