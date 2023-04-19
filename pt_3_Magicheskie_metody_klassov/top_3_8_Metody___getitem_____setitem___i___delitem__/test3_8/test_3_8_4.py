# TEST-TASK___________________________________
def test_4(Array, Integer):
    ar_int = Array(5, cell=Integer)
    assert hasattr(ar_int, "max_length") and hasattr(ar_int, "cell"), "ошибка локальных атрибутов"

    cell = Integer(10)
    assert isinstance(Integer.value, property), " в классе не объявлен объект свойство property value"
    assert cell.value == 10, "ошибка при считывании значения через свойство объект"

    cell.value = 100
    assert cell.value == 100, "ошибка при записи нового значения в защищенный локальный атрибут"

    try:
        cell.value = 100.0
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось ошибка ValueError"

    assert type(cell.value) is int, "не сгенерировалось ошибка ValueError"

    # value = ar_int[0] # получение значения из первого элемента (ячейки) массива ar
    assert ar_int[0] == 0, "ошибка при получение значения из первого элемента (ячейки) массива"

    # ar[1] = value # запись нового значения во вторую ячейку массива ar
    ar_int[1] = 10
    assert ar_int[1] == 10, "ошибка при записи нового значения во вторую ячейку массива ar"

    # Если индекс не целое число или число меньше нуля или больше либо равно max_length,
    # то должно генерироваться исключение командой:
    # raise IndexError('неверный индекс для доступа к элементам массива')
    try:
        ar_int[5]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось ошибка IndexError"

    try:
        ar_int[-1]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось ошибка IndexError"

    # проверка вывода в консоль
    import io
    import sys

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    print(ar_int)
    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
    assert output == '0 10 0 0 0\n', "ошибка в консоль выводится не правильный ответ"
    print("Правильный ответ !!")
