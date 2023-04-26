# TEST-TASK___________________________________
def test_6(Callback, Router):
    @Callback('/about', Router)
    def about():
        return '<h1>About</h1>'

    route = Router.get('/about')
    ret = route()
    assert ret == '<h1>About</h1>', "декорированная функция вернула неверные данные"

    route = Router.get('/')
    assert route is None, "Класс Router, при вызове метода get, вернул неверные данные"

    print("Всё получилось!")
