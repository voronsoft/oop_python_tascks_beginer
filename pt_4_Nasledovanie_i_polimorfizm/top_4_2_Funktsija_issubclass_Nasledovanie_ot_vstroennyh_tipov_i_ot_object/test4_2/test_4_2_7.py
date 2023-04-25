# TEST-TASK___________________________________
def test_7(VideoItem, VideoRating):
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
    assert "title" in v.__dict__ and type(v.title) is str and v.title == 'Курс по Python ООП' and \
           "descr" in v.__dict__ and type(v.descr) is str and v.descr == 'Подробный курс по Python ООР' and \
           "path" in v.__dict__ and type(v.path) is str and v.path == "D:/videos/python_oop.mp4" and \
           "rating" in v.__dict__ and isinstance(v.rating, VideoRating), "ошибка в локальных атрибутах и их значениях"

    rating = VideoRating()
    assert "_VideoRating__rating" in rating.__dict__, "атрибут __rating должен быть приватным"
    assert rating.__dict__['_VideoRating__rating'] == 0, "__rating, по умолчанию должен принимать значение 0"

    assert isinstance(VideoRating.rating, property), \
        "в классе VideoRating не объявлен объект-свойство (property) с именем rating"

    assert rating.rating == 0, "при считывании значения рейтинга возникла ошибка"

    rating.rating = 5
    assert rating.rating == 5, " при записи нового значения в защищённый атрибут __rating возникла ошибка"

    try:
        rating.rating = 6
    except ValueError:
        assert True
    else:
        assert False, "значение рейтинга должно быть в диапазоне 0 - 5"

    try:
        rating.rating = 1.5
    except ValueError:
        assert True
    else:
        assert False, "значение рейтинга должно быть в диапазоне 0 - 5 и только целым числом"

    if type(rating.rating) is not int:
        assert False, "значение рейтинга может быть только целое число"

    assert isinstance(v.rating, VideoRating), \
        "в каждом объекте класса VideoItem должен быть локальный атрибут rating - объект класса VideoRating"

    assert v.rating.rating == 0, "при считывании значения рейтинга из экз. класса VideoItem получены неверные данные"

    v.rating.rating = 5
    assert v.rating.rating == 5, "запись значения рейтинга в экз. класса VideoItem работает некорректно"

    print("Молодец, хорошая работа !")
