from validate_bst import validate_bst
from traversal import BinarySearchTree, Node
import pytest


def test_validate_bst_1():
    # дерево из предыдущей задачи
    bst = BinarySearchTree()

    values = [10, 1, 6, 3, 2, 90, 8, -1, 5]
    for val in values:
        bst.insert_node(val)

    assert validate_bst(bst.root) == True


def test_validate_bst_2():
    # краевые случаи

    # пустое дерево
    bst = BinarySearchTree()
    assert validate_bst(bst.root) == True

    # только корень
    bst = BinarySearchTree()
    bst.insert_node(1)
    assert validate_bst(bst.root) == True

    # корень + 1 или 2 эл-та
    bst = BinarySearchTree()
    bst.insert_node(1)
    bst.insert_node(-1)
    assert validate_bst(bst.root) == True

    bst = BinarySearchTree()
    bst.insert_node(1)
    bst.insert_node(-1)
    bst.insert_node(2)
    assert validate_bst(bst.root) == True


def test_validate_bst_3():
    # напишем свой root без использования уже реализованной вставки

    root = Node(1)
    root.l_child = Node(-1)
    root.r_child = Node(2)
    assert validate_bst(root) == True

    # добавим неправильных элементов
    root.l_child.l_child = Node(100)
    assert validate_bst(root) == False
    root.l_child.r_child = Node(100)
    assert validate_bst(root) == False

    # обратно правильные
    root.l_child.l_child = Node(-20)
    root.l_child.r_child = Node(0)
    assert validate_bst(root) == True


def test_validate_bst_4():
    # напишем свой root без использования уже реализованной вставки

    root = Node(1)
    root.l_child = Node(10)
    assert validate_bst(root) == False

    root.l_child = Node(-1)
    root.r_child = Node(-1)
    assert validate_bst(root) == False


def test_validate_bst_5():
    # большие деревья

    root = Node(-1)
    pointer = root
    for i in range(100):
        pointer.r_child = Node(i)
        pointer = pointer.r_child
    assert validate_bst(root) == True

    root.l_child = Node(100)
    assert validate_bst(root) == False

    root.l_child = Node(-100)
    assert validate_bst(root) == True

    pointer = root
    for i in range(2, 100):
        pointer.l_child = Node(-i)
        pointer = pointer.l_child
    assert validate_bst(root) == True


if __name__ == "__main__":
    pytest.main()
