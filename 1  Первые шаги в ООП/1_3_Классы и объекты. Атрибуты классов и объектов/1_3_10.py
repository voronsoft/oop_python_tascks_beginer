"""
Объявите класс с именем Person и атрибутами:
name: 'Сергей Балакирев'
job: 'Программист'
city: 'Москва'
Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job.
Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
"""


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
# проверьте, существует ли у него локальное свойство с именем job.
print('job' in p1.__dict__)

# TEST-TASK___________________________________
try:
    issubclass(Person, object)
except NameError:
    print("Вы не создали класс - Person")

assert hasattr(Person, 'name') and hasattr(Person, 'job') and hasattr(Person, 'city'), "В классе должно быть 3 атрибута"

try:
    isinstance(p1, Person)

except NameError:
    print("Вы не создали экземпляр класса p1")

assert 'job' not in p1.__dict__, "В экземпляре класса p1 не должно быть локального свойства - job"
