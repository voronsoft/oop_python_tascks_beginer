# TEST-TASK___________________________________
def test_1(temp):
    try:
        assert len(temp) == 3 and "self.data - публичный режим доступа (public)" in temp and \
               "self._word - защищенный режим доступа (protected)" in temp and \
               "self.__buffer - приватный режим доступа (private)" in temp

    except:
        print("Пока неправильно попробуйте другие варианты.")
    else:
        [print(_) for _ in temp]
        print()
        print("Правильно !")
