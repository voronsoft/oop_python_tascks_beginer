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
1 Значения s1.is_empty и s2.is_empty будут совпадать и принимать значение True

2 Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty примет новое значение True

3 Последняя команда изменит атрибут is_empty класса String на значение True

4 Переменная b = s2.is_empty будет ссылаться на локальный атрибут is_empty объекта s2

5 Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String

6 Последняя команда создаст локальное свойство is_empty со значением True в экземпляре s2
"""


# В программе объявлен класс:
class String:
    is_empty = False


# А, затем, создаются два его экземпляра:
s1 = String()
s2 = String()

# После этого выполняется команда:
s2.is_empty = True

print('Посмотрим теперь значения объектов')
print(f'Значение s1-{s1.is_empty}')
print(f'Значение s2-{s2.is_empty}')
print('Ответ:\n-Значение s1.is_empty будет по-прежнему False, а значение s2.is_empty примет новое значение True\n'
      '-Последняя команда создаст локальное свойство is_empty со значением True в экземпляре s2\n'
      '-Переменная a = s1.is_empty будет ссылаться на атрибут is_empty класса String\n'
      '-Переменная b = s2.is_empty будет ссылаться на локальный атрибут is_empty объекта s2')
