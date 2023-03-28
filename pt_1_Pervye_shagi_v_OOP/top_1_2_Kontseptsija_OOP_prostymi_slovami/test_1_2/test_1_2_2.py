# TEST-TASK___________________________________
def test_2(answers):
    try:
        assert len(answers) == 1 and 'как шаблон, по которому конструируются объекты этого класса' in answers
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in answers]
        print()
        print('Правильно !')
