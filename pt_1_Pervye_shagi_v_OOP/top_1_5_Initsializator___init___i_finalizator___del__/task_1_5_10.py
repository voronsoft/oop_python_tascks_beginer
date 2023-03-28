"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/gmjwMakXk0c

Большой подвиг 10. Объявите два класса: 
Cell - для представления клетки игрового поля;
GamePole - для управления игровым полем, размером N x N клеток.

С помощью класса Cell предполагается создавать отдельные клетки командой:
c1 = Cell(around_mines, mine)
- around_mines - число мин вокруг данной клетки поля;
- mine - булева величина (True/False), означающая наличие мины в текущей клетке.

При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
around_mines - число мин вокруг клетки (начальное значение 0);
mine - наличие мины в текущей клетке (True/False);
fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).



С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
pole_game = GamePole(N, M)
Здесь N - размер поля; M - общее число мин на поле.
При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке
N x N элементов - локальном свойстве pole объекта класса GamePole.

В классе GamePole должны быть также реализованы следующие методы:

init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
разумеется каждая мина должна находиться в отдельной клетке).
show() - отображение поля в консоли в виде таблицы чисел открытых клеток
(если клетка не открыта, то отображается символ #).

При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init()
для первоначальной инициализации игрового поля.

В классе GamePole могут быть и другие вспомогательные методы.

Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12. 
P.S. На экран в программе ничего выводить не нужно.
"""
from random import randrange, choice


# Cell - для представления клетки игрового поля;
# С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)
# - around_mines - число мин вокруг данной клетки поля;
# - mine - булева величина (True/False), означающая наличие мины в текущей клетке.
#
# При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


# GamePole - для управления игровым полем, размером N x N клеток.
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле.
# При этом, каждая клетка представляется объектом класса Cell и все объекты хранятся в двумерном списке
# N x N элементов - локальном свойстве pole объекта класса GamePole.
#
# В классе GamePole должны быть также реализованы следующие методы:
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
# разумеется каждая мина должна находиться в отдельной клетке).
#
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток
# (если клетка не открыта, то отображается символ #).
#
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init()
# для первоначальной инициализации игрового поля.
# В классе GamePole могут быть и другие вспомогательные методы.
class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    # init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю,
    # разумеется каждая мина должна находиться в отдельной клетке).
    def init(self):
        count = 0
        while count < self.M:
            i = randrange(0, self.N - 1)
            k = randrange(0, self.N - 1)
            if self.pole[i][k].mine:
                continue
            self.pole[i][k].mine = True
            count += 1

        ind = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    mines = sum(
                        (self.pole[x + i][y + k].mine for i, k in ind if 0 <= x + i < self.N and 0 <= y + k < self.N))
                    self.pole[x][y].around_mines = mines

    # show() - отображение поля в консоли в виде таблицы чисел открытых клеток
    # (если клетка не открыта, то отображается символ #).
    def show(self):
        for i_ in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', i_))


# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.
# P.S. На экран в программе ничего выводить не нужно.
pole_game = GamePole(10, 12)
# pole_game.show()


# TEST-TASK___________________________________

assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')

N = 10
M = 10


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n


for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i, j), \
                f"неверное число мин вокруг клетки с индексами {i, j}"
print("Умница хорошее решение !!")