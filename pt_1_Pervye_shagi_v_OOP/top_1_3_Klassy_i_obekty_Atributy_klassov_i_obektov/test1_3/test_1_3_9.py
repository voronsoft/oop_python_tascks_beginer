# TEST-TASK___________________________________
def test_9(x, fig1, temp):
    Figure = x
    try:
        issubclass(Figure, object)
    except NameError:
        print("Вы не создали класс - Figure")

    assert hasattr(Figure, "type_fig") and hasattr(Figure, "color")
    assert isinstance(fig1, Figure), "не создан екземпляр класса fig1 с требуемыми параметрами"
    assert len(temp) == 2 and "start_pt" in temp and "end_pt" in temp, \
        "В объекте fig1 неправильное количество локальных переменных или  имена переменных не соответствуют заданным "

    assert len(fig1.__dict__) == 2 and fig1.start_pt == (10, 5) and fig1.end_pt == (
        100, 20), "В экземпляре класса должно быть 2 локальных атрибута start_pt и end_pt"

    assert 'color' not in fig1.__dict__, "Локальный атрибут color должен быть удален из fig1"
    print("Правильно так держать ! ")
