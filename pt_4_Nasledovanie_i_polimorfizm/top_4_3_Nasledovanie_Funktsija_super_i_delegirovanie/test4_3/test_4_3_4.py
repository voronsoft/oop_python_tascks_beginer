# TEST-TASK___________________________________
def test_4(ArtObject, Thing, Computer, Auto, Mercedes, Toyota):
    assert issubclass(Thing, object), "Thing это родительский класс"
    assert issubclass(ArtObject, Thing), "ArtObject дочерний класс класса Thing"
    assert issubclass(Computer, Thing), "Computer дочерний класс класса Thing"
    assert issubclass(Auto, Thing), "Auto дочерний класс класса Thing"
    assert issubclass(Mercedes, Auto), "класс Mercedes наследуется от Auto наследуется от Thing"
    assert issubclass(Toyota, Auto), "класс Toyota наследуется от Auto наследуется от Thing"

    thing = Thing("предмет", 2.2)
    assert len(thing.__dict__) == 2 and "weight" in thing.__dict__ and "name" in thing.__dict__, \
        "в Thing должно быть два атрибута: name, weight"

    art = ArtObject('Картина', 2.1, 'Норов', 1977)
    assert len(art.__dict__) == 4 and \
           "name" in art.__dict__ and type(art.name) is str and \
           "weight" in art.__dict__ and type(art.weight) is float and \
           "author" in art.__dict__ and type(art.author) is str and \
           "date" in art.__dict__ and type(art.date) is str and art.date.isdigit(), \
        "в объекте класса ArtObject не полный набор локальных атрибутов или ошибка типа значений"

    comp = Computer('Spectrum', 1.2, 8000, 'INTEL')
    assert len(comp.__dict__) == 4 and \
           "cpu" in comp.__dict__ and type(comp.name) is str and \
           "memory" in comp.__dict__ and type(comp.memory) is int and \
           "name" in comp.__dict__ and type(comp.name) is str and \
           "weight" in comp.__dict__ and type(comp.weight) is float, \
        "в объекте класса ArtObject не полный набор локальных атрибутов или ошибка типа значений"

    auto = Auto('BMW', 1960, (100, 200, 300))
    assert len(auto.__dict__) == 4 and \
           "name" in auto.__dict__ and type(auto.name) is str and \
           "weight" in auto.__dict__ and type(auto.weight) is float and \
           "dims" in auto.__dict__ and type(auto.dims) is tuple and \
           "model" in auto.__dict__ and type(auto.model) is str, \
        "в объекте класса Auto не полный набор локальных атрибутов или ошибка типа значений"

    model_M = Mercedes('Viana', 2.5, (2.5, 3.4, 5.2), 'Mercedes', 3)
    assert len(model_M.__dict__) == 5 and \
           "name" in model_M.__dict__ and type(model_M.name) is str and \
           "weight" in model_M.__dict__ and type(model_M.weight) is float and \
           "dims" in model_M.__dict__ and type(model_M.dims) is tuple and \
           "old" in model_M.__dict__ and type(model_M.old) is int and \
           "model" in model_M.__dict__ and type(model_M.model) is str, \
        "в объекте класса Mercedes не полный набор локальных атрибутов или ошибка типа значений"

    model_T = Toyota('Land Cruiser', 2.2, (2.5, 3.4, 5.2), 'Toyota', True)
    assert len(model_T.__dict__) == 5 and \
           "name" in model_T.__dict__ and type(model_T.name) is str and \
           "weight" in model_T.__dict__ and type(model_T.weight) is float and \
           "dims" in model_T.__dict__ and type(model_T.dims) is tuple and \
           "wheel" in model_T.__dict__ and type(model_T.wheel) is bool and \
           "model" in model_T.__dict__ and type(model_T.model) is str, \
        "в объекте класса Mercedes не полный набор локальных атрибутов"
    print("Отлично!")
