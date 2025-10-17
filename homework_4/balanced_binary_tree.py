from traversal import BinarySearchTree, Node
from typing import Union


def compute_depth(root: Node, cnt: int, depth: int):
    """Вычисление глубины дерева через количество нод в левом и правом поддереве"""

    # если дальше нод нет, возвращаем текущую глубину
    if not root:
        return depth

    # к текущей глубине прибавляем 1
    cnt += 1

    # сверяем с максимальной глубиной
    depth = max(depth, cnt)

    # обновляем как max из двух поддеревьев
    depth = max(
        compute_depth(root.l_child, cnt, depth), compute_depth(root.r_child, cnt, depth)
    )

    return depth


def invoke_compute_depth(root: Union[Node, None]):
    if not root:
        return 0
    return max(compute_depth(root.r_child, 1, 1), compute_depth(root.l_child, 1, 1))


def check_balanced(root: Union[Node, None]) -> bool:
    """
    Проходит по дереву, для каждого узла высчитывает глубину левого и правого поддеревьев
    """

    if not root:
        return True

    left_depth = invoke_compute_depth(root.l_child)
    right_depth = invoke_compute_depth(root.r_child)

    if abs(left_depth - right_depth) > 1:
        return False

    if check_balanced(root.l_child) and check_balanced(root.r_child):
        return True
    else:
        return False
