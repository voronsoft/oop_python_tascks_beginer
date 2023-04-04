# TEST-TASK___________________________________
def test_8(Handler):
    assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"

    @Handler(methods=('GET', 'POST'))
    def contact2(request):
        return "контакты"

    assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
    assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
    assert contact2({}) == "GET: контакты", \
        "декорированная функция вернула неверные данные при указании пустого словаря"

    @Handler(methods=('POST'))
    def index(request):
        return "index"

    assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
    assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
    assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"

    print("Хорошая работа, так держать !!")
