"""
Подвиг 10 (на повторение, релакс). Объявите класс с именем Food (еда), объекты которого создаются командой:

food = Food(name, weight, calories)
где name - название продукта (строка);
weight - вес продукта (любое положительное число);
calories - калорийная ценность продукта (целое положительное число).

Объявите следующие дочерние классы с именами:
BreadFood - хлеб;
SoupFood - суп;
FishFood - рыба.
Объекты этих классов должны создаваться командами:
bf = BreadFood(name, weight, calories, white) # white - True для белого хлеба, False - для остальных
sf = SoupFood(name, weight, calories, dietary) # dietary - True для диетического супа, False - для других видов
ff = FishFood(name, weight, calories, fish) # fish - вид рыбы (семга, окунь, сардина и т.д.)
В каждом объекте этих дочерних классов должны формироваться соответствующие локальные атрибуты с именами:
BreadFood: _name, _weight, _calories, _white
SoupFood: _name, _weight, _calories, _dietary
FishFood: _name, _weight, _calories, _fish

Пример использования классов (эти строчки в программе писать не нужно):
bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
sf = SoupFood("Черепаший суп", 520, 890.5, False)
ff = FishFood("Консерва рыбная", 340, 1200, "семга")
P.S. В программе требуется объявить только классы. На экран выводить ничего не нужно.
"""


# ваш код:
class Food:
    def __init__(self, name, weight, calories):
        self._name = str(name)
        self._weight = weight if type(weight) in (int, float) and weight >= 0 else None
        self._calories = calories if type(calories) == int and calories >= 0 else int(calories)


class BreadFood(Food):
    def __init__(self, name, weight, calories, white):
        super().__init__(name, weight, calories)
        self._white = white  # white - True для белого хлеба, False - для остальных


class SoupFood(Food):
    def __init__(self, name, weight, calories, dietary):
        super().__init__(name, weight, calories)
        self._dietary = dietary  # dietary - True для диетического супа, False - для других видов


class FishFood(Food):
    def __init__(self, name, weight, calories, fish):
        super().__init__(name, weight, calories)
        self._fish = fish  # fish - вид рыбы (семга, окунь, сардина и т.д.)


# end ваш код
# TEST-TASK___________________________________
from test4_5.test_4_5_10 import test_10

test_10(Food, BreadFood, SoupFood, FishFood)
# END
