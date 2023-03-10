"""Подвиг 5. В программе объявлен дескриптор StringField и класс DataBase:
class StringField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y

А, затем, выполняются команды:
db = DataBase('hi', 'low')
db.__dict__['x'] = 'top'
print(db.x)

Какое значение будет выведено в консоль и почему?
"""

# Будет выведено 'top', так как в строчке db.__dict__['x'] = 'top' явно создается локальный атрибут x
# и затем он имеет наибольший приоритет при обращении к нему (в строчке db.x).
#
# Будет выведено 'hi', так как локальное свойство в строчке db.__dict__['x'] = 'top' просто не будет создано
# (имя x уже занято дескриптором StringField).
#
# Будет выведено 'hi', так как StringField - это дескриптор данных и он имеет наибольший приоритет при обращении к атрибутам,
# поэтому в строчке db.x будет обращение к дескриптору, а не к локальному свойству.
#
# Будет выведено 'top', так как в строчке db.__dict__['x'] = 'top',
# фактически, идет обращение к дескриптору StringField и заносится новое значение 'top'.
