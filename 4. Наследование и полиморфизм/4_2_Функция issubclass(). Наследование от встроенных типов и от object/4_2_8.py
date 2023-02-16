# # Подвиг 8. Отметьте все верные определения для функций isinstance() и issubclass().
#
# функция issubclass(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2 но не его базовых классов
# функция issubclass(obj, cls) возвращает True, если объект obj является объектом класса cls или какого-либо его базовых классов
# 		функция isinstance(obj, cls) возвращает True, если объект obj является объектом класса cls
# функция isinstance(obj, cls) возвращает True, если объект obj является объектом класса cls но не его базовых классов
# функция isinstance(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2 или какого-либо его базовых классов
# 		функция issubclass(cls1, cls2) возвращает True, если класс cls1 является подклассом класса cls2

# class Geom:
#     pass

class cls2():
    pass

class cls1(cls2):
    pass

obj = cls1()
x = isinstance(obj, cls1)
x1 = issubclass(cls1, object)