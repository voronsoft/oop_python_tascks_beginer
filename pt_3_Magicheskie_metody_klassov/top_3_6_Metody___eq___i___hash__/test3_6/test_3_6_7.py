# TEST-TASK___________________________________
def test_7(DataBase, Record, lst_in, db):
    db22345 = DataBase('123')
    r1 = Record('fio', 'descr', 10)
    r2 = Record('fio', 'descr', 10)
    assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

    db22345.write(r2)
    r22 = db22345.read(r2.pk)
    assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, \
        "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

    assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

    fio = lst_in[0].split(';')[0].strip()
    v = list(db.dict_db.values())
    if fio == "Балакирев С.М.":
        assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
                v[3]) == 1, "неверно сформирован словарь dict_db"

    if fio == "Гейтс Б.":
        assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
                v[3]) == 1, "неверно сформирован словарь dict_db"
    print("Приавильный ответ, отлично !")
