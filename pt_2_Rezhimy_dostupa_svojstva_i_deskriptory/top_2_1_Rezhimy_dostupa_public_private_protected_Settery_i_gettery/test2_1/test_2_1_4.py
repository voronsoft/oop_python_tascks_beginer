# TEST-TASK___________________________________
def test_4(Money):
    mn_1 = Money(10)
    mn_2 = Money(20)
    assert mn_1._Money__money == 10 and mn_2._Money__money == 20, "неверные значения в локальном приватном атрибуте __money"

    mn_1.set_money(100)
    mn_2.add_money(mn_1)
    assert mn_1.get_money() == 100 and mn_2.get_money() == 120, "неверное количество средств: возможно некорректная работа методов set_money и/или add_money"

    mn_1.set_money(-1)
    assert mn_1.get_money() == 100, "неверное количество средств: некорректная работа метода set_money"
    print("Правильный ответ !")
