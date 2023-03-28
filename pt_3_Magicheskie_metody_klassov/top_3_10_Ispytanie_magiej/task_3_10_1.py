"""
Испытание магией
Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/1dSxnEFfDu8
Вы прошли магические методы. Начальство оценило вашу стойкость,
рвение и решило дать вам испытание для подтверждения уровня полученных навыков.
Вам выпала великая честь создать полноценную программу игры в "Крестики-нолики".
И вот перед вами текст с заданием самого испытания.

-----Техническое задание
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом.
Объекты этого класса будут создаваться командой:
game = TicTacToe()
В каждом объекте этого класса должен быть публичный атрибут:
pole - двумерный кортеж, размером 3x3.
Каждый элемент кортежа pole является объектом класса Cell:
cell = Cell()
В объектах этого класса должно автоматически формироваться локальное свойство:
value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.
Также с объектами класса Cell должна выполняться функция:
bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:
res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j
Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:
raise IndexError('некорректно указанные индексы')

Чтобы в программе не оперировать величинами:
0 - свободная клетка;
1 - крестики и
2 - нолики,
в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):
FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)

В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).
Также в классе TicTacToe должны быть следующие объекты-свойства (property):
is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.
Наконец, с объектами класса TicTacToe должна выполняться функция:
bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):
game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

Вам в программе необходимо объявить только два класса:
TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.
P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
"""
from random import choice


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        # value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.
        self.pole = [[Cell() for _ in range(3)] for _i in range(3)]  # двумерный кортеж, размером 3x3.
        self.human = False
        self.computer = False
        self.draw_game = False

    def verify_index(self, index):
        """Проверка индекса к обращаемой клетке"""
        if type(index) is str:
            index = int(index[0]), int(index[-1])
            if all(True if type(_) is int else False for _ in index) and \
                    0 <= index[0] < len(self.pole) and 0 <= index[1] < len(self.pole[0]):
                return True

        elif all(True if type(_) is int else False for _ in index) and \
                0 <= index[0] < len(self.pole) and 0 <= index[1] < len(self.pole[0]):
            return True
        else:
            raise IndexError('некорректно указанные индексы')

    # К каждой клетке игрового поля должен быть доступ через операторы:
    # res = game[i, j] # получение значения из клетки с индексами i, j
    # game[i, j] = value # запись нового значения в клетку с индексами i, j
    # Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:
    # raise IndexError('некорректно указанные индексы')
    def __getitem__(self, item):
        """Получение значения из клетки"""
        # проверяем индекс (диапазон)
        self.verify_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, val):
        """Запись нового значения в клетку"""
        # проверяем индекс (диапазон)
        self.verify_index(key)
        # записываем 
        self.pole[key[0]][key[1]].value = val
        # проводим проверку выиграл ли кто-то
        self.veryfi_win()

    # В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):
    def init(self):
        """Инициализация игры (очистка игрового поля, возможно, еще какие-либо действия)"""
        self.pole = [[Cell() for _ in range(3)] for _i in range(3)]  # двумерный кортеж, размером 3x3.
        # обновляем переменные human - computer - draw_game
        self.human = False
        self.computer = False
        self.draw_game = False
        return self

    def show(self):
        """Отображение текущего состояния игрового поля (как именно - на свое усмотрение)"""
        x = [[i.value for i in _] for _ in self.pole]
        return [print(*i) for i in x], print()

    def veryfi_win(self):
        """Функция проверки заполненности поля и кто выиграл"""

        # проверка поля по горизонтали
        win_human_row = any(
            [all(_) for _ in [[True if j.value == self.HUMAN_X else False for j in i] for i in self.pole]])
        win_comp_row = any(
            [all(_) for _ in [[True if j.value == self.COMPUTER_O else False for j in i] for i in self.pole]])

        # проверка поля по вертикали
        win_human_col = any(
            [all([True if self.pole[i][_].value == self.HUMAN_X else False for i in range(len(self.pole))]) for _ in
             range(len(self.pole))])
        win_comp_col = any(
            [all([True if self.pole[i][_].value == self.COMPUTER_O else False for i in range(len(self.pole))]) for _ in
             range(len(self.pole))])

        # проверка поля по диагоналям
        win_human_diag = all([self.pole[i][i].value == self.HUMAN_X for i in range(len(self.pole))]) or all(
            [self.pole[i][-1 - i].value == self.HUMAN_X for i in range(len(self.pole))])

        win_comp_diag = all([self.pole[i][i].value == self.COMPUTER_O for i in range(len(self.pole))]) or all(
            [self.pole[i][-1 - i].value == self.COMPUTER_O for i in range(len(self.pole))])

        # Кто выиграл проверяем
        if any([win_human_row, win_human_col, win_human_diag]):
            self.human = True
            # print('Вы выиграли !')
        elif any([win_comp_row, win_comp_col, win_comp_diag]):
            self.computer = True
            # print('В следующий раз повезёт ....')

        elif self.free_cell_check is False and self.human is False and self.computer is False:
            self.draw_game = True
            # print('Хм... ничья.')

    def free_cell_check(self):
        """Проверка свободных клеток"""
        answer = any(
            [(True if self.pole[j][i].value == self.FREE_CELL else False) for j in range(len(self.pole)) for i in
             range(len(self.pole))])
        return answer

    def human_go(self):
        """Реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик)"""
        if self.free_cell_check and self.computer != True:
            while True:
                coord = tuple(map(int, input('Введите координаты: ').split()))
                # проверяем индекс
                self.verify_index(coord)
                # проверяем свободна ли клетка
                if self.pole[coord[0]][coord[1]].value == 0:
                    # если свободна ставим крестик
                    self.pole[coord[0]][coord[1]].value = self.HUMAN_X
                    # проверяем заполненность поля и есть ли выигрышные позиции
                    self.veryfi_win()
                    # останавливаем цикл ввода
                    break
                else:
                    # print('Клетка занята, повторите ввод !\n')
                    continue
        else:
            # print('Игра окончена, выиграл компьютер !')
            pass

    def computer_go(self):
        """Реализация хода компьютера (ставит случайным образом нолик в свободную клетку)"""
        # если свободных клеток нет останавливаем игру
        if self.free_cell_check and self.human != True:
            while True:
                x = choice(
                    range(len(self.pole)))  # random.choice(sequence) - случайный элемент непустой последовательности.
                y = choice(
                    range(len(self.pole)))  # random.choice(sequence) - случайный элемент непустой последовательности.
                # проверяем пустая ли клетка
                if self.pole[x][y].value == 0:
                    # комп ставит нолик
                    self.pole[x][y].value = self.COMPUTER_O
                    # проверяем заполненность поля и есть ли выигрышные позиции
                    self.veryfi_win()
                    break
                # иначе продолжаем цикл пока не будет найдена свободная клетка
        else:
            # print('Игра окончена, вы выиграли !')
            pass

    # Также в классе TicTacToe должны быть следующие объекты-свойства (property):
    def __is_human_win(self):
        """Возвращает True, если победил человек, иначе - False"""
        return self.human

    @property
    def is_human_win(self):
        return self.human

    def __is_computer_win(self):
        """Возвращает True, если победил компьютер, иначе - False"""
        return self.computer

    @property
    def is_computer_win(self):
        return self.computer

    def __is_draw(self):
        """Возвращает True, если ничья, иначе - False"""
        if self.draw_game:
            return True
        else:
            return False

    @property
    def is_draw(self):
        return self.__is_draw()

    # Наконец, с объектами класса TicTacToe должна выполняться функция:
    # bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.
    def bool(self):
        pass


class Cell:
    def __init__(self, value=0):
        self.value = value

    # Также с объектами класса Cell должна выполняться функция:
    # bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.
    def __bool__(self):
        if self.value == 0:
            return True
        else:
            return False

# TEST PROGRAM
# game = TicTacToe()
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")
# #
# #
# TEST BALAKIREV
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
# assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
# cell.value = 1
# assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"
# 
# assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe,
#                                                                                  'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
# 
# game = TicTacToe()
# assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
# assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
# game[1, 1] = TicTacToe.HUMAN_X
# assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
# 
# game[0, 0] = TicTacToe.COMPUTER_O
# assert game[
#            0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
# 
# game.init()
# assert game[0, 0] == TicTacToe.FREE_CELL and game[
#     1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
# 
# try:
#     game[3, 0] = 4
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
# 
# game.init()
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
# 
# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X
# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
# 
# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
