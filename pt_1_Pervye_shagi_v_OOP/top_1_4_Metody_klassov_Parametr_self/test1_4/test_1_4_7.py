# TEST-TASK___________________________________
def test_7(data, result):
    if result is False:
        assert result is False and len(data.__dict__) == 0, "Ошибка в методе create(), не выполняются условия из задачи"
        print('Отлично !')
    else:
        assert result is True and len(data.__dict__) == 3, "Ошибка в методе create(), не выполняются условия из задачи"
        print("Отлично вы справились !")
