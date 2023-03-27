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
# код не менять !!!
import io
import sys

# Создаю объект StringIO
output = io.StringIO()
# Перенаправляю стандартный вывод в StringIO
sys.stdout = output


# END !!!

# Тут напишите ваше решение:
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

# TEST-TASK___________________________________
# Получите данные из StringIO
output_str = output.getvalue()
# Верните стандартный вывод
sys.stdout = sys.__stdout__

try:
    assert output_str == 'Воспроизведение filemedia1\nВоспроизведение filemedia2\n'
except:
    print(f'Ваш ответ: \n{output_str}\nА нужно: ')
    print('Воспроизведение filemedia1\nВоспроизведение filemedia2\n')
    print('Попробуйте найти ошибку у себя в коде...')
else:
    # Выведите данные из переменной
    print(output_str)
    print("Правильно !")
