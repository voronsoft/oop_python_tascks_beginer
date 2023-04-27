# TEST-TASK___________________________________
def test_7(Subject, TemperatureView, PressureView, WetView, Data, Observer):
    assert issubclass(TemperatureView, Observer), "TemperatureView должен быть подклассом Subject"
    assert issubclass(PressureView, Observer), "PressureView должен быть подклассом Subject"
    assert issubclass(WetView, Observer), "WetView должен быть подклассом Subject"

    assert TemperatureView.update != Observer.update, "вы не переопределили метод update в классе TemperatureView"
    assert PressureView.update != Observer.update, "вы не переопределили метод update в классе PressureView"
    assert WetView.update != Observer.update, "вы не переопределили метод update в классе WetView"

    try:
        subject = Subject()
        tv = TemperatureView()
        pr = PressureView()
        wet = WetView()
        #
        subject.add_observer(tv)
        subject.add_observer(pr)
        subject.add_observer(wet)
        #
        # не изменять !!
        import io
        import sys

        console_out = io.StringIO()  # Создаем буфер
        sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер

        subject.change_data(Data(23, 150, 83))
        output = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
        assert output == 'Текущая температура 23\nТекущее давление 150\nТекущая влажность 83\n'
        #
        subject.remove_observer(wet)
        console_out = io.StringIO()  # Создаем буфер
        sys.stdout = console_out  # Перенаправляем стандартный вывод (stdout) в буфер
        subject.change_data(Data(24, 148, 80))
        output1 = console_out.getvalue()  # Получаем содержимое буфера в переменную (для проверки)
        assert output1 == 'Текущая температура 24\nТекущее давление 148\n'
        sys.stdout = sys.__stdout__  # Возвращаем стандартный вывод (stdout) в нормальное состояние


    except:
        assert False, "код работает не правильно"
    else:
        assert True
        print("Всё правильно.")
