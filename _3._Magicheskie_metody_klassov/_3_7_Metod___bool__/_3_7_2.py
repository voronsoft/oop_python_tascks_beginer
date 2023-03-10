"""
Подвиг 2. Пусть в программе объявлен следующий класс:

class User:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def __len__(self):
        return self.old + 1

    def __bool__(self):
        return bool(self.old)
И определены два его объекта:

user1 = User('Sergey', 45)
user2 = User('Петр', 0)
Отметьте все верные пункты, связанные с использованием функции bool().
"""

# bool(user2) вернет значение True, так как магический метод __len__() имеет приоритет над методом __bool__(), а __len__() возвращает ненулевое значение, то есть, True
#
# bool(user2) вернет значение False, так как будет вызван магический метод __bool__(), который вернет False
#
# bool(user1) вернет значение True, так как будет вызван магический метод __bool__(), который вернет True
#
# bool(user1) вернет значение False, так как будет вызван магический метод __bool__(), который вернет False
