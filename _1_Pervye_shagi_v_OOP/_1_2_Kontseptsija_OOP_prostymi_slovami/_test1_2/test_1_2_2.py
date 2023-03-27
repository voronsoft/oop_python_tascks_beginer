from _1_2_2 import temp
# TEST-TASK___________________________________
try:
    assert len(temp) == 1 and 'как шаблон, по которому конструируются объекты этого класса' in temp
except:
    print("Пока неправильно ...")
else:
    [print(_) for _ in temp]
    print()
    print('Правильно !')