# TEST-TASK___________________________________
def test_9(Input, Dense, NetworkIterator, Layer):
    nt = Input(12)
    layer = nt(Dense(nt.inputs, 1024, 'relu'))
    layer = layer(Dense(layer.inputs, 2048, 'relu'))
    layer = layer(Dense(layer.inputs, 10, 'softmax'))

    n = 0
    for x in NetworkIterator(nt):
        assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
        n += 1

    assert n == 4, "итератор перебрал неверное число слоев"
    print("Правильный ответ, умница!")
