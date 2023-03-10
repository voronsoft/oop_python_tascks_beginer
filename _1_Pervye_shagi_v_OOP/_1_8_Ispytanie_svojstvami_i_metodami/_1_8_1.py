"""
Испытание свойствами и методами
Видео-разбор (решение смотреть только после своей попытки): https://youtu.be/26pwwOu_-d0

Представьте, что вы получили задание от заказчика.
Вас просят реализовать простую имитацию локальной сети, состоящую из набора серверов,
соединенных между собой через роутер.

Каждый сервер может отправлять пакет любому другому серверу сети.
Для этого у каждого есть свой уникальный IP-адрес.
Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов.
Алгоритм следующий. Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3.
Для этого, он сначала отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу)

Для реализации этой схемы программе предлагается объявить три класса:
-Server - для описания работы серверов в сети;
-Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
-Data - для описания пакета информации.

-Server.-
Серверы будут создаваться командой:
sv = Server()
Уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра класса Server.
Далее, роутер должен создаваться аналогичной командой:
router = Router()
А, пакеты данных, командой:
data = Data(строка с данными, IP-адрес назначения)

-Router-
Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:
-link(server) - для присоединения сервера server (объекта класса Server) к роутеру
    (для простоты, каждый сервер соединен только с одним роутером);
-unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
-send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
    (после отправки буфер должен очищаться).
И одно обязательное локальное свойство (могут быть и другие свойства):
-buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

Класс Server должен содержать свой набор методов:
-send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
(пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
-get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
и очищает входной буфер;
-get_ip() - возвращает свой IP-адрес.
Соответственно в объектах класса Server должны быть локальные свойства:
-buffer - список принятых пакетов (объекты класса Data, изначально пустой);
-ip - IP-адрес текущего сервера.

-Data-
Наконец, объекты класса Data должны содержать два следующих локальных свойства:
data - передаваемые данные (строка);
ip - IP-адрес назначения.
"""


# -Router-
# Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:
# -link(server) - для присоединения сервера server (объекта класса Server) к роутеру
#     (для простоты, каждый сервер соединен только с одним роутером);
# -unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
# -send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
#     (после отправки буфер должен очищаться).
# И одно обязательное локальное свойство (могут быть и другие свойства):
# -buffer - список для хранения принятых от серверов пакетов (объектов класса Data).

class Router:
    # И одно обязательное локальное свойство (могут быть и другие свойства):
    # -buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    def __init__(self, connect={}):
        self.buffer = list()
        self.connect_router_server = connect

    # -link(server) - для присоединения сервера server (объекта класса Server) к роутеру
    #     (для простоты, каждый сервер соединен только с одним роутером);
    # router.link(sv_from)
    def link(self, server):
        self.connect_router_server.update({server.ip: server})
        server.connect_router_server = self

    # -unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
    # router.unlink(sv_from)
    def unlink(self, server):
        del self.connect_router_server[server.ip]
        server.connect_router_server = None

    # -send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
    #     (после отправки буфер должен очищаться).
    # router.send_data()
    def send_data(self):
        for i in self.buffer:
            if i.ip in self.connect_router_server:
                self.connect_router_server[i.ip].buffer.append(i)
        #             else:
        #                 print(f'ОШИБКА !!!\nСервер: ip-{i.ip}, не соеденен с роутером. Передача пакета данных отменена !!!')
        self.buffer.clear()


class Server:
    num_server = 0

    # Соответственно в объектах класса Server должны быть локальные свойства:
    # -buffer - список принятых пакетов (объекты класса Data, изначально пустой);
    # -ip - IP-адрес текущего сервера.
    def __init__(self):
        self.buffer = list()
        self.ip = self.gen_ip_server()
        self.connect_router_server = None

    @classmethod
    def gen_ip_server(cls):
        cls.num_server += 1
        return cls.num_server

    # send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
    # (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
    # sv_from.send_data(Data("Hello", sv_to.get_ip()))
    def send_data(self, data):
        if (self.connect_router_server != None) and (self.ip in router.connect_router_server):
            # router.buffer.append((data.ip, data.data))
            router.buffer.append(data)

    # get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
    # и очищает входной буфер;
    # msg_lst_from = sv_from.get_data()
    def get_data(self):
        data = self.buffer[:]
        self.buffer.clear()
        return data

    # -get_ip() - возвращает свой IP-адрес.
    def get_ip(self):
        return self.ip


# Наконец, объекты класса Data должны содержать два следующих локальных свойства:
# data - передаваемые данные (строка);
# ip - IP-адрес назначения.
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


# Пример использования этих классов (эти строчки в программе писать не нужно):
router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
# # router.unlink(sv_from)
# # router.unlink(sv_from2)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
#
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
#
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
# Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ).
# Что-либо выводить на экран не нужно.


# # TEST
# assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
# assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"
# 
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
# 
# assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
# assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"
# 
# assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
# 
# assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
# 
# assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"
# 
# router.unlink(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# router.send_data()
# msg_lst_to = sv_to.get_data()
# assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"
