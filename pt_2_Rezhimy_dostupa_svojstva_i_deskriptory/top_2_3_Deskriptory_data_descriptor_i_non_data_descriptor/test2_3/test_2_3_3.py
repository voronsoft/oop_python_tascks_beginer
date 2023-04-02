# TEST-TASK___________________________________
def test_3(temp):
    try:
        assert len(
            temp) == 2 and "дескриптор данных (data descriptor), когда в классе присутствуют методы __get__ и __set__" in temp and \
               "дескриптор не данных (non-data descriptor), когда в классе присутствует метод __get__, но отсутствует метод __set__" in temp

    except:
        print("Пока неправильно попробуйте другие варианты")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
