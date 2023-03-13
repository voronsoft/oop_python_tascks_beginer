"""
В программе объявлен следующий класс с одним методом:

class Loader:
    @classmethod
    def json_parse(cls):
        return ""
И создается объект этого класса:

ld = Loader()

Выберите все верные варианты вызова метода json_parse:
ld.json_parse(Loader)
Loader.json_parse(ld)
    ld.json_parse()
    res = ld.json_parse()
    Loader.json_parse()
    res = Loader.json_parse()
"""

# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 4 and "ld.json_parse()" in temp and "res = ld.json_parse()" in temp and \
           "Loader.json_parse()" in temp and "res = Loader.json_parse()" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
