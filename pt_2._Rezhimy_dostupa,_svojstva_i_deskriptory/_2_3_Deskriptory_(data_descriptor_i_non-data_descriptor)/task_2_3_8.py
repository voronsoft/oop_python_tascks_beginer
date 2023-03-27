"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/l0U_3dTJZyc

Подвиг 8. Вы начинаете создавать интернет-магазин.
Для этого в программе объявляется класс SuperShop, объекты которого создаются командой:
myshop = SuperShop(название магазина)
В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:
- name - название магазина (строка);
- goods - список из товаров.
Также в классе SuperShop должны быть методы:
- add_product(product) - добавление товара в магазин (в конец списка goods);
- remove_product(product) - удаление товара из магазина (из списка goods).
Здесь product - это объект класса Product, описывающий конкретный товар.
В этом классе следует объявить следующие дескрипторы:
- name = StringValue(min_length, max_length)    # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
- price = PriceValue(max_value)    # max_value - максимально допустимое значение
Объекты класса Product будут создаваться командой:
pr = Product(наименование, цена)

Классы StringValue и PriceValue - это дескрипторы данных.
Класс StringValue должен проверять, что присваивается строковый тип с длиной строки в диапазоне [2; 50],
т.е. min_length = 2, max_length = 50.
Класс PriceValue должен проверять, что присваивается вещественное или целочисленное значение в диапазоне [0; 10000],
т.е. max_value = 10000. Если проверки не проходят, то соответствующие (прежние) значения меняться не должны.

Пример использования класса SuperShop (эти строчки в программе писать не нужно):
shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
P.S. В программе требуется объявить классы с описанным функционалом. На экран в программе выводить ничего не нужно.
"""


# Объекты класса SuperShop будут создаваться командой:
# myshop = SuperShop(название магазина)
class SuperShop:
    """Класс интернет магазина  - myshop = SuperShop(название магазина)"""

    #  В каждом объекте класса SuperShop должны формироваться следующие локальные атрибуты:
    def __init__(self, name):
        """Инициализатор названия магазина"""
        # - name - название магазина (строка);
        self.name = str(name)
        # - goods - список из товаров.
        self.goods = list()

    # Также в классе SuperShop должны быть методы:
    def add_product(self, product):
        """Добавление товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """Удаление товара из магазина (из списка goods).
        Здесь product - это объект класса Product, описывающий конкретный товар."""
        # Находим индекс товара из списка и удаляем товар
        del self.goods[self.goods.index(product)]


# Классы StringValue и PriceValue - это дескрипторы данных.
# descriptor
class StringValue:
    """Класс StringValue должен проверять, что присваивается строковый тип с длиной строки в диапазоне [2; 50], т.е. min_length = 2, max_length = 50."""

    min_length = 2
    max_length = 50

    def __set_name__(self, owner, name):
        """Создает имя переменной"""
        self.name = "_" + name

    def __get__(self, instance, owner):
        """Getter descriptor"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Setter descriptor"""
        if type(value) is str and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


# descriptor
class PriceValue:
    """Класс PriceValue должен проверять, что вещественное или целочисленное значение в диапазоне [0; 10000], т.е. max_value = 10000. Если проверки не проходят, то соответствующие (прежние) значения меняться не должны."""

    max_value = 10000

    def __set_name__(self, owner, name):
        """Создает имя переменной"""
        self.name = "_" + name

    def __get__(self, instance, owner):
        """Getter descriptor"""
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        """Setter descriptor"""
        if type(value) in (int, float) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)


# Объекты класса Product будут создаваться командой:
# pr = Product(наименование, цена)
class Product:
    """Описывает конкретный товар"""

    # В этом классе следует объявить следующие дескрипторы:
    name = StringValue()  # min_length - минимально допустимая длина строки; max_length - допустимая длина строки
    price = PriceValue()  # max_value - максимально допустимое значение

    def __init__(self, name, price):
        self.name = name
        self.price = price


# TEST-TASK___________________________________
shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(
    shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"
print("Правильно !")