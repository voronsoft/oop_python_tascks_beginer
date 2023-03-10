"""
В чем отличие между методами класса
(объявленными через @classmethod)
и статическими методами
(объявленными через @staticmethod)?


методы класса предназначены для работы с атрибутами класса и переданными аргументами,
а статические - только с переданными им аргументами

методы класса способны обращаться и к атрибутам класса и к локальным атрибутам объекта,
из которого они были вызваны, а статические методы работают только с переданными им аргументами

статические методы предназначены для работы с локальными атрибутами объектов класса,
а методы класса не имеют такой возможности

статические методы предназначены для работы с атрибутами класса и переданными аргументами,
а методы класса - только с переданными им аргументами
"""

# ОТВЕТ !
# # методы класса предназначены для работы с атрибутами класса и переданными аргументами,
# # а статические - только с переданными им аргументами
