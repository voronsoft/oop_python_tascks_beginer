# TEST-TASK___________________________________
def test_8(DecisionTree, TreeObj):
    assert hasattr(DecisionTree, 'add_obj') and hasattr(DecisionTree, 'predict'), \
        "в классе DecisionTree должны быть методы add_obj и predict"

    assert type(TreeObj.left) == property and type(TreeObj.right) == property, \
        "в классе TreeObj должны быть объекты-свойства left и right"

    root = DecisionTree.add_obj(TreeObj(0))
    v_11 = DecisionTree.add_obj(TreeObj(1), root)
    v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
    DecisionTree.add_obj(TreeObj(-1, "программист"), v_11)
    DecisionTree.add_obj(TreeObj(-1, "кодер"), v_11, False)
    DecisionTree.add_obj(TreeObj(-1, "посмотрим"), v_12)
    DecisionTree.add_obj(TreeObj(-1, "нет"), v_12, False)

    assert DecisionTree.predict(root, [1, 1, 0]) == 'программист', "неверный вывод решающего дерева"
    assert DecisionTree.predict(root, [0, 1, 0]) == 'нет', "неверный вывод решающего дерева"
    assert DecisionTree.predict(root, [0, 1, 1]) == 'посмотрим', "неверный вывод решающего дерева"
    print("Правильный ответ !")
