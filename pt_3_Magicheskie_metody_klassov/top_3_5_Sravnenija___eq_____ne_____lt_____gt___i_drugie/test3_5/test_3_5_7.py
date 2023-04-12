# TEST-TASK___________________________________
def test_7(FileAcceptor):
    acceptor = FileAcceptor('jpg', 'bmp', 'jpeg')
    assert callable(acceptor), "объект должен быть вызываемым"
    assert acceptor('filename.py') == False and acceptor('filename.bmp') == True, \
        "ошибка объект должен вернуть False или True если расширение файла разрешенно или запрещенно"

    acceptor2 = FileAcceptor("png", "bmp")
    acceptor12 = acceptor + acceptor2
    assert acceptor12('filename.jpg') is True and \
           acceptor12('filename.bmp') is True and \
           acceptor12('filename.jpeg') is True and \
           acceptor12('filename.png') is True, "при сложении 2х объектов класса FileAcceptor возникла ошибка" \
                                               "не все расширения файлов были добавлены в новый объект"

    acceptor_images = FileAcceptor("jpg", "jpeg", "png")
    acceptor_docs = FileAcceptor("txt", "doc", "xls")
    filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
                 "eq_2.xls"]
    filenames = list(filter(acceptor_images + acceptor_docs, filenames))
    assert list(filter(acceptor_images + acceptor_docs, filenames)) == ['boat.jpg', 'ans.web.png', 'text.txt',
                                                                        'www.python.doc', 'my.ava.jpg', 'forest.jpeg',
                                                                        'eq_1.png',
                                                                        'eq_2.xls'], "Пока неправильно, прочтите внимательно задание"
    print("Умница, вы справились с задачей !!")
