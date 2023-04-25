# TEST-TASK___________________________________
def test_2(temp):
    try:
        assert len(temp) == 4 and \
               "функция issubclass(SmartPhone, IPhone) вернет False, так как SmartPhone является базовым классом для класса IPhone" in temp and \
               "функция isinstance(phone, SmartPhone) вернет True, так как объект phone связан с базовым классом SmartPhone" in temp and \
               "функция issubclass(IPhone, SmartPhone) вернет True, так как IPhone является подклассом класса SmartPhone" in temp and \
               "функция issubclass(IPhone, object) вернет True, так как все классы в Python 3.x неявно наследуются от класса object" in temp

    except:
        print("Пока неправильно попробуйте другие варианты...")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно )")
