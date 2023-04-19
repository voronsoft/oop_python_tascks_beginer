"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/FWp5trS42e4

Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД.
Объекты этого класса создаются командой:
r = Record(field_name1=value1,... , field_nameN=valueN)
где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по именам полей
(field_name1,... , field_nameN) с соответствующими значениями.
Например:
r = Record(pk=1, title='Python ООП', author='Балакирев')
В объекте r появляются атрибуты:
r.pk # 1
r.title # Python ООП
r.author # Балакирев

Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:
r[0] = 2 # доступ к полю pk
r[1] = 'Супер-курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение командой:
raise IndexError('неверный индекс поля')
P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.
"""


# ваш код:
class Record:
    """Record (запись)"""

    def __init__(self, **kwargs):
        for _ in kwargs.items():
            self.__dict__.update({_[0]: _[1]})

    def __getitem__(self, item):
        """Геттер по индексу"""
        _l = len(self.__dict__)
        if isinstance(item, int) and item <= _l - 1:
            for indx, value in enumerate(self.__dict__):
                if item == indx:
                    return self.__dict__[value]
        else:
            raise IndexError('неверный индекс поля')

    def __setitem__(self, key, value):
        """Сеттер по ключу присваивает некое значение"""
        _l = len(self.__dict__)
        if isinstance(key, int) and key <= _l - 1:
            for indx, val in enumerate(self.__dict__):
                if key == indx:
                    self.__dict__[val] = value
                    break
        else:
            raise IndexError('неверный индекс поля')


# end ваш код

# TEST-TASK___________________________________
from test3_8.test_3_8_2 import test_2

test_2(Record)
# END
