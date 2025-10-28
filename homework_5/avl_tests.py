import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from avl import AVL
from homework_4.balanced_binary_tree import invoke_compute_depth
import pytest


def test_emply_tree():
    avl_tree = AVL()

    assert avl_tree.is_balanced() is True
    assert avl_tree.pre_order() == []
    assert avl_tree.root is None
    assert invoke_compute_depth(avl_tree.root) == 0


def test_add_root():
    avl_tree = AVL()
    avl_tree.insert_node(10)

    assert avl_tree.is_balanced() is True
    assert avl_tree.pre_order() == [10]
    assert avl_tree.root.val == 10
    assert invoke_compute_depth(avl_tree.root) == 1


def test_avl_insert():
    avl_tree = AVL()
    values_to_insert = [30, 20, 40, 10, 25, 50, 5]

    for value in values_to_insert:
        avl_tree.insert_node(value)

    assert avl_tree.is_balanced() is True
    assert avl_tree.in_order() == [5, 10, 20, 25, 30, 40, 50]
    assert invoke_compute_depth(avl_tree.root) == 4
    assert invoke_compute_depth(avl_tree.root.l_child) == 3
    assert invoke_compute_depth(avl_tree.root.r_child) == 2
    assert invoke_compute_depth(avl_tree.root.l_child.l_child) == 2
    assert invoke_compute_depth(avl_tree.root.l_child.r_child) == 1


def test_avl_search():
    avl_tree = AVL()
    values_to_insert = [10, 20, 30, 40, 50, 25]

    for value in values_to_insert:
        avl_tree.insert_node(value)

    for value in values_to_insert:
        assert avl_tree.search(value) is True

    values_to_delete = [10, 20, 30]
    for value in values_to_delete:
        avl_tree.delete_node(value)

    for value in values_to_delete:
        assert avl_tree.search(value) is False

    remaining_values = set(values_to_insert) - set(values_to_delete)
    for value in remaining_values:
        assert avl_tree.search(value) is True

    assert avl_tree.is_balanced() is True


def test_avl_balancing():
    avl_tree = AVL()
    for i in range(1, 100):
        avl_tree.insert_node(i)
        assert avl_tree.is_balanced() is True

    for i in range(1, 100):
        avl_tree.delete_node(i)
        assert avl_tree.is_balanced() is True


if __name__ == "__main__":
    pytest.main()
