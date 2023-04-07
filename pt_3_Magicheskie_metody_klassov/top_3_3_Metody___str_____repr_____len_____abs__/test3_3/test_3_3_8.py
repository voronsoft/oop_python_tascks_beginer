# TEST-TASK___________________________________
def test_8(Clock, DeltaClock):
    a = Clock(2, 45, 0)
    b = Clock(1, 15, 0)
    assert hasattr(a, 'hours') and hasattr(a, 'minutes') and hasattr(a, 'seconds'), \
        "ошибка атрибутов в экземпляре класса - Clock"

    assert hasattr(Clock, "get_time") and callable(Clock.get_time), "отсутствует метод get_time"
    assert a.get_time() == 9900, "метод get_time должен возвращать возвращает текущее время в секундах " \
                                 "(то есть, значение hours * 3600 + minutes * 60 + seconds)"

    x = Clock(1.0, -15, 0)
    assert all(True if type(_) is int and _ >= 0 else False for _ in a.__dict__.values()), \
        "значения времени должны быть int >= 0"

    dt = DeltaClock(a, b)
    assert all(True if isinstance(_, Clock) else False for _ in dt.__dict__.values()), \
        "экземпляр класса должен содержать объекты класса Clock"

    assert str(dt) == '01: 30: 00', \
        "ошибка метод str() вернул строку неправильного формата.. (необходимый формат 00: 00: 00)"
    assert str(dt)[0:2].isdigit() and str(dt)[4:6].isdigit() and str(dt)[8:10].isdigit(), \
        "время должно иметь двузначный формат пример 01: 02: 20"

    len_dt = len(dt)  # разницу времен clock1 - clock2 в секундах (целое число)
    assert len(dt) == 5400, "ошибка формата строки, метод len() должен возвращать разницу времени в секундах"

    # не изменять !!
    import io
    import sys
    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    # end

    print(dt)  # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды

    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
    assert output == '01: 30: 00\n', "метод print() должен вывести в консоль строку формата 01: 30: 00"

    print("Правильный ответ !")
