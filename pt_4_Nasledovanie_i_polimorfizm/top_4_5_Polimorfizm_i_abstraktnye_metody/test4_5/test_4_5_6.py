# TEST-TASK___________________________________
def test_6(Model, ABC, ModelForm):
    assert issubclass(Model, ABC) and '_abc_impl' in dir(Model), "класс Model не унаследован от класса ABC"
    assert hasattr(Model, "get_pk"), "в классе Model, не переопределен метод get_pk"
    assert hasattr(Model, "get_info"), "в классе Model, не переопределен метод get_info"

    try:
        Model.get_pk.__isabstractmethod__
    except AttributeError:
        assert False, "get_pk не является абстрактным методом"
    else:
        assert True

    assert issubclass(ModelForm, Model), "класс ModelForm не унаследован от класса Model"
    assert ModelForm.get_pk != Model.get_pk, "не переопределен метод get_pk в классе ModelForm"

    form = ModelForm("Логин", "Пароль")
    assert "_login" in form.__dict__, "не найден атрибут _login"
    assert "_password" in form.__dict__, "не найден атрибут _password"
    assert "_id" in form.__dict__, "не найден атрибут _id"
    assert form.get_pk() == 1, "метод get_pk работает некорректно"

    print("Прекрасный ответ.")
