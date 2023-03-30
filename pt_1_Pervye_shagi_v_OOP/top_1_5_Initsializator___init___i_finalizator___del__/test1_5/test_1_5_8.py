# TEST-TASK___________________________________
def test_8(Cart, Table, TV, Notebook, Cup):
    # Проверка класса Cart
    x = Cart()
    assert hasattr(x, 'goods') and len(x.goods) == 0, " в объекте класса Cart нет атрибута goods"
    assert hasattr(x, 'add'), "У объекта нет метода add"
    assert hasattr(x, 'remove'), "У объекта нет метода remove"
    assert hasattr(x, 'get_list'), "У объекта нет метода get_list"
    # ___
    # Проверка класса Table - столы;
    x = Table('наименование', '100')
    assert hasattr(x, 'name') and hasattr(x, 'price'), "В классе должны быть 2 атрибута name и price"
    # ___
    # Проверка класса TV - телевизоры;
    x = TV('наименование', '100')
    assert hasattr(x, 'name') and hasattr(x, 'price'), "В классе должны быть 2 атрибута name и price"
    # ___
    # Проверка класса Notebook - ноутбуки;
    x = Notebook('наименование', '100')
    assert hasattr(x, 'name') and hasattr(x, 'price'), "В классе должны быть 2 атрибута name и price"
    # ___
    # Проверка класса Cup - кружки.
    x = Cup('наименование', '100')
    assert hasattr(x, 'name') and hasattr(x, 'price'), "В классе должны быть 2 атрибута name и price"
    # ___

    cart = Cart()
    # Добавьте в него:
    # два телевизора (TV),
    for i in ('tv1 1000', 'tv2 2000'):
        cart.add(TV(*i.split()))
    # один стол (Table),
    cart.add(Table('Стол', '555'))
    # два ноутбука (Notebook)
    for i in ('nout1 3000', 'nout2 4000'):
        cart.add(Notebook(*i.split()))
    # одну кружку (Cup).
    cart.add(Cup('Кружка', '100'))

    # проверка объектов в списке cart.goods
    counts = {}
    for obj in cart.goods:
        class_name = type(obj).__name__
        if class_name in counts:
            counts[class_name] += 1
        else:
            counts[class_name] = 1

    assert counts == {'TV': 2, 'Table': 1, 'Notebook': 2, 'Cup': 1}, "количество объектов неправильное"
    assert cart.get_list() == ['tv1: 1000', 'tv2: 2000', 'Стол: 555', 'nout1: 3000', 'nout2: 4000', 'Кружка: 100'], \
        "метод get_list отработал некорректно"

    print("Правильный ответ !")
