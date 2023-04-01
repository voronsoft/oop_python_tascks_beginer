# TEST-TASK___________________________________
def test_7(Line):
    line = Line(1, 2, 3, 4)
    assert len(line.__dict__) == 4
    assert hasattr(Line, "set_coords"), "В классе не определён метод set_coords"
    assert hasattr(Line, "get_coords"), "В классе не определён метод get_coords"
    assert hasattr(Line, "draw"), "В классе не определён метод draw"

    assert '_Line__x1' in line.__dict__ and '_Line__y1' in line.__dict__ and '_Line__x2' in line.__dict__ and \
           '_Line__y2' in line.__dict__, "Ошибка, проверьте имена атрибутов, а так же атрибуты должны быть приватными"

    assert type(line.get_coords()) == tuple and \
           len(line.__dict__) == len(line.get_coords()), "Метод get_coords вернул неправильный результат"

    # проверка метода draw()
    import io
    import sys

    # Создаю объект StringIO
    output = io.StringIO()
    # Перенаправляю стандартный вывод в StringIO
    sys.stdout = output
    # выполняю метод draw() что бы перехватить то что будет выведено в консоль принтом
    line.draw()
    # Получаю данные из StringIO и записываю в переменную output_str
    output_str = output.getvalue()
    # Возвращаю перехват вывода, на стандартный вывод в консоль
    sys.stdout = sys.__stdout__
    # проверяю что данные в output_str это одна строка
    # проверяю что перенос строки в самом конце
    # проверяю что '\n' в строке только 1
    assert type(output_str) == str and output_str[-1:] == '\n' and output_str.count(
        '\n') == 1, "Ошибка, метод draw работает неверно"
    # end draw
    print('Правильный ответ !')
