# TEST-TASK___________________________________
def test_4(lst_shop, ShopItem, Dimensions, lst_shop_sorted):
    assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

    lst_sp = []
    lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
    lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
    lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
    lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

    lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
    s = [x.name for x in lst_shop_sorted]
    assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

    d1 = Dimensions(40, 30, 120)
    d2 = Dimensions(40, 30, 120)
    d3 = Dimensions(30, 20, 100)
    assert d1 <= d2, "неверно отработал оператор <="
    assert d3 <= d2, "неверно отработал оператор <="
    assert d3 < d2, "неверно отработал оператор <"

    d2.a = 10
    d2.b = 10
    d2.c = 10
    assert d2 < d1, "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"

    print("Правильный ответ.")
