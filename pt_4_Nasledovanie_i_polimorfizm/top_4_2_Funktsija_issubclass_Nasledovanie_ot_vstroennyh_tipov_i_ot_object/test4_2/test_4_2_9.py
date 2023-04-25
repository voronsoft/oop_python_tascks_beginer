# TEST-TASK___________________________________
def test_9(SmartPhone, IteratorAttrs):
    assert issubclass(IteratorAttrs, object), "следует объявить класс IteratorAttrs"
    assert issubclass(SmartPhone, IteratorAttrs), "класс SmartPhone должен быть потомком класса IteratorAttrs"
    assert hasattr(SmartPhone, "__iter__"), \
        "экземпляры класса SmartPhone должны поддерживать итерацию, подумайте как это реализовать"

    phone = SmartPhone('iPhone', (10, 20), 1024)
    assert "size" in phone.__dict__ and "memory" in phone.__dict__ and "model" in phone.__dict__, \
        "ошибкав локальных атрибутах - ошибка названий"

    assert type(phone.__dict__["size"]) is tuple and \
           len(phone.__dict__["size"]) == 2 and \
           all(True if type(_) in (int, float) else False for _ in phone.__dict__["size"]), \
        "атрибут size содержит неверные данные, а также данные должны быть кортежем"

    assert type(phone.__dict__["memory"]) is int, "атрибут memory должен содержать значение целое число"
    assert type(phone.__dict__["model"]) is str, "атрибут model должен содержать значение в виде строки"

    try:
        temp = [(attr, value) for attr, value in phone]
    except:
        assert False, "объект некорректно отрабатывает оператор for"

    assert temp == [('model', 'iPhone'), ('size', (10, 20)), ('memory', 1024)] and \
           len(temp) == 3 and \
           len(temp[0]) == 2 and \
           all(True if type(_) is tuple else False for _ in temp), \
        "при выполнении оператора for были получены некорректные данные, ошибка данных "

    print("Так держать вы закончили главу !")
