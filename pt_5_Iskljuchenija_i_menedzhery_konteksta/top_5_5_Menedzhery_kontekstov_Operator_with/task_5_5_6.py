"""
Подвиг 6 (на повторение). Имеется следующий фрагмент программы:

class PrinterError(Exception):
    #Класс общих ошибок принтера
    pass


class PrinterConnectionError(PrinterError):
    #Ошибка соединения с принтером
    pass


class PrinterPageError(PrinterError):
    #Ошибка отсутствия бумаги в принтере
    pass


try:
    raise PrinterConnectionError('соединение с принтером отсутствует')
except (PrinterConnectionError, PrinterPageError) as e:
    print(e)
except PrinterError as e:
    print(e)

Выберите все верные утверждения, связанные с этой программой.


блок except с двумя классами PrinterConnectionError и PrinterPageError записывать нельзя, возникнет ошибка
    при возникновении исключений PrinterConnectionError или PrinterPageError выполнение программы перейдет в блок except с этими двумя классами
    при выполнении программы на экране будет отображена строка "соединение с принтером отсутствует"
последний блок except с классом PrinterError никогда выполнен не будет ни при каких типах исключений
"""
