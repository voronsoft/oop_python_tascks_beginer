# TEST-TASK___________________________________
def test_7(Game, Singleton):
    game1 = Game('mario')
    game2 = Game('polo')
    game3 = Game('koko')
    assert issubclass(Game, Singleton), "ошибка, класс Game должен быть дочерним классом от Singleton"
    assert "name" in game1.__dict__, "ошибка, в каждом объекте класса Game должен формироваться атрибут name"
    assert id(game1) == id(game2) == id(
        game3), "ошибка, объекты класса Game должны ссылаться на один единственный обект"

    print("Правильно )")
