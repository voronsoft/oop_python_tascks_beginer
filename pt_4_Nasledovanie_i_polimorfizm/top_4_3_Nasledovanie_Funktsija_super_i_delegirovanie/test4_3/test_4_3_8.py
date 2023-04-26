# TEST-TASK___________________________________
def test_8(SoftList):
    sl = SoftList("python")
    assert sl[0] == 'p'
    assert sl[-1] == 'n'
    assert sl[6] == False
    assert sl[-7] == False
    print("Всё получилось!")
