# TEST-TASK___________________________________
def test_6(TriangleListIterator):
    lst = [['x00', 'x00', 'x00', 'x00'],
           ['x10', 'x11', 'x12', 'x13'],
           ['x20', 'x21', 'x22', 'x23'],
           ['x30', 'x31', 'x32', 'x33'],
           ['x40', 'x41', 'x42', 'x43', 'x45', 'x46']
           ]
    it = TriangleListIterator(lst)
    temp = []
    for _ in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
        temp.append(_)

    assert temp == ['x00',
                    'x10', 'x11',
                    'x20', 'x21', 'x22',
                    'x30', 'x31', 'x32', 'x33',
                    'x40', 'x41', 'x42', 'x43', 'x45'], "некорректно отработал перебор методом треугольника"

    lst1 = [['x00'],
            ['x10', 'x11'],
            ['x20', 'x21', 'x22']]
    it1 = TriangleListIterator(lst1)
    temp1 = []
    for _ in it1:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
        temp1.append(_)

    assert temp1 == ['x00',
                     'x10', 'x11',
                     'x20', 'x21', 'x22'], "некорректно отработал перебор методом треугольника"

    it_iter = iter(it1)
    assert next(it_iter) == 'x00' and next(it_iter) == 'x10' and next(it_iter) == 'x11', \
        "ошибка, при переборе методом next(iter) должно возвращаться новое значение" \
        "а так же значения должны возвращаться по условию задачи"

    lst2 = [['x00'],
            ['x10', ],
            ['x20', 'x21', 'x22']]
    it2 = TriangleListIterator(lst2)
    temp2 = []
    try:
        for _ in it2:
            temp2.append(_)
    except IndexError:
        assert True
    else:
        assert False, "ошибка, не сгенерировалась ошибка IndexError при входе неравномерного списка из-за структуры списка"
    print("Правильный ответ !!!")
