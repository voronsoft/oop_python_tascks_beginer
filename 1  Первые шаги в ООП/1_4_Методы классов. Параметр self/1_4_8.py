"""
В программе объявлен класс:
class String:
    is_empty = False

А, затем, создаются два его экземпляра:
s1 = String()
s2 = String()

После этого выполняется команда:
s2.is_empty = True

Выберите верные утверждения, связанные с этой программой.
"""
# Создайте список temp с правильными ответами через запятую
# Пример temp = ['ответ1', 'ответ2']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# Переменная b = s2.is_empty будет ссылаться на локальный атрибут is_empty объекта s2
# Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty примет новое значение True
# Последняя команда изменит атрибут is_empty класса String на значение True
# Последняя команда создаст локальное свойство is_empty со значением True в экземпляре s2
# Значения s1.is_empty и s2.is_empty будут совпадать и принимать значение True
# Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String


# TEST-TASK___________________________________
try:
    assert len(temp) == 4 and \
           "Переменная b = s2.is_empty будет ссылаться на локальный атрибут is_empty объекта s2" in temp and \
           "Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty примет новое значение True" in temp and \
           "Последняя команда создаст локальное свойство is_empty со значением True в экземпляре s2" in temp and \
           "Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String" in temp
except:
    print("Неправильно, попробуйте снова")
else:
    print("Правильно !")
