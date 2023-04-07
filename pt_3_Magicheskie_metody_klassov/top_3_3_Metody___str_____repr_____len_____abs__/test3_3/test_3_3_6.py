# TEST-TASK___________________________________
def test_6(Complex):
    assert isinstance(Complex.real, property), "Метод real не является объектом-свойством (property)"
    assert isinstance(Complex.img, property), "Метод img не является объектом-свойством (property)"

    cmp = Complex(7, 8)
    assert len(cmp.__dict__) == 2, "должно быть два локальных свойства действительная часть и мнимая часть"

    try:
        cmp.img = ""
        cmp.img = str()
        cmp.real = ""
        cmp.real = str()

    except ValueError:
        assert True
    else:
        assert False, "ошибка, не была сгенерирована ошибка ValueError при записи некорректных данных"

    cmp.real = 3
    assert cmp.real == 3, "ошибка при изменении значения на другое"

    cmp.img = 4
    assert cmp.img == 4, "ошибка при изменении значения на другое"
    assert abs(cmp) == 5, \
        "ошибка в возвращении модуля комплексного числа (вычисляется по формуле: sqrt(real*real + img*img)"

    print("Правильный ответ !")
