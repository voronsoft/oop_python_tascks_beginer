"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/QtOqF78VlHM

Подвиг 7 (познание срезов). Объявите в программе класс с именем RadiusVector (радиус-вектор), объекты которого создаются командой:

v = RadiusVector(x1, x2,..., xN)
где x1, x2,..., xN - координаты радиус-вектора (числа: целые или вещественные).
В каждом объекте класса RadiusVector должен быть локальный атрибут:
- coords - список из координат радиус-вектора.
Для доступа к отдельным координатам, реализовать следующий функционал:
coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
v[i] = value # изменение i-й координаты
v[start:stop] = [val_1, val_2, ...] # изменение сразу нескольких координат
v[start:stop:step] = [val_1, val_2, ...] # изменение сразу нескольких координат

Пример использования класса (эти строчки в программе не писать):
v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
v[0] = 10.5
P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится объектом класса slice.
Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций (списков, кортежей и т.п.).
"""


class RadiusVector:
    def __init__(self, *args):
        if all(type(_) in (int, float) for _ in args):
            self.coords = list(args)

    # Для доступа к отдельным координатам, реализовать следующий функционал:
    def __getitem__(self, item):
        """Доступ к координатам"""
        # coord = v[i] # получение значения i-й координаты (целое число, отсчет с нуля)
        if isinstance(item, int) and 0 <= item < len(self.coords):
            return self.coords[item]

        # coords_1 = v[start:stop] # получение среза (набора) координат в виде кортежа
        # coords_2 = v[start:stop:step] # получение среза (набора) координат в виде кортежа
        elif isinstance(item, slice):
            return tuple(self.coords[item])

    def __setitem__(self, key, value):
        """Запись координат"""
        self.coords[key] = value

# # TEST
# # Пример использования класса (эти строчки в программе не писать):
# v = RadiusVector(1, 1, 1, 1, 1)
# print(v[1])  # 1
# print(v[0:2])
# v[:] = 1, 2, 3, 4
# print(v[2])  # 3
# print(v[1:])  # (2, 3, 4)
# v[0] = 10.5