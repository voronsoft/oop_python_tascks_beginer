Подвиг
2.
Метод
__exit__
имеет
следующую
сигнатуру:


def __exit__(self, exc_type, exc_val, exc_tb):
    ...


За
что
отвечают
параметры
exc_type, exc_val, exc_tb
этого
метода?

exc_type
тип
возникшего
исключения(None, если
не
произошло)
exc_val
объект
класса
возникшего
исключения(None, если
не
произошло)
exc_tb
трассировка
стека
возникшего
исключения(None, если
не
произошло)