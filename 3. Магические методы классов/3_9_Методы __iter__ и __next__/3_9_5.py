"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/-ZvYUtWMUFw

Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)
где:
fio - ФИО сотрудника (строка);
job - наименование должности (строка);
old - возраст (целое число);
salary - зарплата (число: целое или вещественное);
year_job - непрерывный стаж на указанном месте работы (целое число).
В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами:
fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:
data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)
При работе с индексами, проверить корректность значения indx.
Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:
raise IndexError('неверный индекс')

Пример использования класса (эти строчки в программе не писать):
pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
"""


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = str(fio)  # ФИО сотрудника (строка);
        self.job = str(job)  # наименование должности (строка);
        self.old = int(old)  # возраст (целое число);
        if type(salary) in (int, float):
            self.salary = int(salary)  # зарплата (число: целое или вещественное);
        else:
            raise ValueError('число должно быть целое или вещественное')
        self.year_job = int(year_job)  # непрерывный стаж на указанном месте работы (целое число).

        self.lst = ['fio', 'job', 'old', 'salary', 'year_job']
        # переменная для итератора
        self.it = 0

    # Также с объектами класса Person должны поддерживаться следующие команды:
    # data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
    def __getitem__(self, item):
        if 0 <= item < len(self.lst):
            for ind, val in enumerate(self.lst):
                if ind == item:
                    return getattr(self, val)
        else:
            raise IndexError('неверный индекс')

    # p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
    def __setitem__(self, key, value):
        if 0 <= key < len(self.lst):
            for ind, val in enumerate(self.lst):
                if ind == key:
                    return setattr(self, val, value)

        else:
            raise IndexError('неверный индекс')

    # for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    #     print(v)
    # При работе с индексами, проверить корректность значения indx.
    # Оно должно быть целым числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:
    # raise IndexError('неверный индекс')
    def __iter__(self):
        self.it = 0
        return self

    def __next__(self):
        if self.it < len(self.lst):
            ret_value = self.it
            self.it += 1
            return self[ret_value]
        else:
            raise StopIteration

# # TEST
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# # print(pers[0])
# pers[0] = 'Балакирев С.М.'
# # print(pers[0])
# for v in pers:
#     print(v)
# #pers[5] = 123 # IndexError
