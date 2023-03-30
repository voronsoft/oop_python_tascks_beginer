# TEST-TASK___________________________________
def test_10(pole_game, GamePole):
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
