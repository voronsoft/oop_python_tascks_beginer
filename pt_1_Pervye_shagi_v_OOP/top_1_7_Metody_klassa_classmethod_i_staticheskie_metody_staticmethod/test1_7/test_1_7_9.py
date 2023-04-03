# TEST-TASK___________________________________
def test_9(Video, YouTube, output_str):
    try:
        issubclass(Video, object)
    except NameError:
        print("Вы не создали класс - Video")

    try:
        issubclass(YouTube, object)
    except NameError:
        print("Вы не создали класс - YouTube")

    assert hasattr(Video, 'play'), 'Метод play не создан'
    assert hasattr(Video, 'create'), 'Метод create не создан'
    assert hasattr(YouTube, 'add_video'), 'Метод add_video не создан'
    assert hasattr(YouTube, 'play'), 'Метод play не создан'

    try:
        assert output_str == 'воспроизведение видео Python\nвоспроизведение видео Python ООП\n'
    except:
        print(f'Ваш ответ: \n{output_str}\nА нужно: ')
        print('воспроизведение видео Python\nВоспроизведение видео Python ООП\n')
        print('Попробуйте найти ошибку у себя в коде...')
    else:
        # Выведите данные из переменной
        print(output_str)
        print("Правильно !")
