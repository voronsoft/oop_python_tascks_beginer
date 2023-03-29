# TEST-TASK___________________________________
def test_8(x, tb1, tb2):
    TravelBlog = x
    try:
        issubclass(TravelBlog, object)
    except NameError:
        print("Вы не создали класс TravelBlog")
    else:
        try:
            isinstance(tb1, TravelBlog) and isinstance(tb2, TravelBlog)
        except NameError:
            print("Вы не создали экземпляры класса - tb1 и tb2")
        else:
            assert len(tb1.__dict__) == 2 and "name" in tb1.__dict__ and \
                   "days" in tb1.__dict__, "Должно быть два локальных свойства name и days"
            assert len(tb2.__dict__) == 2 and "name" in tb2.__dict__ and \
                   "days" in tb2.__dict__, "Должно быть два локальных свойства name и days"
            assert TravelBlog.total_blogs == 2, "Атрибут класса total_blogs, должен быть равен 2м"

    assert tb1.name == 'Франция' and tb1.days == 6, "Какое то значение локального атрибута tb1 неверное"
    assert tb2.name == 'Италия' and tb2.days == 5, "Какое то значение локального атрибута tb2 неверное"
    print("Правильно !")
