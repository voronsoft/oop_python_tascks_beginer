"""Испытание "Бремя наследия"
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/M_UctsRbNGA

Всевидящее око начальства увидело, что вы прошли еще одну ступень в постижении глубин ООП языка Python - наследование.
Вас вновь решили испытать и посмотреть, на что вы действительно способны. Тимлид (Teamleader) с широкой улыбкой протянул вам следующее задание.

Техническое задание
Необходимо написать универсальную основу для представления ненаправленных связных графов и поиска в них кратчайших маршрутов.
Далее, этот алгоритм предполагается применять для прокладки маршрутов: на картах, в метро и так далее.

Для универсального описания графов, вам требуется объявить в программе следующие классы:
Vertex - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
Link - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
LinkedGraph - для представления связного графа в целом (карта целиком).

Объекты класса Vertex должны создаваться командой:
v = Vertex()
и содержать локальный атрибут:
_links - список связей с другими вершинами графа (список объектов класса Link).
Также в этом классе должно быть объект-свойство (property):
links - для получения ссылки на список _links.
Объекты следующего класса Link должны создаваться командой:
link = Link(v1, v2)
где v1, v2 - объекты класса Vertex (вершины графа).
Внутри каждого объекта класса Link должны формироваться следующие локальные атрибуты:
_v1, _v2 - ссылки на объекты класса Vertex, которые соединяются данной связью;
_dist - длина связи (по умолчанию 1); это может быть длина пути, время в пути и др.

В классе Link должны быть объявлены следующие объекты-свойства:
v1 - для получения ссылки на вершину v1;
v2 - для получения ссылки на вершину v2;
dist - для изменения и считывания значения атрибута _dist.

Наконец, объекты третьего класса LinkedGraph должны создаваться командой:
map_graph = LinkedGraph()
В каждом объекте класса LinkedGraph должны формироваться локальные атрибуты:
_links - список из всех связей графа (из объектов класса Link);
_vertex - список из всех вершин графа (из объектов класса Vertex).
В самом классе LinkedGraph необходимо объявить (как минимум) следующие методы:
def add_vertex(self, v): ... - для добавления новой вершины v в список _vertex (если она там отсутствует);
def add_link(self, link): ... - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);
def find_path(self, start_v, stop_v): ... - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.
Метод find_path() должен возвращать список из вершин кратчайшего маршрута и список из связей этого же маршрута в виде кортежа:
([вершины кратчайшего пути], [связи между вершинами])
Поиск кратчайшего маршрута допустимо делать полным перебором с помощью рекурсивной функции (будем полагать, что общее число вершин в графе не превышает 100).
Для тех, кто желает испытать себя в полной мере, можно реализовать алгоритм Дейкстры поиска кратчайшего пути в связном взвешенном графе.
В методе add_link() при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex, если они там отсутствуют.
Проверку наличия связи в списке _links следует определять по вершинам этой связи. Например, если в списке имеется объект:
_links = [Link(v1, v2)]

то добавлять в него новые объекты Link(v2, v1) или Link(v1, v2) нельзя
(обратите внимание у всех трех объектов будут разные id, т.е. по id определять вхождение в список нельзя).
Подсказка: проверку на наличие существующей связи можно выполнить с использованием функции filter() и указанием нужного условия для отбора объектов.

Пример использования классов, применительно к схеме метро (эти строчки в программе писать не нужно):
map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

print(len(map_graph._links))   # 8 связей
print(len(map_graph._vertex))  # 7 вершин
path = map_graph.find_path(v1, v6)
Однако, в таком виде применять классы для схемы карты метро не очень удобно. Например, здесь нет указаний названий станций,
а также длина каждого сегмента равна 1, что не соответствует действительности.

Чтобы поправить этот момент и реализовать программу поиска кратчайшего пути в метро между двумя произвольными станциями,
объявите еще два дочерних класса:
class Station(Vertex): ... - для описания станций метро;
class LinkMetro(Link): ... - для описания связей между станциями метро.

Объекты класса Station должны создаваться командой:
st = Station(name)
где name - название станции (строка).
В каждом объекте класса Station должен дополнительно формироваться локальный атрибут:
name - название станции метро.
(Не забудьте в инициализаторе дочернего класса вызывать инициализатор базового класса).
В самом классе Station переопределите магические методы __str__() и __repr__(), чтобы они возвращали название станции метро (локальный атрибут name).

Объекты второго класса LinkMetro должны создаваться командой:
link = LinkMetro(v1, v2, dist)
где v1, v2 - вершины (станции метро);
dist - расстояние между станциями (любое положительное число).

(Также не забывайте в инициализаторе этого дочернего класса вызывать инициализатор базового класса).

В результате эти классы должны совместно работать следующим образом (эти строчки в программе писать не нужно):
map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._links))
print(len(map_metro._vertex))
path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
print(sum([x.dist for x in path[1]]))  # 7
P.S. В программе нужно объявить только классы Vertex, Link, LinkedGraph, Station, LinkMetro. На экран ничего выводить не нужно.
"""


class Vertex:
    """Для представления вершин графа"""

    def __init__(self):
        """Инициализатор класса Vertex"""
        #  список связей с другими вершинами графа (список объектов класса Link)
        self._links = list()

    @property
    def links(self):
        """Getter _links(Vertex)"""
        return self._links  # для считывания


class Link:
    """Для описания связи между двумя произвольными вершинами графа"""

    def __init__(self, v1, v2, dist=1):
        """Инициализатор класса Link"""
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    # Property
    @property
    def v1(self):
        """Getter _v1(Link)"""
        return self._v1  # для считывания

    @property
    def v2(self):
        """Getter _v2(Link)"""
        return self._v2  # для считывания

    @property
    def dist(self):
        """Getter _dist(Link)"""
        return self._dist  # для считывания

    @dist.setter
    def dist(self, value):
        """Setter _dist(Link)"""
        self._dist = value  # для записи


class LinkedGraph:
    """Для представления связного графа в целом (карта целиком)"""

    # Наконец, объекты класса LinkedGraph должны создаваться командой: map_graph = LinkedGraph()
    def __init__(self):
        """Инициализатор класса LinkedGraph"""
        # В каждом объекте класса LinkedGraph должны формироваться локальные атрибуты:
        self._links = list()  # _links - список из всех связей графа (из объектов класса Link)
        self._vertex = list()  # _vertex - список из всех вершин графа (из объектов класса Vertex)

    # В самом классе LinkedGraph необходимо объявить (как минимум) следующие методы:
    def add_vertex(self, v):
        """для добавления новой вершины v в список _vertex (если она там отсутствует)"""
        if v not in self._vertex:
            self._vertex.append(v)

    # - для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует);
    def add_link(self, link):
        """для добавления новой связи link в список _links (если объект link с указанными вершинами в списке отсутствует)"""
        # В методе add_link() при добавлении новой связи следует автоматически добавлять вершины этой связи в список _vertex, если они там отсутствуют.
        # Проверку наличия связи в списке _links следует определять по вершинам этой связи.
        # Например, если в списке имеется объект: _links = [Link(v1, v2)] то добавлять в него новые объекты Link(v2, v1) или Link(v1, v2) нельзя
        # (обратите внимание у всех трех объектов будут разные id, т.е. по id определять вхождение в список нельзя)
        # Подсказка: проверку на наличие существующей связи можно выполнить с использованием функции filter() и указанием нужного условия для отбора объектов.

        # проверка на одинаковые id вершины
        ans = tuple(filter(lambda x: id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2) or
                                     id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2), self._links))
        # если одинаковых вершин в списке _links нет, то добавляем их
        if len(ans) == 0:
            self._links.append(link)
            # добавляем вершины этой связи в список _vertex через функцию self.add_vertex(self, v)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            # добавляем связи вершин объекту класса Vertex
            link.v1.links.append(link)
            link.v2.links.append(link)

    # - для поиска кратчайшего маршрута из вершины start_v в вершину stop_v.
    def find_path(self, start_v, stop_v):
        """для поиска кратчайшего маршрута из вершины start_v в вершину stop_v"""
        # Метод find_path() должен возвращать список из вершин кратчайшего маршрута
        # и список из связей этого же маршрута
        # в виде кортежа: ([вершины кратчайшего пути], [связи между вершинами])
        # Поиск кратчайшего маршрута допустимо делать полным перебором с помощью рекурсивной функции
        # (будем полагать, что общее число вершин в графе не превышает 100).
        # Для тех, кто желает испытать себя в полной мере, можно реализовать алгоритм Дейкстры поиска кратчайшего
        # пути в связном взвешенном графе.
        self._start_v = start_v
        self._stop_v = stop_v
        return self._next(self._start_v, None, [], [])

    def _dist_path(self, links):
        return sum([x.dist for x in links if x is not None])

    def _next(self, current, link_prev, current_path, current_links):
        current_path += [current]
        if link_prev:
            current_links += [link_prev]

        if current == self._stop_v:
            return current_path, current_links

        len_path = -1
        best_path = []
        best_links = []
        for link in current.links:
            path = []
            links = []
            if link.v1 not in current_path:
                path, links = self._next(link.v1, link, current_path[:], current_links[:])
            elif link.v2 not in current_path:
                path, links = self._next(link.v2, link, current_path[:], current_links[:])

            if self._stop_v in path and (len_path > self._dist_path(links) or len_path == -1):
                len_path = self._dist_path(links)
                best_path = path[:]
                best_links = links[:]
        return best_path, best_links


# Чтобы поправить этот момент и реализовать программу поиска кратчайшего пути в метро между двумя произвольными станциями, объявите еще два дочерних класса:
# Объекты класса Station должны создаваться командой:
# st = Station(name)
# где name - название станции (строка).
# (Не забудьте в инициализаторе дочернего класса вызывать инициализатор базового класса).
# В самом классе Station переопределите магические методы __str__() и __repr__(), чтобы они возвращали название станции метро (локальный атрибут name).
class Station(Vertex):  # - для описания станций метро
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# Объекты второго класса LinkMetro должны создаваться командой:
# link = LinkMetro(v1, v2, dist)
# где v1, v2 - вершины (станции метро); dist - расстояние между станциями (любое положительное число)
# (Также не забывайте в инициализаторе этого дочернего класса вызывать инициализатор базового класса).
#
class LinkMetro(Link):  # - для описания связей между станциями метро
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)
        self._dist = dist

# My test
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
# v4 = Station("Лубянка")
# v5 = Station("Кузнецкий мост")
# v6 = Station("Китай-город 1")
# v7 = Station("Китай-город 2")
# 
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# map_metro.add_link(LinkMetro(v1, v3, 1))
# 
# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))
# 
# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))
# 
# print(len(map_metro._links))
# print(len(map_metro._vertex))
# path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
# print(path[0])    # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
# print(sum([x.dist for x in path[1]]))  # 7
#
#
#
#
#
#
#
# #TEST
# map2 = LinkedGraph()
# v1 = Vertex()
# v2 = Vertex()
# v3 = Vertex()
# v4 = Vertex()
# v5 = Vertex()
# 
# map2.add_link(Link(v1, v2))
# map2.add_link(Link(v2, v3))
# map2.add_link(Link(v2, v4))
# map2.add_link(Link(v3, v4))
# map2.add_link(Link(v4, v5))
# 
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
# 
# map2.add_link(Link(v2, v1))
# assert len(map2._links) == 5, "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"
# 
# path = map2.find_path(v1, v5)
# s = sum([x.dist for x in path[1]])
# assert s == 3, "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"
# 
# assert issubclass(Station, Vertex) and issubclass(LinkMetro, Link), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"
# 
# map2 = LinkedGraph()
# v1 = Station("1")
# v2 = Station("2")
# v3 = Station("3")
# v4 = Station("4")
# v5 = Station("5")
# 
# map2.add_link(LinkMetro(v1, v2, 1))
# map2.add_link(LinkMetro(v2, v3, 2))
# map2.add_link(LinkMetro(v2, v4, 7))
# map2.add_link(LinkMetro(v3, v4, 3))
# map2.add_link(LinkMetro(v4, v5, 1))
# 
# assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
# assert len(map2._vertex) == 5, "неверное число вершин в списке _vertex класса LinkedGraph"
# 
# path = map2.find_path(v1, v5)
# 
# assert str(path[0]) == '[1, 2, 3, 4, 5]', path[0]
# s = sum([x.dist for x in path[1]])
# assert s == 7, "неверная суммарная длина маршрута для карты метро"
