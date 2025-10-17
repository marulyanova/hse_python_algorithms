from balanced_binary_tree import check_balanced, invoke_compute_depth
from traversal import BinarySearchTree, Node
import pytest


def test_compute_depth():
    bst = BinarySearchTree()
    values = [10, 1, 6, 3, 2, 90, 8, -1, 5]
    for val in values:
        bst.insert_node(val)

    assert invoke_compute_depth(bst.root) == 5

    # пустое
    bst = BinarySearchTree()
    assert invoke_compute_depth(bst.root) == 0

    # 1 элемент
    bst = BinarySearchTree()
    bst.insert_node(1)
    assert invoke_compute_depth(bst.root) == 1

    # несколько, много элементов
    root = Node(1)
    root.l_child = Node(-1)
    root.r_child = Node(2)
    assert invoke_compute_depth(root) == 2

    root.l_child.l_child = Node(-100)
    assert invoke_compute_depth(root) == 3

    root = Node(-1)
    pointer = root
    for i in range(100):
        pointer.r_child = Node(i)
        pointer = pointer.r_child
    assert invoke_compute_depth(root) == 101


def test_is_balanced_1():
    bst = BinarySearchTree()
    values = [10, 1, 6, 3, 2, 90, 8, -1, 5]
    for val in values:
        bst.insert_node(val)

    # на рисунке видно, что левое поддерево глубины 5, а правое глубины 2
    assert check_balanced(bst.root) == False


def test_is_balanced_2():

    # пустое дерево
    bst = BinarySearchTree()
    assert check_balanced(bst.root) == True

    # только корень
    bst = BinarySearchTree()
    bst.insert_node(1)
    assert check_balanced(bst.root) == True

    # корень + 1 или 2 эл-та
    bst = BinarySearchTree()
    bst.insert_node(1)
    bst.insert_node(-1)
    assert check_balanced(bst.root) == True

    bst = BinarySearchTree()
    bst.insert_node(1)
    bst.insert_node(-1)
    bst.insert_node(2)
    assert check_balanced(bst.root) == True


def test_is_balanced_3():
    root = Node(1)
    root.l_child = Node(-1)
    root.r_child = Node(2)
    assert check_balanced(root) == True

    root = Node(1)
    root.l_child = Node(-1)
    # перегрузим левое дерево
    root.l_child.l_child = Node(-100)
    assert check_balanced(root) == False

    # сбалансируем
    root.r_child = Node(10)
    assert check_balanced(root) == True
    root.l_child.r_child = Node(0)
    assert check_balanced(root) == True

    # снова перегрузим
    root.l_child.l_child.l_child = Node(1000)
    assert check_balanced(root) == False


def test_is_balanced_4():
    # большие деревья

    root = Node(0)
    pointer = root
    for i in range(1, 100):
        pointer.r_child = Node(i)
        pointer = pointer.r_child
    assert check_balanced(root) == False

    root.l_child = Node(-1)
    assert check_balanced(root) == False

    pointer = root
    for i in range(2, 100):
        pointer.l_child = Node(-i)
        pointer = pointer.l_child
    assert check_balanced(root) == False


def test_is_balanced_5():
    # создадим дерево как на картинке tree_example_2.py

    bst = BinarySearchTree()
    values = [0, -3, 3, -5, -2, 2, 5]
    for val in values:
        bst.insert_node(val)

    assert invoke_compute_depth(bst.root) == 3
    assert check_balanced(bst.root) == True


if __name__ == "__main__":
    pytest.main()
