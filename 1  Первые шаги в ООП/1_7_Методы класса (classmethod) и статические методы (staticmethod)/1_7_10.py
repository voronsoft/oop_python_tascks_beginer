"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Y4Hvpg4FuKs

Подвиг 10 (на повторение).
Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
В этом классе должны быть реализованы следующие методы:
add_application(self, app) - добавление нового приложения app в магазин;
remove_application(self, app) - удаление приложения app из магазина;
block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
total_apps(self) - возвращает общее число приложений в магазине.

Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
Здесь Application - класс, описывающий добавляемое приложение с указанным именем.
Каждый объект класса Application должен содержать локальные свойства:

name - наименование приложения (строка);
blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).

Как хранить список приложений в объектах класса AppStore решите сами.

P.S. В программе нужно только объявить классы с указанным функционалом.
"""


# Объявите класс AppStore
# В этом классе должны быть реализованы следующие методы:
class AppStore:
    lst_object = []

    @classmethod
    def add_app_from_lst_object(cls, name):
        cls.lst_object.append(name)

    @classmethod
    def remove_app_from_lst_object(cls, name):
        x = cls.lst_object.index(name)
        del cls.lst_object[x]

    # add_application(self, app) - добавление нового приложения app в магазин;
    def add_application(self, app):
        self.add_app_from_lst_object(app)

    # remove_application(self, app) - удаление приложения app из магазина;
    def remove_application(self, app):
        self.remove_app_from_lst_object(app)

    # block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True);
    def block_application(self, app):
        app.blocked = True

    # total_apps(self) - возвращает общее число приложений в магазине.
    def total_apps(self):
        return len(self.lst_object)


# Здесь Application - класс, описывающий добавляемое приложение с указанным именем.
# Каждый объект класса Application должен содержать локальные свойства: 
# name - наименование приложения (строка);
# blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

# Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
# Как хранить список приложений в объектах класса AppStore решите сами.

# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# print(store.total_apps())
# store.block_application(app_youtube)
# store.remove_application(app_youtube)
