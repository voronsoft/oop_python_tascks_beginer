"""
Имеется следующий класс:
class Stepik:
    def next_task(self):
        return "Следующее задание"

И создается объект этого класса:
my_st = Stepik()

Выберите все верные варианты вызова метода next_task()

1 - my_st.next_task(Stepik)

2 - next_task(my_st)

3 - next_task(Stepik)

4 - my_st.next_task()

5 - Stepik.my_st.next_task()

6 - Stepik.next_task(my_st)
"""


# Имеется следующий класс:
class Stepik:
    def next_task(self):
        return "Следующее задание"


# И создается объект этого класса:
my_st = Stepik()
# Выберите все верные варианты вызова метода next_task()
my_st.next_task()
Stepik.next_task(my_st)
