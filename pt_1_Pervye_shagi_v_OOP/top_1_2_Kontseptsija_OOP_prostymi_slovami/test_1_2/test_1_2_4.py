# TEST-TASK___________________________________
def test_4(answers):
    try:
        assert len(answers) == 1 and \
               'да, например, используя парадигму структурного программирования (не включая ООП)' in answers
    except:
        print("Пока неправильно ...")
    else:
        [print(_) for _ in answers]
        print()
        print('Правильно !')