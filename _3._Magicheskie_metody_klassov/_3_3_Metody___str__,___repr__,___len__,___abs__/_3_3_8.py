"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V7SV1pOWyEY

Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен.
Объекты этого класса должны создаваться командой:
dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени.

Эти объекты должны создаваться командой:
clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

- get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
Если разность получается отрицательной, то разницу времен считать нулевой.

Пример использования классов (эти строчки в программе писать не нужно):

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
Обратите внимание, добавляется незначащий ноль, если число меньше 10.

P.S. На экран ничего выводить не нужно, только объявить классы.
"""


class DeltaClock:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        """ str(dt) возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды"""
        d = self.__len__()
        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'

    def __len__(self):
        """ возвращает разницу времен clock1 - clock2 в секундах (целое число)"""
        x = self.a.get_time() - self.b.get_time()
        return x if x > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = self.verify_time(hours)
        self.minutes = self.verify_time(minutes)
        self.seconds = self.verify_time(seconds)

    @staticmethod
    def verify_time(time):
        if type(time) == int and time >= 0:
            if len(str(time)) == 1:
                return time
            else:
                return time

    def get_time(self):
        """возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds)"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

# # TEST
# a = Clock(2, 45, 0)
# b = Clock(1, 15, 0)
# dt = DeltaClock(a, b)
# print(a.get_time())
# print(dt)  # 01: 30: 00
# len_dt = len(dt)  # 5400
