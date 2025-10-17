from traversal import BinarySearchTree
import pytest


def test_bst():
    bst = BinarySearchTree()
    assert bst.root is None

    # если использовать такой метод вставки, то получится дерево изображенное в tree_example.jpeg
    values = [10, 1, 6, 3, 2, 90, 8, -1, 5]
    for val in values:
        bst.insert_node(val)

    # Left - Node - Right, прямой проход равен отсортированному массиву
    assert bst.in_order() == sorted(values)

    # Node - Left - Right, ориентируясь на рисунок, составляем таргет ответ
    assert bst.pre_order() == [10, 1, -1, 6, 3, 2, 5, 8, 90]

    # Left - Right - Node
    assert bst.post_order() == [-1, 2, 5, 3, 8, 6, 1, 90, 10]

    # Node - Right - Left
    assert bst.reverse_pre_order() == [10, 90, 1, 6, 8, 3, 5, 2, -1]

    # Right - Node - Left, должен быть отсортирован в обратном порядке
    assert bst.reverse_in_order() == [90, 10, 8, 6, 5, 3, 2, 1, -1]
    assert bst.reverse_in_order() == sorted(values)[::-1]

    # Right - Left - Node
    assert bst.reverse_post_order() == [90, 8, 5, 2, 3, 6, -1, 1, 10]


if __name__ == "__main__":
    pytest.main()
