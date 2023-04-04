# TEST-TASK___________________________________
def test_7(HandlerGET):
    @HandlerGET
    def index(request):
        return "главная страница сайта"

    res = index({"method": "GET"})
    assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"

    res = index({"method": "POST"})
    assert res is None, "декорированная функция вернула неверные данные"

    res = index({"method": "POST2"})
    assert res is None, "декорированная функция вернула неверные данные"

    res = index({})
    assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"

    print("Прекрасно, правильно.")
