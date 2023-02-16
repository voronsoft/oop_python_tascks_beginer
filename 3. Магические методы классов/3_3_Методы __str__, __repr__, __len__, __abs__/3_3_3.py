"""Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:
model = Model()
Объявите в этом классе метод
query() для формирования записи базы данных.
Использоваться этот метод должен следующим образом:
model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)

Например:
model.query(id=1, fio='Sergey', old=33)
Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:
print(model)
В консоль должна выводиться информация об объекте в формате:

"Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"

Например:
"Model: id = 1, fio = Sergey, old = 33"
Если метод query() не вызывался, то в консоль выводится строка:
"Model"

P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.
"""


class Model:

    def __init__(self, id=None, fio=None, old=None):
        if None not in (id, fio, old):
            self.id = int(id)
            self.fio = str(fio)
            self.old = int(old)
        else:
            self.id = id
            self.fio = fio
            self.old = old

    def query(self, *args, **qwargs):
        self.id, self.fio, self.old = list(qwargs.values())

    def __str__(self):
        # "Model: id = 1, fio = Sergey, old = 33"
        if (self.id is not None) and (self.fio is not None) and (self.old is not None):
            return f'Model: id = {self.id}, fio = {self.fio}, old = {self.old}'
        else:
            return 'Model'


# # TEST
# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)
