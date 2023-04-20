Подвиг
9(на
повторение).
В
программе
объявлен
класс
и
создается
его
объект:


class Shop:
    ID_SHOP_ITEM = 0


sp = Shop()
sp.ID_SHOP_ITEM += 1
print(Shop.ID_SHOP_ITEM)

Выберите
все
верные
утверждения, связанные
с
этой
программой.
на
экране
будет
отображено
значение
0
в
строчке
sp.ID_SHOP_ITEM += 1
атрибут
ID_SHOP_ITEM
класса
Shop
увеличивается
на
1
в
строчке
sp.ID_SHOP_ITEM += 1
возникнет
ошибка, так
как
это
эквивалентно
команде
sp.ID_SHOP_ITEM = sp.ID_SHOP_ITEM + 1, а
локальный
атрибут
ID_SHOP_ITEM
отсутствует
в
объекте
sp
в
строчке
sp.ID_SHOP_ITEM += 1
создается
новая
локальная
переменная
ID_SHOP_ITEM
со
значением
1