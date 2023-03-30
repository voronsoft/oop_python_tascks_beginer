# TEST-TASK___________________________________
def test_8(temp):
    try:
        assert len(temp) == 4 and \
               "Переменная b = s2.is_empty будет ссылаться на локальный атрибут is_empty объекта s2" in temp and \
               "Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty примет новое значение True" in temp and \
               "Последняя команда создаст локальное свойство is_empty со значением True в экземпляре s2" in temp and \
               "Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String" in temp
    except:
        print("Неправильно, попробуйте снова")
    else:
        [print(_) for _ in temp]
        print("Правильно так держать !")
