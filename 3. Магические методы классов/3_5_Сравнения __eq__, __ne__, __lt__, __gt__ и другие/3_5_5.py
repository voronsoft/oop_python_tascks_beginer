"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/k7PSxUf0w6g

Подвиг 5. Имеется стихотворение, представленное следующим списком строк:

stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова
и разбить строку по словам (слова разделяются одним или несколькими пробелами).
На основе полученного списка слов, создать объект класса StringText командой:
st = StringText(lst_words)
где lst_words - список из слов одной строчки стихотворения.

С объектами класса StringText должны быть реализованы операторы сравнения:
st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2

Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text.
Затем, сформировать новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов.
Для сортировки использовать стандартную функцию sorted() языка Python.
После этого преобразовать данный список (lst_text_sorted)
в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).
P.S. На экран в программе ничего выводить не нужно.
"""


# здесь продолжайте программу
# st = StringText(lst_words)
# где lst_words - список из слов одной строчки стихотворения.
class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words  # где lst_words - список из слов одной строчки стихотворения.

    # -------------
    # С объектами класса StringText должны быть реализованы операторы сравнения:
    # st1 > st2   # True, если число слов в st1 больше, чем в st2 -     __gt__(self, other)
    def __gt__(self, other):
        return len(self.lst_words) > len(other.lst_words)

    # # st1 < st2   # True, если число слов в st1 меньше, чем в st2 -     __lt__(self, other)
    # def __lt__(self, other):
    #     return len(self.lst_words) < len(other.lst_words)

    # st1 >= st2  # True, если число слов в st1 больше или равно st2 -  __ge__(self, other)
    def __ge__(self, other):
        return len(self.lst_words) >= len(other.lst_words)

    # # st1 <= st2  # True, если число слов в st1 меньше или равно st2 -  __le__(self, other)
    # def __le__(self, other):
    #     return len(self.lst_words) <= len(other.lst_words)

    # len()
    def __len__(self):
        return len(self.lst_words)

    # -------------


# TEST
# эти строчки не менять
stich = ["Я к вам пишу – чего же боле?",
         "Что я могу еще сказать?",
         "Теперь, я знаю, в вашей воле",
         "Меня презреньем наказать.",
         "Но вы, к моей несчастной доле",
         "Хоть каплю жалости храня,",
         "Вы не оставите меня."]
# Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" в начале и в конце каждого слова
for i in range(len(stich)):
    # удаляем все знаки - '–?!,.;'
    for x in '–?!,.;':
        while x in stich[i]:
            stich[i] = stich[i].replace(x, '')
    # оставляем только одинарные пробелы
    for i in range(len(stich)):
        while stich[i].find('  ') > 0:
            stich[i] = stich[i].replace('  ', ' ')

# Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text.
lst_text = [StringText(i.split()) for i in stich]

# Затем, сформировать новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов.
# Для сортировки использовать стандартную функцию sorted() языка Python.
lst_text_sorted = sorted(lst_text, key=len, reverse=True)

# После этого преобразовать данный список (lst_text_sorted)
# в список из строк (объекты заменяются на соответствующие строки, между словами ставится пробел).
lst_text_sorted = [' '.join(i.lst_words) for i in lst_text_sorted]
# P.S. На экран в программе ничего выводить не нужно.
