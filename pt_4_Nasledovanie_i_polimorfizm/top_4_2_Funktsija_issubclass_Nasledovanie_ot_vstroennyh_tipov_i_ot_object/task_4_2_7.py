"""
Подвиг 7 (на повторение). Необходимо в программе объявить класс VideoItem для представления одного видео
(например, в youtube). Объекты этого класса должны создаваться командой:

video = VideoItem(title, descr, path)
где title - заголовок видео (строка);
descr - описание видео (строка);
path - путь к видео файлу.
В каждом объекте класса VideoItem должны создаваться соответствующие атрибуты: title, descr, path.

Затем, нужно создать класс для формирования оценки видео в баллах от 0 до 5.
Для этого нужно объявить еще один класс с именем VideoRating, объекты которого создаются командой:

rating = VideoRating()
В каждом объекте класса VideoRating должен быть локальный приватный атрибут с именем __rating,
содержащий целое число от 0 до 5 (по умолчанию 0).
А для записи и считывания значения из этого приватного атрибута должно быть объект-свойство (property) с именем rating.

Так как атрибут __rating - это целое число в диапазоне [0; 5],
то в момент присвоения ему какого-либо значения необходимо проверять,
что присваиваемое значение - целое число в диапазоне [0; 5]. Если это не так, то генерировать исключение командой:
raise ValueError('неверное присваиваемое значение')

Далее, в каждом объекте класса VideoItem должен быть локальный атрибут rating - объект класса VideoRating.

Пример использования классов (эти строчки в программе не писать):
v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
v.rating.rating = 6  # ValueError
P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.
"""


# ваш код:
class VideoRating:
    def __init__(self, num=0):
        self.verify(num)
        self.__rating = num

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.verify(value)
        self.__rating = value

    @staticmethod
    def verify(num):
        if 0 <= num <= 5 and type(num) is int:
            return True
        else:
            raise ValueError('неверное присваиваемое значение')


class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title  # заголовок видео (строка)
        self.descr = descr  # описание видео (строка)
        self.path = path  # путь к видео файлу
        self.rating = VideoRating()


# TEST-TASK___________________________________
from test4_2.test_4_2_7 import test_7

test_7(VideoItem, VideoRating)
# END
