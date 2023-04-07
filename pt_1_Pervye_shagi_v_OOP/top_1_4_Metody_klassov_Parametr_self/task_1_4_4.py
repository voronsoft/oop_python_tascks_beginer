"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/AbMOpQSt1fA

Подвиг 4. Объявите класс с именем MediaPlayer с двумя методами:
open(file) - для открытия медиа-файла с именем file
(создает локальное свойство filename со значением аргумента file в объекте класса MediaPlayer)

play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")

Создайте два экземпляра этого класса с именами: media1 и media2.
Вызовите из них метод open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2.
После этого вызовите через объекты метод play(). При этом, на экране должно отобразиться две строки (без кавычек):

"Воспроизведение filemedia1"
"Воспроизведение filemedia2"
"""
# не изменять !!
import io
import sys

console_out = io.StringIO()  # Создаем буфер
sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер


# end


# ваш код:
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print("Воспроизведение", self.filename)


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()
# end ваш код

# TEST-TASK___________________________________
from test1_4.test_1_4_4 import test_4  # импортируем функцию для проверки

output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние
test_4(MediaPlayer, output)  # проверяем класс и то что будет выведено в консоль
