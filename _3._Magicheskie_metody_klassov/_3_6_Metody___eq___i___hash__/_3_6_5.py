"""
Подвиг 5. Пусть в программе определен следующий класс:

class Index:
    START_INDEX = 0

    def __init__(self):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1

    def __hash__(self):
        return hash(str(self.id))
И делается попытка создать словарь с ключами из объектов этого класса:

id1 = Index()
id2 = Index()
d = {id1: id1, id2: id2}
Выберите верное утверждение, связанное с этой программой.
"""


#
# будет создан словарь с одним ключом, так как объект id1 равен объекту id2
#
# возникнет ошибка, так как ключами словаря не могут выступать объекты классов
#
# программа выполнится без ошибок, но словарь будет пустым, так как объекты id1, id2 не могут выступать ключами словаря
#
# словарь будет успешно создан и к его значениям можно обращаться, например, командой: d[id1].id

# TEST
class Index:
    START_INDEX = 0

    def __init__(self):
        self.id = Index.START_INDEX
        Index.START_INDEX += 1

    def __hash__(self):
        return hash(str(self.id))


# И делается попытка создать словарь с ключами из объектов этого класса:

id1 = Index()
id2 = Index()
d = {id1: id1, id2: id2}
print(d[id1].id)
# словарь будет успешно создан и к его значениям можно обращаться, например, командой: d[id1].id
