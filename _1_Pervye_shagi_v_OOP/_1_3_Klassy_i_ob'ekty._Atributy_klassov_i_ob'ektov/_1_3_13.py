"""
Выберите верные способы удаления атрибута tp из класса Point.
"""

#   delattr(Point, 'tp')
# delattr(Point, tp)
# del Point['tp']
# delattr('Point', 'tp')
#   del Point.tp
# del tp of Point
# Point.tp = None
# Point.tp = 0

# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 2 and "delattr(Point, 'tp')" in temp and "del Point.tp" in temp
except:
    print("Пока неправильно....")
else:
    print("Правильно !!")
