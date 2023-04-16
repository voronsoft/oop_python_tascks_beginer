# TEST-TASK___________________________________
def test_4(Player, players, lst_in, players_filtered):
    assert hasattr(Player, "__bool__"), "определите метод __bool__"
    assert len(players) == len([Player(*i.split(';')) for i in lst_in]), "в списке неправильное количество объектов"
    assert players_filtered == list(filter(bool, players)), "некорректно отработала функция сортировки"
    print("Правильный ответ")
