from _1_2_1 import temp

# TEST-TASK___________________________________
try:
    assert len(temp) == 3 and 'инкапсуляция' in temp and 'полиморфизм' in temp and 'наследование' in temp
except:
    print("Пока неправильно ...")
else:
    [print(_) for _ in temp]
    print()
    print('Правильно !')
