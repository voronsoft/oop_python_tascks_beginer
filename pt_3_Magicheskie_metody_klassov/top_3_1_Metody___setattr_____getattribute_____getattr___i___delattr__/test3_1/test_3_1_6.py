# TEST-TASK___________________________________
def test_6(Museum, Picture, Mummies, Papyri):
    mus = Museum("Эрмитаж")
    assert type(mus.name) is str, "название должно быть строкой"
    assert mus.exhibits == [], "exhibits должен быть списком"
    assert hasattr(mus, "add_exhibit"), "метод не объявлен"
    assert hasattr(mus, "remove_exhibit"), "метод не объявлен"
    assert hasattr(mus, "get_info_exhibit"), "метод не объявлен"

    pic = Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
                  "Вдохновляющая, устрашающая, волнующая картина")
    assert 'name' in pic.__dict__.keys() and 'descr' in pic.__dict__.keys() and 'author' in pic.__dict__.keys(), "ошибка в локальных атрибутах"

    mum = Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации")
    assert 'name' in mum.__dict__.keys() and 'location' in mum.__dict__.keys() and 'descr' in mum.__dict__.keys(), "ошибка в локальных атрибутах"

    p = Papyri("Ученья для, не злата ради",
               "Древняя Россия",
               "Самое древнее найденное рукописное свидетельство о языках программирования")
    assert 'name' in p.__dict__.keys() and 'date' in p.__dict__.keys() and 'descr' in p.__dict__.keys(), "ошибка в локальных атрибутах"
    assert type(p.date) is str, "название должно быть строкой"

    # проверка методов
    # add_exhibit(self, obj) - добавление нового экспоната в музей (в конец списка exhibits);
    # remove_exhibit(self, obj) - удаление экспоната из музея (из списка exhibits по ссылке obj - на экспонат)
    # get_info_exhibit(self, indx) - получение информации об экспонате (строка) по индексу списка (нумерация с нуля).
    mus.add_exhibit(pic)
    assert mus.exhibits[0] == pic and len(mus.exhibits) == 1, "некорректно отработал метод add_exhibit"

    mus.remove_exhibit(pic)
    assert len(mus.exhibits) == 0 and pic not in mus.exhibits, "некорректно отработал метод remove_exhibit"

    mus.add_exhibit(p)
    mus.add_exhibit(pic)
    answ = mus.get_info_exhibit(0)
    assert answ == f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}", "некорректно отработал метод get_info_exhibit"
    print("Правильный ответ. )")
