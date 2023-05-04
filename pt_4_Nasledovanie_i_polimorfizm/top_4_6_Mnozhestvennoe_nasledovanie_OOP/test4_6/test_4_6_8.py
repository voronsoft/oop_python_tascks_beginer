# TEST-TASK___________________________________
def test_8(DetailView, RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
    assert issubclass(DetailView, GeneralView), "класс DetailView должен наследоваться от класса GeneralView"

    class DetailView(RetriveMixin, UpdateMixin, GeneralView):
        allowed_methods = ('GET', 'POST',)

    view = DetailView()

    try:
        html = view.render_request({'url': '123', 'method': 'POST'})
    except AttributeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение AttributeError при вызове команды render_request({'url': '123', 'method': 'POST'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

    try:
        html = view.render_request({'url': '123', 'method': 'PUT'})
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при вызове команды render_request({'url': '123', 'method': 'PUT'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

    html = view.render_request({'url': '123', 'method': 'GET'})
    assert html == "GET: 123", "метод render_request вернул неверные данные"

    class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
        allowed_methods = ('GET', 'POST',)

    view = DetailView()
    html = view.render_request({'url': '123', 'method': 'POST'})
    assert html == "POST: 123", "метод render_request вернул неверные данные"
    print("Здорово, всё верно. 8")
