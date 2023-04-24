# TEST-TASK___________________________________
def test_6(DetailView, GenericView):
    dv = DetailView()  # по умолчанию methods=('GET',)
    assert issubclass(DetailView, GenericView), "ошибка, класс DetailView должен быть дочерним классом от GenericView"
    assert dv.methods == ('GET',), "по умолчанию атрибут methods должен принимать значение ('GET',)"

    dv = DetailView(methods=('PUT', 'POST'))
    assert dv.methods == ('PUT', 'POST'), "ошибка в локальном атрибуте methods неверные"

    dv = DetailView()
    assert hasattr(dv, "render_request") and callable(dv.render_request), "необъявлен метод render_request"
    assert id(GenericView.get) is not id(DetailView.get), "вы не переопределили метод get в дочернем классе"

    html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')  # вернёт - строку 'url: https://site.ru/home'
    assert html == 'url: https://site.ru/home'

    try:
        dv.render_request({'url': 'https://site.ru/home'}, 'ttt')
    except TypeError:
        assert True
    else:
        assert False, "ошибка, не сгенерировалась ошибка TypeError когда метод запроса неправильный"

    dv = DetailView()
    try:
        dv.get('123')
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError при проверке является ли строка словарем "

    try:
        dv.get({"1": 123})
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка TypeError при проверке на наличие url в словаре"

    assert dv.get({"url": 123}) == 'url: 123', "метод get вернул неверный формат строки"

    print("Правильный ответ !!!")
