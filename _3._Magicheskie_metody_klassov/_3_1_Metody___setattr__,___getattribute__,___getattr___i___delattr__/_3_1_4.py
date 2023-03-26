"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/DVydksYIejk

Подвиг 4. Вы создаете интернет-магазин. Для этого нужно объявить два класса:
Shop - класс для управления магазином в целом;
Объекты класса Shop следует создавать командой:
shop = Shop(название магазина)
В каждом объекте класса Shop должно создаваться локальное свойство:
goods - список товаров (изначально список пустой).
А также в классе объявить методы:
add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Product - класс для представления отдельного товара.
Объекты класса Product следует создавать командой:
p = Product(название, вес, цена)
В них автоматически должны формироваться локальные атрибуты:
id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).
В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных
локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.).
Если проверка не проходит, то генерировать исключение командой:
raise TypeError("Неверный тип присваиваемых данных.")
Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id.
При попытке это сделать генерировать исключение:
raise AttributeError("Атрибут id удалять запрещено.")

Пример использования классов (в программе эти строчки не писать):
shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
P.S. На экран ничего выводить не нужно.
"""


class Shop:
    """Shop - класс для управления магазином в целом;"""

    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        """Добавление нового товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """remove_product(self, product) - удаление товара product из магазина (из списка goods)"""
        for ind, value in enumerate(self.goods):
            if product == self.goods[ind]:
                del self.goods[ind]


# Product - класс для представления отдельного товара.
class Product:
    """Product - класс для представления отдельного товара."""
    id_product = 0

    @classmethod
    def generator_id(cls):
        cls.id_product += 1
        return cls.id_product

    # Объекты класса Product следует создавать командой:
    # p = Product(название, вес, цена)
    # В них автоматически должны формироваться локальные атрибуты:
    def __init__(self, name, weight, price):
        # id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
        self.id = self.generator_id()
        # name - название товара (строка);
        self.name = name
        # weight - вес товара (целое или вещественное положительное число);
        self.weight = weight
        # price - цена (целое или вещественное положительное число).
        self.price = price

    # В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых данных
    # локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.).
    # Если проверка не проходит, то генерировать исключение командой:
    # raise TypeError("Неверный тип присваиваемых данных.")
    def __setattr__(self, key, value):
        if key == 'id' and type(value) is int:
            return object.__setattr__(self, key, value)

        elif key == 'name' and type(value) is str:
            return object.__setattr__(self, key, value)

        elif key == 'weight' and type(value) in (int, float) and value >= 0:
            return object.__setattr__(self, key, value)

        elif key == 'price' and type(value) in (int, float) and value >= 0:
            return object.__setattr__(self, key, value)

        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    # Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id.
    # При попытке это сделать генерировать исключение:
    # raise AttributeError("Атрибут id удалять запрещено.")
    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        else:
            object.__delattr__(self, item)


# ПРОВЕРКА
# Пример использования классов (в программе эти строчки не писать):
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")
# # P.S. На экран ничего выводить не нужно.
# shop.remove_product(p)

# TEST-TASK___________________________________
assert issubclass(Shop, object), "Класс Book не является подклассом object, скорее всего не создан"
assert issubclass(Product, object), "Класс Product не является подклассом object, скорее всего не создан"

# проверка атрибутов в классах
shop = Shop("Балакирев и К")
# проверка названия
assert 'Балакирев и К' in shop.__dict__.values(), "ошибка в инициализаторе, не создается название магазина "

assert hasattr(shop, "goods"), "Не создан локальный атрибут - goods"
assert hasattr(shop, 'add_product'), "Метод add_product не определен в объекте"
assert hasattr(shop, 'remove_product'), "Метод add_product не определен в объекте"

# проверка атрибутов в классах
book = Product("Python ООП", 100, 1024)

assert hasattr(book, 'id'), "Не создан локальный атрибут - id"
assert type(book.id) == int, "номер id должен быть целым числом"

assert hasattr(book, 'weight'), "Не создан локальный атрибут - weight"
assert type(book.weight) in (int, float) and book.weight > 0, \
    "weight должен быть целое или вещественное положительное число"

assert hasattr(book, 'price'), "Не создан локальный атрибут - price"
assert type(book.price) in (int, float) and book.price > 0, \
    "price должна быть целое или вещественное положительное число "

# проверка, что номера id уникальны
lst = [Product("Python ООП", 100, 1024).id for _ in range(0, 20)]
assert any(False if lst[_] in lst[_ + 1:] else True for _ in range(len(lst))), "ошибка id не уникальны !!!"

# проверка add_product
shop.add_product(Product("Python ООП", 100, 1024))
x = Product("Test", 10, 10)
shop.add_product(x)
assert shop.goods[1] == x, "метод add_product отработал некоректно"

# проверка remove_product
shop.remove_product(x)
assert x not in shop.goods, "метод remove_product отработал некоректно"

try:
    del x.id
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при попытке удаления из продукта, атрибута id"

print("Правильный ответ !")
