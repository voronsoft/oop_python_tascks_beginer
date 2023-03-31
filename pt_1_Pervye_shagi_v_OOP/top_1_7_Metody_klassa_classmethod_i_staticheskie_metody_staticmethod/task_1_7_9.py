"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/YkDq9p8n17A

Подвиг 9.
Объявите в программе класс Video.
С двумя методами:
- create(self, name) - для задания имени name текущего видео
    (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
- play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").

Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):
- add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
- play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).
(здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
videos - для хранения добавленных объектов класса Video (изначально список пуст).
Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем,
вызывать метод play() класса Video.

Методы add_video и play вызывайте напрямую из класса YouTube.
Создавать экземпляр этого класса не нужно.

Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП".
После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите
(с помощью метода play класса YouTube) сначала первое, а затем, второе видео.
"""
# код не менять !!!
import io
import sys

# Создаю объект StringIO
output = io.StringIO()
# Перенаправляю стандартный вывод в StringIO
sys.stdout = output


# END !!!

# Объявите в программе класс Video.
class Video:
    def __init__(self, name):
        self.name = self.create(name)

    # С двумя методами:
    # - create(self, name) - для задания имени name текущего видео
    # (метод сохраняет имя name в локальном атрибуте name объекта класса Video);
    def create(self, name):
        return name

    # - play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
    def play(self):
        print(f'воспроизведение видео {self.name}')


# Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):
# - add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
# - play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).
class YouTube:
    # videos - для хранения добавленных объектов класса Video (изначально список пуст).
    videos = []

    @classmethod
    # - add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
    def add_video(cls, video):
        cls.videos.append(video)

    # Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем,
    # вызывать метод play() класса Video.
    @classmethod
    def play(cls, video_indx=0):
        return Video.play(cls.videos[video_indx])


# Методы add_video и play вызывайте напрямую из класса YouTube.
# Создавать экземпляр этого класса не нужно.
# 
# Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП".
# После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите
# (с помощью метода play класса YouTube) сначала первое, а затем, второе видео.
v1 = Video('Python')
v2 = Video('Python ООП')
YouTube.add_video(v1)
YouTube.add_video(v2)

[YouTube.play(i) for i in range(len(YouTube.videos))]

# TEST-TASK___________________________________
# Получите данные из StringIO
output_str = output.getvalue()
# Верните стандартный вывод
sys.stdout = sys.__stdout__
from test1_7.test_1_7_9 import test_9

test_9(Video, YouTube, output_str)

# END
