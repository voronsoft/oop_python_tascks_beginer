"""
Подвиг 9. Объявите класс Recipe для представления рецептов.
Отдельные ингредиенты рецепта должны определяться классом Ingredient.
Объекты этих классов должны создаваться командами:

ing = Ingredient(name, volume, measure)
recipe = Recipe()
recipe = Recipe(ing_1, ing_2,..., ing_N) где ing_1, ing_2,..., ing_N - объекты класса Ingredient.

В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
-name - название ингредиента (строка);
-volume - объем ингредиента в рецепте (вещественное число);
-measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;

С объектами класса Ingredient должна работать функция:
str(ing)  # название: объем, ед. изм.
и возвращать строковое представление объекта в формате:
"название: объем, ед. изм."
Например:
ing = Ingredient("Соль", 1, "столовая ложка")
s = str(ing) # Соль: 1, столовая ложка

Класс Recipe должен иметь следующие методы:
add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.

Также с объектами класса Recipe должна поддерживаться функция:
len(recipe) - возвращает число ингредиентов в рецепте.

Пример использования классов (эти строчки в программе писать не нужно):

recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
P.S. На экран ничего выводить не нужно, только объявить классы.
"""


# recipe = Recipe()
# recipe = Recipe(ing_1, ing_2,..., ing_N)
# где ing_1, ing_2,..., ing_N - объекты класса Ingredient.
class Recipe:
    """ Для представления рецептов."""

    def __init__(self, *args):
        self.lst = list(args)

    def add_ingredient(self, ing):
        """Добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец)"""
        self.lst.append(ing)

    def remove_ingredient(self, ing):
        """Удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта"""
        del self.lst[self.lst.index(ing)]

    def get_ingredients(self):
        """Получение кортежа из объектов класса Ingredient текущего рецепта"""
        return tuple(self.lst)

    # len(recipe) - возвращает число ингредиентов в рецепте.
    def __len__(self):
        return len(self.lst)


# ing = Ingredient(name, volume, measure)
class Ingredient:
    """Ингредиент для рецепта"""

    def __init__(self, name='', volume=0.0, measure=''):
        self.name = str(name)  # название ингредиента (строка)
        self.volume = float(volume)  # объем ингредиента в рецепте (вещественное число)
        self.measure = str(measure)  # единица измерения объема ингредиента (строка), литр, чайная ложка, грамм, штук.

    def __str__(self):
        """"название: объем, ед. изм."""
        return f'{self.name}: {int(self.volume)}, {self.measure}'

# # ТЕСТ
# i1 = Ingredient("Соль", 1, "столовая ложка")
# i2 = Ingredient("Мука", 1, "кг")
# i3 = Ingredient("Мясо баранины", 10, "кг")
# i4 = Ingredient("Масло", 100, "гр")
# recipe = Recipe(i1, i2, i3)
# recipe.add_ingredient(i4)
# recipe.remove_ingredient(i3)
# 
# assert len(recipe) == 3, "функция len вернула неверное значение"
# lst = recipe.get_ingredients()
# for x in lst:
#     assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
#     assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"
# 
# assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"
# 
# i4 = Ingredient("Масло", 120, "гр")
# recipe.add_ingredient(i4)
# assert len(recipe) == 4, "функция len вернула неверное значение"
