# TEST-TASK___________________________________
def test_4(Cat, Animal, Dog):
    assert issubclass(Cat, Animal) and issubclass(Dog, Animal), "Cat, Dog не являются дочерними классами от Animal"
    assert hasattr(Cat, "get_info") and hasattr(Dog, "get_info"), " в дочерних классах должен быть метод - get_info"
    assert callable(Cat.get_info) and callable(Dog.get_info), "ошибка, get_info должен быть методом"

    cat = Cat('кот', 4, 'black', 2.25)
    assert type(cat.name) is str and \
           type(cat.color) is str and \
           type(cat.old) is int and \
           type(cat.weight) in (int, float) and cat.weight > 0, "в локальных атрибутах не тот тип данных значений"

    dog = Dog('собака', 10, 'Борзая', (1.0, 0.85))
    assert type(dog.name) is str and \
           type(dog.breed) is str and \
           type(dog.old) is int and \
           type(dog.size) is tuple and \
           type(dog.size[0]) in (int, float) and \
           type(dog.size[1]) in (int, float), 'в локальных атрибутах не тот тип данных значений'

    assert cat.get_info() == 'кот: 4, black, 2.25', "метод cat.get_info() вернул неправильный формат строки"
    assert dog.get_info() == 'собака: 10, Борзая, (1.0, 0.85)', "метод dog.get_info() вернул неправильный формат строки"
    print("Правильный ответ !!")
