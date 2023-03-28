"""
В программе объявлен следующий класс с одним методом:

class Math:
    @staticmethod
    def sqrt(x):
        return x ** 0.5
И создается объект этого класса:

m = Math()

Выберите все верные варианты вызова метода sqrt:
    res = Math.sqrt(4)
    res = m.sqrt(2)
res = Math.sqrt(m, 4)
m.Math.sqrt(3)
"""
# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 2 and "res = Math.sqrt(4)" in temp and "res = m.sqrt(2)" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
