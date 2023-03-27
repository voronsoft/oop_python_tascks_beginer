"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PJsJOIxZOdM

Подвиг 6. Ваша задача написать программу поиска слова в строке.
Задача усложняется тем, что слово должно определяться в разных его формах.
Например, слово:
программирование

может иметь следующие формы:
программирование, программированию, программированием, программировании,
программирования, программированиям, программированиями, программированиях

Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:
mw = Morph(word1, word2, ..., wordN)
где word1, word2, ..., wordN - возможные формы слова.
В классе Morph реализовать методы:
- add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
- get_words(self) - получение кортежа форм слов.
Также с объектами класса Morph должны выполняться следующие операторы сравнения:
mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
И аналогичная пара сравнений:
"word" == mw1
"word" != mw1

После создания класса Morph, формируется список dict_words из объектов этого класса, для следующих слов с их словоформами:

- связь, связи, связью, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях

Затем, прочитайте строку из входного потока командой:
text = input()
Найдите все вхождения слов из списка dict_words (используя операторы сравнения)
в строке text (без учета регистра, знаков пунктуаций и их словоформы).
Выведите на экран полученное число.

Sample Input:

Мы будем устанавливать связь завтра днем.
Sample Output:

2
"""


# здесь объявляйте класс
# TEST
class Morph:
    def __init__(self, *args):
        self.lst = list(map(lambda x: x.strip(" .,!?:;").lower(), args))

    # В классе Morph реализовать методы:
    # - add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
    def add_word(self, word):
        if word.lower() not in self.lst:
            self.lst.append(word.lower())

    # - get_words(self) - получение кортежа форм слов.
    def get_words(self):
        return tuple(self.lst)

    # Также с объектами класса Morph должны выполняться следующие операторы сравнения:
    # mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
    # mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)
    def __eq__(self, other):
        return other.lower() in self.lst

    # И аналогичная пара сравнений:
    # "word" == mw1
    # "word" != mw1


# TEST

mw = Morph('связь', 'связи', 'связью', 'связей', 'связям', 'связями', 'связях')
mw1 = Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами',
            'векторах')
mw2 = Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами',
            'эффектах')
mw3 = Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')
mw4 = Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах')

dict_words = [mw, mw1, mw2, mw3, mw4]

# Затем, прочитайте строку из входного потока командой:
text = input('')


# Найдите все вхождения слов из списка dict_words (используя операторы сравнения)
# в строке text (без учета регистра, знаков пунктуаций и их словоформы).
def search(stich):
    # удаляем всё лишнее из строки
    for i in range(1):
        # удаляем все знаки - '–?!,.;'
        for x in '–?!,.;':
            while x in stich:
                stich = stich.replace(x, '')
        # оставляем только одинарные пробелы
        for i in range(1):
            while stich[i].find('  ') > 0:
                stich[i] = stich[i].replace('  ', ' ')
    # ищем все вхождения (совпвдения слов)
    x = 0
    for i in stich.lower().split():
        for k in dict_words:
            if i in (k.lst):
                # находим (индекс) слово из списка по совпвдению
                if i == k.lst[k.lst.index(i)]:
                    x += 1
    return x


# Выведите на экран полученное число.
print(search(text))
# Sample Input:
# 
# Мы будем устанавливать связь завтра днем.
# Sample Output: 2