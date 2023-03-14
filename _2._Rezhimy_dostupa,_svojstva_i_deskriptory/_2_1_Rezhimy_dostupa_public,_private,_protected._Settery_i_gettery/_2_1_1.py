"""
Подвиг 1. Установите соответствия между именами атрибутов классов и их режимами доступа.

self.data - приватный режим доступа (private)
self._word - защищенный режим доступа (protected)
self.__buffer - публичный режим доступа (public)
"""
# Создайте список temp с правильными ответами через запятую
# Пример temp = ['self.data - ответ', 'self.data - ответ1']
# Запустите файл на исполнение

# Вставьте правильные ответы в переменную
temp = []
# END

# TEST-TASK___________________________________
try:
    assert len(temp) == 3 and "self.data - публичный режим доступа (public)" in temp and \
           "self._word - защищенный режим доступа (protected)" in temp and \
           "self.__buffer - приватный режим доступа (private)" in temp

except:
    print("Пока неправильно попробуйте другие варианты")
else:
    [print(_) for _ in temp]
    print()
    print("Правильно !")
