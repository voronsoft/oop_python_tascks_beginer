# TEST-TASK___________________________________
def test_5(Planet, s_system, SolarSystem):
    temp = Planet('Меркурий', 4878, 87.97, 1407.5)
    assert temp.__dict__ == temp.__dict__ and len(
        temp.__dict__) == 4, "в экземпляре класса Planet ошибка лок атрибутов"

    assert '_name' in temp.__dict__ and \
           '_diametr' in temp.__dict__ and \
           '_period_solar' in temp.__dict__ and \
           '_period' in temp.__dict__, "ошибка локальных атрибутов класса Planet"

    try:
        s_system.__dict__
    except AttributeError:
        assert True
    else:
        assert False, "в s_system не найден __slots__"

    assert "__slots__" in SolarSystem.__dict__
    assert SolarSystem.__dict__["__slots__"] == ['_mercury',
                                                 '_venus',
                                                 '_earth',
                                                 '_mars',
                                                 '_jupiter',
                                                 '_saturn',
                                                 '_uranus',
                                                 '_neptune'
                                                 ], "ошибка в списке __slots__"

    s_system2 = SolarSystem()
    assert id(s_system) == id(s_system2), "одновременно в программе два и более объектов класса SolarSystem недопустимо"

    assert all(True if _ in dir(s_system) else False for _ in SolarSystem.__dict__["__slots__"]), \
        "не все планеты созданы в s_system из коллеции __slots__"

    assert s_system._earth.__dict__ == {'_name': 'Земля', '_diametr': 12756, '_period_solar': 365.3, '_period': 23.93}, \
        "ошибка s_system._earth"

    assert s_system._mercury.__dict__ == {'_name': 'Меркурий', '_diametr': 4878, '_period_solar': 87.97,
                                          '_period': 1407.5}, \
        "ошибка s_system._mercury"

    assert s_system._jupiter.__dict__ == {'_name': 'Юпитер', '_diametr': 142800, '_period_solar': 4330, '_period': 9.9}, \
        "ошибка s_system._jupiter"

    assert s_system._mars.__dict__ == {'_name': 'Марс', '_diametr': 6794, '_period_solar': 687, '_period': 24.62}, \
        "ошибка s_system._mars"

    assert s_system._neptune.__dict__ == {'_name': 'Нептун', '_diametr': 49528, '_period_solar': 60150,
                                          '_period': 16.1}, \
        "ошибка s_system._neptune"

    assert s_system._saturn.__dict__ == {'_name': 'Сатурн', '_diametr': 120660, '_period_solar': 10753,
                                         '_period': 10.63}, \
        "ошибка s_system._saturn"

    assert s_system._uranus.__dict__ == {'_name': 'Уран', '_diametr': 51118, '_period_solar': 30665, '_period': 17.2}, \
        "ошибка s_system._uranus"

    assert s_system._venus.__dict__ == {'_name': 'Венера', '_diametr': 12104, '_period_solar': 224.7,
                                        '_period': 5832.45}, \
        "ошибка s_system._venus"

    print("Правильный ответ ! 5")
