# TEST-TASK___________________________________
def test_3(Lector, Mentor, Reviewer, Student):
    assert issubclass(Lector, Mentor), "Lector, должен быть подклассом класса Mentor"
    assert issubclass(Reviewer, Mentor), "Reviewer, должен быть подклассом класса Mentor"

    # В самих классах Lector и Reviewer необходимо объявить метод:
    # def set_mark(self, student, mark): ...
    assert hasattr(Lector, "set_mark"), "не объявлен метод def set_mark(self, student, mark)"
    assert hasattr(Reviewer, "set_mark"), "не объявлен метод def set_mark(self, student, mark)"

    lector = Lector("Балакирев С.М.", "Информатика")
    assert "_fio" in lector.__dict__, "в экземпляре класса Lector не найден атрибут _fio"
    assert "_subject" in lector.__dict__, "в экземпляре класса Lector не найден атрибут _fio"

    reviewer = Reviewer("Гейтс Б.", "Информатика")
    assert "_fio" in lector.__dict__, "в экземпляре класса Reviewer не найден атрибут _fio"
    assert "_subject" in lector.__dict__, "в экземпляре класса Reviewer не найден атрибут _fio"

    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]

    lector.set_mark(students[0], 4)
    assert students[0]._lect_marks[0] == 4, "в классе Lector некорректно работает метод set_mark"
    lector.set_mark(students[1], 2)
    assert students[1]._lect_marks[0] == 2, "в классе Lector некорректно работает метод set_mark"

    reviewer.set_mark(students[0], 5)
    assert students[0]._house_marks[0] == 5, "в классе Reviewer некорректно работает метод set_mark"
    reviewer.set_mark(students[1], 3)
    assert students[1]._house_marks[0] == 3, "в классе Reviewer некорректно работает метод set_mark"

    assert Lector.__str__ != object.__str__, "в классе Lector нужно переопределить метод __str__"
    assert Reviewer.__str__ != object.__str__, "в классе Reviewer нужно переопределить метод __str__"

    import io
    import sys

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    print(persons[0])
    output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    assert output == 'Лектор Балакирев С.М.: предмет Информатика\n', \
        "для объектов класса Lector формат вывода должен быть: Лектор <ФИО>: предмет <предмет>"

    console_out = io.StringIO()  # Создаем буфер
    sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
    print(students[0])
    output1 = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
    assert output1 == 'Студент Иванов А.Б.: оценки на лекциях: [4]; оценки за д/з: [5]\n', \
        "для объектов класса Reviewer формат вывода должен быть: Эксперт <ФИО>: предмет <предмет>"

    sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние

    print("Правильный ответ !")
