В
программе
описаны
два
класса
следующим
образом:


class SmartPhone:
    pass


class IPhone(SmartPhone):
    pass


И
создается
объект
второго
класса:

phone = IPhone()
Выберите
все
верные
утверждения, связанные
с
этой
программой.

функция
issubclass(SmartPhone, IPhone)
вернет
False, так
как
SmartPhone
является
базовым
классом
для
класса
IPhone
функция
isinstance(phone, SmartPhone)
вернет
True, так
как
объект
phone
связан
с
базовым
классом
SmartPhone
функция
issubclass(IPhone, SmartPhone)
вернет
True, так
как
IPhone
является
подклассом
класса
SmartPhone
функция
issubclass(IPhone, object)
вернет
True, так
как
все
классы
в
Python
3.
x
неявно
наследуются
от
класса
object
функция
issubclass(phone, SmartPhone)
вернет
True, так
как
объект
phone
связан
с
базовым
классом
SmartPhone
функция
issubclass(SmartPhone, IPhone)
вернет
True, так
как
SmartPhone
связан
с
дочерним
классом
IPhone
