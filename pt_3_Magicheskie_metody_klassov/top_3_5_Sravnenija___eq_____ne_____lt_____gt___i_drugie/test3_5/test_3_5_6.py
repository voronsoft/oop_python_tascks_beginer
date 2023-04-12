# TEST-TASK___________________________________
def test_6(Morph, dict_words, answer, text):
    assert hasattr(Morph, "add_word"), "объявите метод add_word"
    assert hasattr(Morph, "get_words"), "объявите метод get_words"
    assert hasattr(Morph, "__eq__"), "необъявлен метод для операции == и !="
    assert len(dict_words) == 5, "не все объекты с словоформами добавлены в список dict_words"
    assert dict_words[0] == 'связях' and dict_words[0] != 'св', "некорректно работает метод  mw1 == 'word'"
    assert 'связях' == dict_words[0] and 'св' != dict_words[0], "некорректно работает метод 'word' == mw1"

    if text == "Мы будем устанавливать связь завтра днем." and answer == 2:
        print("Правильно !")
    elif text == "Мы будем устанавливать связь завтра днем." and answer != 2:
        print("ошибка, пересчет вхождений не правильный")
