# TEST-TASK___________________________________
def test_10(x, p1, temp):
    Person = x

    try:
        issubclass(Person, object)
    except NameError:
        print("Вы не создали класс - Person")

    assert hasattr(Person, 'name') and hasattr(Person, 'job') and hasattr(Person, 'city'), \
        "В классе должно быть 3 атрибута"

    try:
        isinstance(p1, Person)

    except NameError:
        print("Вы не создали экземпляр класса p1")

    assert 'job' not in p1.__dict__, "Ошибка, в экземпляре класса p1 не должно быть локального свойства - job"
    assert Person.name == 'Сергей Балакирев' and Person.job == 'Программист' and \
           Person.city == 'Москва', "Неправильно попробуйте снова"
    assert temp is False
    print("Правильно !!")
