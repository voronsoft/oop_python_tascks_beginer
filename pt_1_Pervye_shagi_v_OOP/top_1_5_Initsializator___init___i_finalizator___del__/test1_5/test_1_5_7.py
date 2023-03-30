# TEST-TASK___________________________________
def test_7(mb, MotherBoard):
    assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, 'get_config')

    def get_config():
        mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

        return [f"Материнская плата: {mb.name}",
                f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
                f"Слотов памяти: {mb.total_mem_slots}",
                f"Память: {mem_str}"]

    res1 = ("".join(mb.get_config())).replace(" ", "")
    res2 = ("".join(get_config())).replace(" ", "")
    assert res1 == res2, "метод get_config возвратил неверные данные"
    print("Правильно !")
