# TEST-TASK___________________________________
def test_6(RenderList):
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    #
    render = RenderList("ol")
    html = render(lst)
    assert html == '<ol>\n<li>Пункт меню 1</li>\n<li>Пункт меню 2</li>\n<li>Пункт меню 3</li>\n</ol>', \
        "неправильный формат строки"
    #
    render = RenderList("ul")
    html = render(lst)
    assert html == '<ul>\n<li>Пункт меню 1</li>\n<li>Пункт меню 2</li>\n<li>Пункт меню 3</li>\n</ul>', \
        "неправильный формат строки"
    #
    render = RenderList("div")
    html = render(lst)
    assert html == '<ul>\n<li>Пункт меню 1</li>\n<li>Пункт меню 2</li>\n<li>Пункт меню 3</li>\n</ul>', \
        "неправильный формат строки"

    print("Ух ты, правильный ответ !!")
