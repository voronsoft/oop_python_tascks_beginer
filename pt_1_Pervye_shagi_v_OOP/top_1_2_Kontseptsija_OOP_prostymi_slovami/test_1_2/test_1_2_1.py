# TEST-TASK___________________________________
def test_1(answers):
    try:
        assert len(
            answers) == 3 and 'инкапсуляция' in answers and 'полиморфизм' in answers and 'наследование' in answers
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in answers]
        print()
        print('Правильно !')
