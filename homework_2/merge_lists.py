import pytest
from typing import List, Tuple
from stack_vs_queue import Node


def create_linked_list(values: List[int]) -> Node | None:
    """Создает связный список из поданных значений"""

    if len(values) == 0:
        return None

    node = Node(node_value=values[0])
    iterator = node
    for i in range(1, len(values)):
        new_node = Node(node_value=values[i])
        iterator.next_node = new_node
        iterator = iterator.next_node
    return node


def prepare_output(node: Node | None) -> List[int]:
    """Создает обычный список для наглядного вывода из поданного связного списка"""

    res = []
    while node is not None and node.node_value is not None:
        res.append(node.node_value)
        node = node.next_node
    return res


def check_one_list_empty(list1: Node | None, list2: Node | None) -> List[int] | None:
    """Проверка, если заведомо один из списков пуст или оба"""

    if list1 is None and list2 is None:
        return prepare_output(None)

    if list1 is None and list2 is not None:
        return prepare_output(list2)

    if list2 is None and list1 is not None:
        return prepare_output(list1)

    return None


def merge_lists_cycle(
    res_node: Node, list1: Node, list2: Node, iterator: Node
) -> List[int]:
    """Объединение двух связных списков с сортировкой элементов"""

    def add_new_node(iterator: Node, listt: Node) -> Tuple[Node, Node]:
        iterator.next_node = Node(node_value=listt.node_value)
        iterator = iterator.next_node
        listt = listt.next_node
        return (iterator, listt)

    while True:
        if list1 is None and list2 is None:
            return prepare_output(res_node)

        elif list1 is None and list2 is not None:
            iterator, list2 = add_new_node(iterator, list2)

        elif list2 is None and list1 is not None:
            iterator, list1 = add_new_node(iterator, list1)

        elif list2.node_value < list1.node_value:
            iterator, list2 = add_new_node(iterator, list2)

        elif list2.node_value >= list1.node_value:
            iterator, list1 = add_new_node(iterator, list1)


def merge_lists_without_fictitious(list1: Node | None, list2: Node | None) -> List[int]:
    """Объединение двух связных списков в один без использования фиктивного элемента"""

    res_node = None

    # Проверка, если заведомо один из списков пуст или оба
    check = check_one_list_empty(list1, list2)
    if check is not None:
        return check

    # Инициализация первого элемента в голове
    if list1.node_value <= list2.node_value:
        res_node = Node(node_value=list1.node_value)
        list1 = list1.next_node
    else:
        res_node = Node(node_value=list2.node_value)
        list2 = list2.next_node
    iterator = res_node

    # Пока не кончатся элементы в обоих списках, добавляем в объединенный
    return merge_lists_cycle(
        res_node=res_node, list1=list1, list2=list2, iterator=iterator
    )


def merge_lists_with_fictitious(list1: Node | None, list2: Node | None) -> List[int]:
    """Объединение двух связных списков в один с использованием фиктивного элемента"""

    # Инициализация фиктивным элементом
    res_node = Node(node_value="FICTIOUS")
    iterator = res_node

    # Проверка, если заведомо один из списков пуст или оба
    check = check_one_list_empty(list1, list2)
    if check is not None:
        return check

    # Добавление первого элемента (наименьшего) из списков в голову
    if list1.node_value <= list2.node_value:
        iterator.next_node = Node(node_value=list1.node_value)
        iterator = iterator.next_node
        list1 = list1.next_node
    else:
        iterator.next_node = Node(node_value=list2.node_value)
        iterator = iterator.next_node
        list2 = list2.next_node

    # Пока не кончатся элементы в обоих списках, добавляем в объединенный
    return merge_lists_cycle(
        res_node=res_node.next_node, list1=list1, list2=list2, iterator=iterator
    )


# ------------------------------------------------------------------------------------


def do_test(func, list1: List[int], list2: List[int]) -> List[int]:
    return func(create_linked_list(list1), create_linked_list(list2))


def test_test_case_without_fictitious():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 1, 2, 3, 4, 4]


def test_custom_without_fictitious():
    list1 = []
    list2 = []
    assert do_test(merge_lists_without_fictitious, list1, list2) == []

    list1 = [1]
    list2 = []
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1]

    list1 = []
    list2 = [1]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1]

    list1 = [1]
    list2 = [1]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 1]

    list1 = [1, 3]
    list2 = [1, 2]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 1, 2, 3]

    list1 = [0, 1, 3, 10]
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [
        0,
        1,
        1,
        2,
        3,
        4,
        5,
        10,
    ]

    list1 = [3]
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 2, 3, 4, 5]

    list1 = []
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 2, 4, 5]

    list1 = [1, 2, 4, 5, 6]
    list2 = []
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 2, 4, 5, 6]

    list1 = [1, 2]
    list2 = [3, 4]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 2, 3, 4]

    list1 = [3, 4]
    list2 = [1, 2]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [1, 2, 3, 4]

    list1 = [3, 4]
    list2 = [3, 4]
    assert do_test(merge_lists_without_fictitious, list1, list2) == [3, 3, 4, 4]


def test_test_case_with_fictitious():
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 1, 2, 3, 4, 4]


def test_custom_with_fictitious():
    list1 = []
    list2 = []
    assert do_test(merge_lists_with_fictitious, list1, list2) == []

    list1 = [1]
    list2 = []
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1]

    list1 = []
    list2 = [1]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1]

    list1 = [1]
    list2 = [1]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 1]

    list1 = [1, 3]
    list2 = [1, 2]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 1, 2, 3]

    list1 = [0, 1, 3, 10]
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [
        0,
        1,
        1,
        2,
        3,
        4,
        5,
        10,
    ]

    list1 = [3]
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 2, 3, 4, 5]

    list1 = []
    list2 = [1, 2, 4, 5]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 2, 4, 5]

    list1 = [1, 2, 4, 5, 6]
    list2 = []
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 2, 4, 5, 6]

    list1 = [1, 2]
    list2 = [3, 4]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 2, 3, 4]

    list1 = [3, 4]
    list2 = [1, 2]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [1, 2, 3, 4]

    list1 = [3, 4]
    list2 = [3, 4]
    assert do_test(merge_lists_with_fictitious, list1, list2) == [3, 3, 4, 4]


if __name__ == "__main__":
    pytest.main()
