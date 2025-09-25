import pytest
from typing import List
from merge_lists import (
    create_linked_list,
    merge_lists_with_fictitious,
    merge_lists_without_fictitious,
)


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
