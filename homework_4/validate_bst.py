from traversal import Node
from typing import Union

"""
Условия бинарного дерева поиска:
1) Все узлы левого поддерева любого узла содержат значения меньшие, чем значение самого узла.
2) Все узлы правого поддерева любого узла содержат значения большие (или равные, в зависимости от реализации), чем значение самого узла.
3) Оба поддерева (левое и правое) также являются бинарными деревьями поиска.
"""


def check_node(node: Node, value: int, how: Union["upper", "lower"]) -> bool:
    """
    Итеративно проверяет, больше/меньше ли указанное значение всех значений в переданном дереве.
    Если встретили неподходящий элемент, сразу возвращаем False и не проверяем последующие
    """

    if not node:
        return True

    # Проверяем значение текущей ноды
    if how == "upper":
        if value < node.val:
            return False
    elif how == "lower":
        if value > node.val:
            return False
    else:
        raise ValueError(f"Incorrect type of comparison: {how}")

    # Если все ок, проверяем поддеревья
    if check_node(node.l_child, value, how) and check_node(node.r_child, value, how):
        return True
    else:
        return False


def validate_bst(root: Node) -> bool:

    if not root:
        return True

    if root.l_child:

        # Проверка, что в левом поддереве только меньшие
        if not check_node(root.l_child, root.val, "upper"):
            return False

        # Проверка, что левое поддерево тоже BST
        if not validate_bst(root.l_child):
            return False

    if root.r_child:

        # Проверка, что в правом поддереве только большие
        if not check_node(root.r_child, root.val, "lower"):
            return False

        # Проверка, что правое поддерево тоже BST
        if not validate_bst(root.r_child):
            return False

    return True
