import sys
import os

sys.path.append(os.path.dirname(__file__))

from traversal import BinarySearchTree, Node
from typing import Union


def compute_depth(root: Node) -> int:
    """Вычисление глубины дерева через количество нод в левом и правом поддереве"""

    # если дальше нод нет, возвращаем текущую глубину
    if root is None:
        return 0

    # обновляем как max из двух поддеревьев + 1
    left_depth = compute_depth(root.l_child)
    right_depth = compute_depth(root.r_child)
    return 1 + max(left_depth, right_depth)


def invoke_compute_depth(root: Union[Node, None]) -> int:
    if root is None:
        return 0
    return compute_depth(root)


def find_highest_disbalance(root: Union[Node, None]) -> Union[Node, None]:
    """
    Проходит по дереву, для каждого узла высчитывает глубину левого и правого поддеревьев,
    возвращает самую ближайшую к корну вершину, у левого и правого поддеревьев которой разница в глубинах больше 1.
    Используется для AVL-дерева, поиск места для ребалансировки
    """

    if root is None:
        return None

    left_depth = invoke_compute_depth(root.l_child)
    right_depth = invoke_compute_depth(root.r_child)

    if abs(left_depth - right_depth) > 1:
        return root

    left_disbalance = find_highest_disbalance(root.l_child)
    if left_disbalance:
        return left_disbalance
    return find_highest_disbalance(root.r_child)


def check_balanced(root: Union[Node, None]) -> bool:
    """
    Проходит по дереву, для каждого узла высчитывает глубину левого и правого поддеревьев
    """

    if root is None:
        return True

    left_depth = invoke_compute_depth(root.l_child)
    right_depth = invoke_compute_depth(root.r_child)

    if abs(left_depth - right_depth) > 1:
        return False

    return check_balanced(root.l_child) and check_balanced(root.r_child)
