# TEST-TASK___________________________________
def test_4(cl, output):
    MediaPlayer = cl

    assert hasattr(MediaPlayer, "open"), "не объявлен метод - open"
    assert hasattr(MediaPlayer, "play"), "не объявлен метод - play"

    x = MediaPlayer()
    assert len(x.__dict__) == 0

    x.open("filemedia1")
    assert "filename" in x.__dict__ and x.filename == "filemedia1", "некоректно отработал метод - open"

    # проверяем что выводится в консоль в проверяемом файле

    assert output == 'Воспроизведение filemedia1\nВоспроизведение filemedia2\n', \
        f"Ошибка должно получиться :\nВоспроизведение filemedia1\nВоспроизведение filemedia2\n" \
        f"\nВаш ответ:\n{output}"

    print(output)
    print("Правильно !")
