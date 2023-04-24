"""
Подвиг 2. В программе объявлены два класса следующим образом:

class Table:
    def __init__(self, model, color):
        self.model = model
        self.color = color


class RoundTable(Table):
    def __init__(self, model, color, radius, height):
        super().__init__(model, color)
        self.radius = radius
        self.height = height
И создается объект класса RoundTable:

rt = RoundTable('PC', 'brown', 500, 750)
Выберите все верные утверждения, связанные с этим фрагментом программы.

    класс RoundTable наследуется от класса Table
параметры self в инициализаторе класса RoundTable и в инициализаторе класса Table ссылаются на разные объекты
    в созданном объекте rt формируются четыре локальных свойства: model, color, radius, height
при создании объекта rt вызывается сначала инициализатор класса Table, а затем, - класса RoundTable
    параметры self в инициализаторе класса RoundTable и в инициализаторе класса Table ссылаются на один и тот же объект rt
класс Table наследуется от класса RoundTable
    при создании объекта rt вызывается сначала инициализатор класса RoundTable, а затем, - класса Table
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = [""]
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test4_1.test_4_1_2 import test_2

test_2(temp)
# END
