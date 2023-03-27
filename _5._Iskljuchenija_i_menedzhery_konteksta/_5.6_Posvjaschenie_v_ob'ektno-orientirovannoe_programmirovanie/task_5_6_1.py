import random




class Ship:
    def __init__(self, length, name):
        self.length = length
        self.position = None
        self.orientation = None
        self.health = length
        self.destroyed = False
        self.name = name
        self.hits = [False] * length


    def place_ship(self, game_pole):
        """
        Размещение корабля на игровом поле

        game_pole: экземпляр класса GamePole - игровое поле, на котором будет размещен корабль
        """
        # Выбираем случайную позицию и ориентацию корабля
        row = random.randint(0, game_pole.size - 1)
        col = random.randint(0, game_pole.size - 1)
        orientation = random.choice(['horizontal', 'vertical'])

        # Проверяем, можно ли разместить корабль в этой позиции и ориентации
        while not game_pole.check_ship_placement(row, col, orientation, self.length):
            row = random.randint(0, game_pole.size - 1)
            col = random.randint(0, game_pole.size - 1)
            orientation = random.choice(['horizontal', 'vertical'])

        # Устанавливаем позицию и ориентацию корабля
        self.position = (row, col)
        self.orientation = orientation

        # Обновляем состояние игрового поля
        game_pole.place_ship(row, col, orientation, self.length)

    def check_placement(self, game_pole, row, col, orientation):
        """
        Проверка возможности размещения корабля на игровом поле в указанных координатах и ориентации

        game_pole: экземпляр класса GamePole - игровое поле
        row: int - номер строки, в которой размещается корабль
        col: int - номер столбца, в котором размещается корабль
        orientation: str - ориентация корабля: 'horizontal' или 'vertical'

        Возвращает True, если размещение возможно, иначе - False
        """
        if orientation == 'horizontal':
            # Проверяем, что корабль полностью помещается на поле
            if col + self.length > game_pole.size:
                return False
            # Проверяем, что корабль не пересекается с другими кораблями
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + self.length + 1):
                    if i < 0 or i >= game_pole.size or j < 0 or j >= game_pole.size:
                        continue
                    if game_pole.cells[i][j] != 0:
                        return False
        else:
            # Проверяем, что корабль полностью помещается на поле
            if row + self.length > game_pole.size:
                return False
            # Проверяем, что корабль не пересекается с другими кораблями
            for i in range(row - 1, row + self.length + 1):
                for j in range(col - 1, col + 2):
                    if i < 0 or i >= game_pole.size or j < 0 or j >= game_pole.size:
                        continue
                    if game_pole.cells[i][j] != 0:
                        return False
        # Если все проверки пройдены успешно, размещение корабля возможно
        return True

    def is_destroyed(self):
        """
        Проверка, разрушен ли корабль
        """
        return all(self.hits)

    def hit(self):
        """
        Обработка попадания по кораблю
        """
        self.hits += 1
        if self.hits == self.length:
            self.destroyed = True
            for cell in self.cells:
                row, col = cell
                game_pole.cells[row][col] = 2

    def move(self, game_pole):
        """
        Перемещение корабля на игровом поле

        game_pole: экземпляр класса GamePole - игровое поле, на котором находится корабль
        """
        # Генерируем направление перемещения - вперед или назад
        direction = random.choice([-1, 1])

        # Вычисляем новую позицию корабля
        row, col = self.position
        if self.orientation == 'horizontal':
            new_col = col + direction
            # Проверяем, не выходит ли корабль за пределы поля
            if new_col < 0 or new_col + self.length > game_pole.size:
                direction *= -1
                new_col = col + direction
            # Проверяем, не пересекается ли корабль с другими кораблями на поле
            if any(game_pole.cells[row][new_col + i] for i in range(self.length)):
                direction *= -1
                new_col = col + direction
        else:  # self.orientation == 'vertical'
            new_row = row + direction
            # Проверяем, не выходит ли корабль за пределы поля
            if new_row < 0 or new_row + self.length > game_pole.size:
                direction *= -1
                new_row = row + direction
            # Проверяем, не пересекается ли корабль с другими кораблями на поле
            if any(game_pole.cells[new_row + i][col] for i in range(self.length)):
                direction *= -1
                new_row = row + direction

        # Обновляем позицию корабля на поле
        game_pole.clear_ship(self)
        self.position = (new_row, new_col)
        game_pole.place_ship(self)


#
#
# TEST-TASK___________________________________
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(
    s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
