# TEST-TASK___________________________________
def test_4(Car):
    auto = Car()
    assert '_Car__model' in auto.__dict__, 'В объекте класса нет приватного атрибута __model'
    auto.model = 'Toyota'
    assert auto.model == 'Toyota', 'Некорректно работает записать данных в __model'
    assert auto._Car__model == "Toyota", 'Некоректно работает считывание значения с защищенного приватного свойства'
    assert len(auto.__dict__) == 1, 'Объект класса должен содержать всего один защищённый атрибут'
    print("Правильный ответ")
