"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/nT_sMhJsw1E

Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:

my_money = Money(100)
your_money = Money(1000)
Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.

P.S. На экран в программе ничего выводить не нужно.
"""


# здесь объявляйте класс Money
class Money:
    def __init__(self, s):
        self.money = s


my_money = Money(100)
your_money = Money(1000)

# TEST-TASK___________________________________
assert hasattr(my_money, "money"), "Пока неправильно"
assert hasattr(your_money, "money"), "Пока неправильно"
print(f"my_money {my_money.__dict__}")
print(f"your_money {your_money.__dict__}")
print("Правильно !")