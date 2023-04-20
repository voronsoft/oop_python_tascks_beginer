# TEST-TASK___________________________________
def test_7(IterColumn):
    lst = [['x00', 'x01', 'x02', 'x02'],
           ['x10', 'x11', 'x12', 'x13'],
           ['x20', 'x21', 'x22', 'x23'],
           ['x30', 'x31', 'x32', 'x33'],
           ['x40', 'x41', 'x42', 'x43', 'x45', 'x46']
           ]
    it = IterColumn(lst, 1)
    temp = []
    it_iter = iter(it)
    for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
        temp.append(x)

    assert temp == ['x01', 'x11', 'x21', 'x31', 'x41'], \
        "ошибка, значения после перебора должны быть : позиция Х из каждой строки"

    assert next(it_iter) == 'x01' and next(it_iter) == 'x11' and next(it_iter) == 'x21' and \
           next(it_iter) == 'x31' and next(it_iter) == 'x41', \
        "ошибка при использовании метода next(it_iter), возвращаемые значения неккорректны"
    print("Правильный ответ ))")
