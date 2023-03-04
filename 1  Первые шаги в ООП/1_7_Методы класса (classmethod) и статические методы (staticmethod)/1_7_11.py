"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/38QoBSpQqnM

Подвиг 11 (на повторение).
Объявите класс для мессенджера с именем Viber.
В этом классе должны быть следующие методы:

add_message(msg) - добавление нового сообщения в список сообщений;
remove_message(msg) - удаление сообщения из списка;
set_like(msg) - поставить/убрать лайк для сообщения msg
(т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
show_last_message(число) - отображение последних сообщений;
total_messages() - возвращает общее число сообщений.

Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)

Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:
text - текст сообщения (строка);
fl_like - поставлен или не поставлен лайк у сообщения
(булево значение True - если лайк есть и False - в противном случае, изначально False);

P.S. Как хранить список сообщений, решите самостоятельно.
"""


class Viber:
    list_message = []

    # В этом классе должны быть следующие методы:
    # add_message(msg) - добавление нового сообщения в список сообщений;
    @staticmethod
    def add_message(msg):
        Viber.list_message.append(msg)

    # remove_message(msg) - удаление сообщения из списка;
    @staticmethod
    def remove_message(msg):
        del Viber.list_message[Viber.list_message.index(msg)]

    # set_like(msg) - поставить/убрать лайк для сообщения msg
    # (т.е. изменить атрибут fl_like объекта msg: если лайка нет то он ставится, если уже есть, то убирается);
    @staticmethod
    def set_like(msg):
        ind = Viber.list_message.index(msg)
        if msg.fl_like:
            Viber.list_message[ind].fl_like = False
        else:
            Viber.list_message[ind].fl_like = True

    # show_last_message(число) - отображение последних сообщений;
    @staticmethod
    def show_last_message(num_msg):
        [print(i.text, end=" : ") for i in Viber.list_message[int('-' + str(num_msg)):]]

    # total_messages() - возвращает общее число сообщений.
    @staticmethod
    def total_messages():
        return len(Viber.list_message)


# Класс Message(необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором локальных свойств:
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения
# (булево значение True - если лайк есть и False - в противном случае, изначально False);
class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
# msg = Message("Всем привет!", True)
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Viber.show_last_message(3)
# qq = Viber.total_messages()

# P.S. Как хранить список сообщений, решите самостоятельно.
