# TEST-TASK___________________________________
def test_8(CountryInterface, ABC, Country):
    assert issubclass(CountryInterface, ABC), "CountryInterface должен быть унаследован от ABC"
    assert issubclass(Country, CountryInterface), "класс Country должен быть дочерним классом класса CountryInterface"

    # Model.get_pk.__isabstractmethod__
    assert CountryInterface.name.__isabstractmethod__, "в классе CountryInterface свойство name должен быть абстрактным"
    assert CountryInterface.population.__isabstractmethod__, \
        "в классе CountryInterface свойство population должен быть абстрактным"
    assert CountryInterface.square.__isabstractmethod__, "в классе CountryInterface свойство square быть абстрактным"
    assert CountryInterface.get_info.__isabstractmethod__, \
        "в классе CountryInterface метод get_info должен быть абстрактным"

    assert isinstance(Country.name, property), "объект свойство name не найден"
    assert isinstance(Country.population, property), "объект свойство population не найден"
    assert isinstance(Country.square, property), "объект свойство square не найден"

    country = Country("Крокозия", 140000000, 324005489.55)
    assert "_Country__name" in country.__dict__, "__name не найден"
    assert "_Country__population" in country.__dict__, "__population не найден"
    assert "_Country__square" in country.__dict__, "__square  не найден"
    assert "get_info" in dir(country) and callable(country.get_info), "метод get_info не найден"
    assert country.get_info() == 'Крокозия: 324005489.55, 140000000', "метод get_info работает не корректно"

    assert country.name == "Крокозия", "при считывании значения __name произошла ошибка"

    assert country.population == 140000000, "при считывании значения __population произошла ошибка"
    country.population = 14
    assert country.population == 14, "при записи значения __population произошла ошибка"

    assert country.square == 324005489.55, "при считывании значения __square произошла ошибка"
    country.square = 0.55
    assert country.square == 0.55, "при записи значения __square произошла ошибка"

    print("Отлично!!")
