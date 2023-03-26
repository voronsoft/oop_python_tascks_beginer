"""Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/Xq19kCDRaag

Подвиг 7 (на повторение).
Объявите класс SmartPhone, объекты которого предполагается создавать командой:
sm = SmartPhone(марка смартфона)
Каждый объект должен содержать локальные атрибуты:
model - марка смартфона (строка);
apps - список из установленных приложений (изначально пустой).
Также в классе SmartPhone должны быть объявлены следующие методы:
add_app(self, app) - добавление нового приложения на смартфон (в конец списка apps);
remove_app(self, app) - удаление приложения по ссылке на объект app.
При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).

Каждое приложение должно определяться своим классом.
Для примера объявите следующие классы:
AppVK - класс приложения ВКонтаке;
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
app_1 = AppVK() # name = "ВКонтакте"

AppYouTube - класс приложения YouTube;
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024

AppPhone - класс приложения телефона.
Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112}) # name = "Phone", phone_list = словарь с контактами

Пример использования классов (в программе эти строчки не писать):
sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
P.S. На экран ничего выводить не нужно.
"""


# Объявите класс SmartPhone, объекты которого предполагается создавать командой:
# sm = SmartPhone(марка смартфона)
class SmartPhone:
    """Марка смартфона"""

    # Каждый объект должен содержать локальные атрибуты:
    def __init__(self, model):
        self.model = model  # марка смартфона (строка);
        self.apps = list()  # список из установленных приложений (изначально пустой).

    # Также в классе SmartPhone должны быть объявлены следующие методы:
    def add_app(self, app):
        """Добавление нового приложения на смартфон (в конец списка apps)"""
        if True not in [type(app) == type(i) for i in self.apps]:
            # При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).
            self.apps.append(app)

    def remove_app(self, app):
        """Удаление приложения по ссылке на объект app"""
        if app in self.apps:
            self.apps.remove(app)


# AppVK - класс приложения ВКонтаке;
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# app_1 = AppVK() # name = "ВКонтакте"
class AppVK():
    def __init__(self):
        self.name = 'ВКонтакте'


# AppYouTube - класс приложения YouTube;
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# app_2 = AppYouTube(1024) # name = "YouTube", memory_max = 1024
class AppYouTube():
    def __init__(self, memory_max=1024):
        self.name = 'YouTube'
        self.memory_max = memory_max


# AppPhone - класс приложения телефона.
# Объекты этих классов должны создаваться следующим образом (с соответствующим набором локальных атрибутов):
# app_3 = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
# name = "Phone"
# phone_list = словарь с контактами
class AppPhone():
    def __init__(self, phone_list):
        self.name = 'Phone'
        self.phone_list = phone_list


# ПРОВЕРКА
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)
# 
# sm.remove_app(a)

# TEST-TASK___________________________________
try:
    smart = SmartPhone("Honor 1.0")
except:
    print("шибка при создании объекта класса SmartPhone")

try:
    app_vk = AppVK()
except:
    print("шибка при создании объекта класса AppVK")

try:
    app_you_tube = AppYouTube(2048)
except:
    print("шибка при создании объекта класса AppYouTube")

try:
    app_phone = AppPhone({"Балакирев": 1234567890, "Сергей": 98450647365, "Работа": 112})
except:
    print("шибка при создании объекта класса AppPhone")

assert hasattr(smart, "model") and hasattr(smart, "apps") and hasattr(smart, "add_app") and \
       hasattr(smart, "remove_app"), "не все атрибуты и методы есть в объекте класса SmartPhone"

assert hasattr(app_vk, "name"), "не все атрибуты и методы есть в объекте класса AppVK"

assert hasattr(app_you_tube, "name") and hasattr(app_you_tube, "memory_max"), \
    "не все атрибуты и методы есть в объекте класса AppYouTube"

assert hasattr(app_phone, "name") and hasattr(app_phone, "phone_list"), \
    "не все атрибуты и методы есть в объекте класса AppYouTube"

assert type(app_phone.phone_list) is dict, "тип phone_list некорректный"

assert type(smart.model) is str, "название должно быть строкой"
assert type(smart.apps) is list, "apps должен быть списком"

smart.add_app(app_vk)
assert smart.apps[0] == app_vk, "некоректно сработал метод add_app"

smart.remove_app(app_vk)
assert len(smart.apps) == 0, "некоректно сработал метод remove_app"

# При добавлении нового приложения проверять, что оно отсутствует в списке apps (отсутствует объект соответствующего класса).
smart.add_app(app_vk)
smart.add_app(AppVK())

assert smart.apps.count(app_vk) == 1, \
    "метод add_app отработал с ошибкой в списке несколько объектов одного и того же класса"
print("Правильный ответ !!")
