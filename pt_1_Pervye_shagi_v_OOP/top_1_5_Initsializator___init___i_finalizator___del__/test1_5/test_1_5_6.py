# TEST-TASK___________________________________
def test_6(gr, Graph, data_graph, output):
    assert isinstance(gr, Graph) and hasattr(Graph, 'set_data') and hasattr(Graph, 'show_table') and \
           hasattr(Graph, 'show_graph') and hasattr(Graph, 'show_bar') and hasattr(Graph, 'set_show')

    assert gr.data == data_graph, "данные в объекте класса Graph и в списке data_graph отличаются"
    assert hasattr(gr, 'is_show'), "объект gr не имеет атрибута is_show"

    data = [1, 2, 3, 4]
    gr2 = Graph(data)
    gr3 = Graph(data)
    gr3.data.append(5)

    assert gr2.data != gr3.data, "локальный атрибут data должен быть уникальным (своим собственным) в каждом объекте класса Graph"

    # проверяем что выводится в консоль в проверяемом файле
    assert output == 'Столбчатая диаграмма: 8 11 10 -32 0 7 18\nОтображение данных закрыто\n'
    print(output)
    print("\nПравильный ответ !")
