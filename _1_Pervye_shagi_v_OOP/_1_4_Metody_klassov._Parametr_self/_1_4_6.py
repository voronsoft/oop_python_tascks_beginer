"""
Имеется следующий класс:
class Stepik:
    def next_task(self):
        return "Следующее задание"

И создается объект этого класса:
my_st = Stepik()

Выберите все верные варианты вызова метода next_task()
"""

# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ2']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# my_st.next_task(Stepik)
# next_task(my_st)
# next_task(Stepik)
# my_st.next_task()
# Stepik.my_st.next_task()
# Stepik.next_task(my_st)

# TEST-TASK___________________________________
try:
    assert len(temp) == 2 and "my_st.next_task()" in temp and "Stepik.next_task(my_st)" in temp
except:
    print("Неправильно, попробуйте снова")
else:
    print("Правильно !")
