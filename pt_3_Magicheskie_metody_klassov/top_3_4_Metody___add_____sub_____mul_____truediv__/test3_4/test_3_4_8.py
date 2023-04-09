# TEST-TASK___________________________________
def test_8(Budget, Item):
    my_budget = Budget()
    assert hasattr(my_budget, "add_item") and hasattr(my_budget, "remove_item") and hasattr(my_budget, "get_items"), \
        "ошибка в не все методы объявлены в екземпляре класса"

    st = Item("Курс по Python ООП", 2000)
    assert hasattr(st, "name") and hasattr(st, "money"), "ошибка локальных атрибутов в пункте расхода бюджета"

    assert len(my_budget.get_items()) == 0, "метод get_items() работает некорректно"

    my_budget.add_item(Item("Курс по Python ООП", 2000))
    my_budget.add_item(Item("Курс по Django", 5000.01))
    assert len(my_budget.get_items()) == 2, "метод add_item работает некорректно"

    # -remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
    temp = id(my_budget.get_items()[0])
    my_budget.remove_item(1)
    assert len(my_budget.get_items()) == 1 and id(my_budget.get_items()[0]) == temp, \
        "метод remove_item удалил не тот объект"

    x = Item("Курс по Python ООП", '2000')
    assert x.__dict__ == {}, "атрибут money может принимать значения только int или float"

    a = Item("Курс по Python ООП", 2000)
    b = Item("Курс по Django", 5000.01)
    c = Item("Курс по Python ООП", 2000)
    s = a + b
    assert s == 7000.01, "ошибка при операции - сумма для двух статей расходов"
    s = a + b + c
    assert s == 9000.01, "ошибка при операции - сумма N статей расходов"

    print("Правильный ответ !!")
