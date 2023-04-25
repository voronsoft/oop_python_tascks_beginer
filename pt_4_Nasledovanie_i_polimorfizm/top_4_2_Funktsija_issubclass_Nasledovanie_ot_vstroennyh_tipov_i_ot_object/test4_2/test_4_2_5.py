# TEST-TASK___________________________________
def test_5(Plants, Protists, Mosses, Flowering, Animals, Worms, Mammals, Human, Monkeys, Monkey, Worm, Person, Flower,
           lst_animals, lst_plants, lst_mammals):
    assert issubclass(Plants, Protists), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Mosses, Plants), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Flowering, Plants), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Animals, Protists), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Worms, Animals), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Mammals, Animals), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Human, Mammals), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Monkeys, Mammals), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Monkey, Monkeys), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Human, Mammals), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Worm, Worms), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Person, Human), "ошибка в построении унаследования подклассов от родительских классов"
    assert issubclass(Flower, Flowering), "ошибка в построении унаследования подклассов от родительских классов"

    assert len(lst_animals) == 6 and all(True if isinstance(_, Animals) else False for _ in lst_animals), \
        "список lst_animals сформирован некорректно"

    assert len(lst_plants) == 2 and all(True if isinstance(_, Plants) else False for _ in lst_plants), \
        "список lst_plants сформирован некорректно"

    assert len(lst_mammals) == 4 and all(True if isinstance(_, Mammals) else False for _ in lst_mammals), \
        "список lst_mammals сформирован некорректно"

    print("Отлично!")
