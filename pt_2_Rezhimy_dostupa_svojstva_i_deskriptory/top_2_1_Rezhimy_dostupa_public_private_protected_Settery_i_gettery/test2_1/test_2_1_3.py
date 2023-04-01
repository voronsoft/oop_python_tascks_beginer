# TEST-TASK___________________________________
def test_3(clock, Clock):
    assert isinstance(clock, Clock) and hasattr(Clock, 'set_time') and hasattr(Clock, 'get_time'), \
        "в классе Clock присутствуют не все методы"

    assert clock.get_time() == 4530, "текущее время в объекте clock не равно 4530"

    clock.set_time(10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(-10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(1000001)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    print("Правильный ответ !")
