"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ljahVEppmxM

Из входного потока читаются строки данных с помощью команды:
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
в формате: id, name, old, salary (записанные через пробел). Например:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
...

То есть, каждая строка - это элемент списка lst_in.

Необходимо в класс DataBase:
class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

добавить два метода:
select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне [a; b] (включительно)
по их индексам (не id, а индексам списка); также учесть, что граница b может превышать длину списка.

insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
Каждая запись в списке lst_data должна быть представлена словарем в формате:
{'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
Например:
{'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}

Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в кол FIELDS.

P. S. Ваша задача только добавить два метода в класс DataBase.

Sample Input:

1 Сергей 35 120000
2 Федор 23 12000
3 Иван 13 1200
"""
# код не менять
import io
import sys

s = "1 Сергей 35 120000\n2 Федор 23 12000\n3 Иван 13 1200\n"
stream = io.StringIO(s)
sys.stdin = stream
# END

import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    # select(self, a, b) - возвращает список из элементов списка lst_data в диапазоне
    # [a; b] (включительно) по их индексам (не id, а индексам списка);
    def select(self, a, b):
        if b < len(self.lst_data):
            return self.lst_data[a:b + 1]
        # также учесть, что граница b может превышать длину списка.
        elif b >= len(self.lst_data):
            return self.lst_data

    # insert(self, data) - для добавления в список lst_data новых данных из переданного списка строк data;
    # Каждая запись в списке lst_data должна быть представлена словарем в формате:
    # # lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
    # {'id': 'номер', 'name': 'имя', 'old': 'возраст', 'salary': 'зарплата'}
    # Например:
    # {'id': '1', 'name': 'Сергей', 'old': '35', 'salary': '120000'}
    def insert(self, data):
        self.data = [i.split() for i in data]
        data = [dict(zip(self.FIELDS, self.data[i])) for i in range(len(self.data))]
        for i in data:
            self.lst_data.append(i)


db = DataBase()
db.insert(lst_in)

# TEST-TASK___________________________________
res1 = db.select(0, 50)

lstgfghj8gh9jg2 = []
for d in lst_in:
    lstgfghj8gh9jg2.append(dict(zip(DataBase.FIELDS, d.split())))

assert res1 == lstgfghj8gh9jg2, "метод select вернул неверные данные"

res2 = db.select(0, 1)
assert res2 == lstgfghj8gh9jg2[0:2], "некорректно работает метод select"

print("Правильно !")
