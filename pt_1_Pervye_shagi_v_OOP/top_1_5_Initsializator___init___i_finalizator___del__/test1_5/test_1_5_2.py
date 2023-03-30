# TEST-TASK___________________________________
def test_2(my_money, your_money):
    assert hasattr(my_money, "money"), "Пока неправильно"
    assert hasattr(your_money, "money"), "Пока неправильно"
    print(f"my_money {my_money.__dict__}")
    print(f"your_money {your_money.__dict__}")
    print("Правильно !")
