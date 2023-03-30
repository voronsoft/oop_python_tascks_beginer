# TEST-TASK___________________________________
def test_5(cl, output):
    Graph = cl
    try:
        hasattr(Graph, 'set_data')
        hasattr(Graph, 'draw')
    except:
        print("Проверьте методы в классе")

    graph_1 = Graph()
    graph_1.set_data([10, -5, 100, 20, 0])
    assert 'data' in graph_1.__dict__ and graph_1.data == [10, -5, 100, 20, 0], "ошибка в методе - set_data "

    try:
        assert output == '10 0 2 5 7\n'
    except:
        print("Ошибка в методе - draw или входные данные не [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]")
        print("Пока не правильно !")
        print(f"Ваш ответ: {output}")
        print(f"Требуется: 10 0 2 5 7")
    else:
        print(output)
        print("Отлично !")
