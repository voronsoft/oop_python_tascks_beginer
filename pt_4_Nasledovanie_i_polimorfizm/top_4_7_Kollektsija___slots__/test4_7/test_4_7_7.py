# TEST-TASK___________________________________
def test_7(Note, Notes, notes):
    try:
        Note(1)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка ValueError при проверке ноты"

    assert Note('до')._ton == 0, "тон по умолчанию должен быть 0"

    try:
        Note('до', -2)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалась ошибка ValueError при проверке тональности"

    assert '_name' in Note('до').__dict__ and '_ton' in Note('до').__dict__, \
        "в нотах должны быть локальные атрибуты _name и _ton"

    assert "__slots__" in Notes.__dict__, "в Notes не найден __slots__"
    assert Notes.__dict__["__slots__"] == ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'], \
        "__slots__ должно находиться допускаемые ноты - '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'"

    try:
        notes.__dict__
    except AttributeError:
        assert True
    else:
        assert False, "в объекте класса Notes не должно быть __dict__"

    assert '_do' in notes.__slots__ and isinstance(notes._do, Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_re' in notes.__slots__ and isinstance(notes._re, Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_mi' in notes.__slots__ and isinstance(notes._mi, Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_fa' in notes.__slots__ and isinstance(notes._fa, Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_solt' in notes.__slots__ and isinstance(notes._solt,
                                                     Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_la' in notes.__slots__ and isinstance(notes._la, Note), "атрибуты нот должны быть экземплярами класса Note"
    assert '_si' in notes.__slots__ and isinstance(notes._si, Note), "атрибуты нот должны быть экземплярами класса Note"

    assert notes._re._ton == 0, "ошибка значения в атрибуте"
    assert notes._solt._ton == 0, "ошибка значения в атрибуте"

    assert id(notes) == id(Notes()) == id(Notes()), "Объект класса Notes должен быть всего один"

    assert notes[0]._name == "до", "операция notes[x] работает некорректно"
    assert notes[1]._name == "ре", "операция notes[x] работает некорректно"
    assert notes[2]._name == "ми", "операция notes[x] работает некорректно"
    assert notes[3]._name == "фа", "операция notes[x] работает некорректно"

    notes[3]._ton = -1
    assert notes[3]._ton == -1, "при изменении тональности ноты произошла ошибка"

    try:
        notes[3]._ton = 2
    except ValueError:
        assert True
    else:
        assert False, "при операции изменить тон на некорректное значение не сгенерировалась ошибка ValueError"

    print("вы справились! 7")
