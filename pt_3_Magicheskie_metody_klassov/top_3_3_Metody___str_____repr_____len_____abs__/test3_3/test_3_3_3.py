# TEST-TASK___________________________________
def test_3(Model):
    import io
    import sys

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    #
    model = Model()
    model.query(id=1, fio='Sergey', old=33)
    #
    print(model)
    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние

    if output == "Model: id = 1, fio = Sergey, old = 33\n":
        print(output)
        print("Правильный ответ !")
    else:
        print(f"Ваш ответ: {output}")
        print(f"Правильный ответ: Model: id = 1, fio = Sergey, old = 33")
        print("\nошибка, формат строки неправильный")
