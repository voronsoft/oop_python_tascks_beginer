"""
Выберите верные способы удаления атрибута tp из класса Point.

delattr(Point, 'tp')
delattr(Point, tp)
del Point['tp']
delattr('Point', 'tp')
del Point.tp
del tp of Point
Point.tp = None
Point.tp = 0
"""

# Вставьте правильные ответы в переменную
# Пример temp = ['ответ', 'ответ' ]
temp = ["delattr(Point, 'tp')", "del Point.tp"]
# Запустите файл на исполнение для проверки

# TEST-TASK___________________________________
from test1_3.test_1_3_13 import test_13

test_13(temp)
# END
