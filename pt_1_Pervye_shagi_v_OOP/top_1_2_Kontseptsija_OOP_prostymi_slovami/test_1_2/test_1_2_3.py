# TEST-TASK___________________________________
def test_3(answers):
    try:
        assert len(
            answers) == 2 and 'наследование позволяет как бы вынести «за скобки» общее для разных классов' in answers and \
               'на основе одного или нескольких классов создается новый (дочерний) класс' in answers
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in answers]
        print()
        print('Правильно !')
