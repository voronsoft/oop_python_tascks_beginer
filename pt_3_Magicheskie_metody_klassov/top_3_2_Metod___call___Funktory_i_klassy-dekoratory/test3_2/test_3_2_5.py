# TEST-TASK___________________________________
def test_5(DigitRetrieve):
    dg = DigitRetrieve()

    assert dg("123") == 123, "целые числа в строке следует приводить к целочисленному типу данных"
    assert dg("45.54") == None, "любые не целочисленные типы данных нужно приводить к значению None"
    assert dg("-56") == -56, "целые числа в строке следует приводить к целочисленному типу данных"
    assert dg("12fg") == None, "любые не целочисленные типы данных нужно приводить к значению None"
    assert dg("abc") == None, "любые не целочисленные типы данных нужно приводить к значению None"
    print("Правильный ответ !!")
