"""
В программе объявлен следующий класс с одним методом:

class Stepik:
    def get_certificate(self):
        return False
И создается объект этого класса:

st = Stepik()
Выберите все верные варианты вызова метода get_certificate:

st.Stepik.get_certificate()
    Stepik.get_certificate(st)
get_certificate()
Stepik.get_certificate()
    st.get_certificate()
Stepik.st.get_certificate()
"""

# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 2 and "Stepik.get_certificate(st)" in temp and "st.get_certificate()" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
