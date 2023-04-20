# TEST-TASK___________________________________
def test_5(Person):
    pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
    assert hasattr(Person, "__next__"), "необъявлен метод  __next__"
    assert hasattr(Person, "__iter__"), "необъявлен метод  __iter__"

    assert hasattr(pers, "fio") and hasattr(pers, 'job') and hasattr(pers, 'old') and hasattr(pers, 'salary') and \
           hasattr(pers, 'year_job'), "в объекте отсутствуют необходимые локальные атрибуты"

    assert pers[0] == 'Гейтс Б.' and pers[1] == 'бизнесмен' and pers[2] == 61 and pers[3] == 1000000 and pers[4] == 46, \
        "ошибка при обращнии к значению элемента p[0] (значение не соответствует порядку локальных атрибутов"

    # p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
    pers[0] = "Балакирев С."
    assert pers.__dict__['fio'] == "Балакирев С.", "ошибка при записи значения методом pers[0] = 'Балакирев С.'"

    assert [v for v in pers] == ['Балакирев С.', 'бизнесмен', 61, 1000000, 46], \
        "x = [v for v in p]: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job"

    try:
        pers[5]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка IndexError при вводе некоррректного индекса"

    print("Правильный ответ ))")
