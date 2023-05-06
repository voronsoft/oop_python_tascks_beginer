"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/rtma49Ye7hY

Подвиг 7. Объявите класс Note (нота), объекты которого создаются командой:

note = Note(name, ton)
где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си);
ton - тональность ноты (целое число).
Тональность (ton) принимает следующие целые значения:
-1 - бемоль (flat); 0 - обычная нота (normal); 1 - диез (sharp).

Если в названии (name) или тональности (ton) передаются недопустимые значения, то генерируется исключение командой:
raise ValueError('недопустимое значение аргумента')
В каждом объекте класса Note должны формироваться локальные атрибуты с именами _name и _ton с соответствующими значениями.

Объявите класс с именем Notes, в объектах которого разрешены только локальные атрибуты с именами (ограничение задается через коллекцию __slots__):
_do - ссылка на ноту до (объект класса Note);
_re - ссылка на ноту ре (объект класса Note);
_mi - ссылка на ноту ми (объект класса Note);
_fa - ссылка на ноту фа (объект класса Note);
_solt - ссылка на ноту соль (объект класса Note);
_la - ссылка на ноту ля (объект класса Note);
_si - ссылка на ноту си (объект класса Note).

Объект класса Notes должен создаваться командой:
notes = Notes()
и быть только один (одновременно в программе два и более объекта класса Notes недопустимо). Используйте для этого паттерн Singleton.

В момент создания объекта Notes должны автоматически создаваться перечисленные локальные атрибуты
и ссылаться на соответствующие объекты класса Note (тональность (ton) у всех нот изначально равна 0).

Обеспечить возможность обращения к нотам по индексам: 0 - до; 1 - ре; ... ; 6 - си.
Например:
nota = notes[2]  # ссылка на ноту ми
notes[3]._ton = -1 # изменение тональности ноты фа
Если указывается недопустимый индекс (не целое число, или число, выходящее за интервал [0; 6]), то генерируется исключение командой:
raise IndexError('недопустимый индекс')
Создайте в программе объект notes класса Notes.

P.S. В программе следует объявить только классы и создать объект notes. На экран выводить ничего не нужно.
"""


# ваш код:
class Note:
    """Нота"""

    def __init__(self, name, ton=0):
        self._name = name  # где name - название ноты (допустимые значения: до, ре, ми, фа, соль, ля, си)
        self._ton = ton  # тональность ноты (целое число) -1 - бемоль (flat); 0 - обычная нота (normal); 1 - диез (sharp).

    def verify_mane(self, val):
        if type(val) is str and val in ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']:
            return True
        else:
            raise ValueError('недопустимое значение аргумента')

    def verify_ton(self, val):
        if type(val) == int and val in [-1, 0, 1]:
            return True
        else:
            raise ValueError('недопустимое значение аргумента')

    def __setattr__(self, key, value):
        if key == '_name' and self.verify_mane(value):
            object.__setattr__(self, key, value)

        elif key == '_ton' and self.verify_ton(value):
            object.__setattr__(self, key, value)


class Notes:
    SS = None
    __slots__ = ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si']

    def __new__(cls, *args, **kwargs):
        if cls.SS is None:
            cls.SS = super().__new__(cls)
        return cls.SS

    def __init__(self):
        n_ru_name = iter(['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'])
        for i in self.__slots__:
            setattr(self, i, Note(next(n_ru_name)))

    def __getitem__(self, item):
        lst = {ind: val for ind, val in enumerate(self.__slots__)}
        if 0 <= item < len(lst):
            ans = lst[item]
            return self.__getattribute__(ans)
        else:
            raise IndexError('недопустимый индекс')


# TEST
notes = Notes()
# notes1 = Notes()
# nota = notes[2]  # ссылка на ноту ми
# notes[3]._ton = -1 # изменение тональности ноты фа
# note = Note('до', -1)

# end ваш код
# TEST-TASK___________________________________
from test4_7.test_4_7_7 import test_7

test_7(Note, Notes, notes)
# END
