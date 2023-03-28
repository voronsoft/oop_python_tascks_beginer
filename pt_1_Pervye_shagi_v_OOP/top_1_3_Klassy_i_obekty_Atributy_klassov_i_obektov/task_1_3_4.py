"""
Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные):

title: "Мороженое"
weight: 154
tp: "Еда"
price: 1024
Затем, после объявления класса, измените его атрибут price на значение 2048 и добавьте еще один атрибут:
inflation: 100
Запустите файл на исполнение
"""


# TEST
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


# измените его атрибут price на значение 2048
Goods.price = 2048
# добавьте еще один атрибут
Goods.inflation = 100

# TEST-TASK___________________________________
assert hasattr(Goods, "title"), "В классе нет атрибута title"
assert hasattr(Goods, "weight"), "В классе нет атрибута weight"
assert hasattr(Goods, "tp"), "В классе нет атрибута tp"
assert hasattr(Goods, "price"), "В классе нет атрибута price"
assert hasattr(Goods, "inflation"), "В классе нет атрибута inflation"

assert Goods.title == "Мороженое", "Значение атрибута неправильное"
assert Goods.weight == 154, "Значение атрибута неправильное"
assert Goods.tp == "Еда", "Значение атрибута неправильное"
assert Goods.price == 2048, "Значение атрибута неправильное"
assert Goods.inflation == 100, "Значение атрибута неправильное"
print("Правильно !")
