# TEST-TASK___________________________________
def test_4(WordString):

    words = WordString()
    a = [_ for _ in words.__dict__.keys()]
    assert words.__dict__[a[0]] == '', "объект должен создаваться командой words = WordString()"

    words2 = WordString("sdfsd fsdf")
    a = [_ for _ in words2.__dict__.keys()]
    assert words2.__dict__[a[0]] == 'sdfsd fsdf', "объект должен создаваться командой words = WordString('string')"

    assert len(words2) == 2, "метод len работает некорректно"

    words2 = WordString("sdfsd fsdf   hjk")
    assert len(words2) == 3, \
        "метод len работает некорректно возможно вы не учли, что пробелов может быть более одного в строке"

    assert words2(1) == 'fsdf' and words2(2) == 'hjk', \
        "некорректно работает метод который должен вернуть нужное слово по индексу"

    assert hasattr(WordString, 'string'), "в классе нет метода string"
    assert isinstance(WordString.string, property), "Метод string не является объектом-свойством (property)"

    assert '_WordString__string' in words2.__dict__, "атрибут string должен быть приватным"
    print("Правильный ответ, отлично !")

    import io
    import sys

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    #
    words = WordString()
    words.string = "Курс по Python ООП"
    n = len(words)
    first = "" if n == 0 else words(0)
    print(f"Число слов: {n}; первое слово: {first}")
    #
    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
    assert output == "Число слов: 4; первое слово: Курс\n"
