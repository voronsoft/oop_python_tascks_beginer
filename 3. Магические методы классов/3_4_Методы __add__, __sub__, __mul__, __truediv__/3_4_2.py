"""
Подвиг 2. В программе определен следующий класс:

class Way:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        return Way(self.length + other.length)
И создаются два объекта:

w1 = Way(5)
w2 = Way(10)
Выберите все верные строчки программы при работе с объектами w1 и w2 (те, что не приводят к ошибкам во время выполнения).


    w = w1 + w2

# w = 15 + w2

    w1 += w2

# w = w1 + 10

# w = w1 + w2 + w1
"""