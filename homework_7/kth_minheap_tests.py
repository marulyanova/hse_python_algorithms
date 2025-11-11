from kth_minheap import find_kth_max_minheap, find_kth_max_minheap_auto
import pytest


def test_example_cases():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert find_kth_max_minheap(nums, k) == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_max_minheap(nums, k) == 4


def test_example_cases_auto():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert find_kth_max_minheap_auto(nums, k) == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_max_minheap_auto(nums, k) == 4


def test_corner_cases():
    nums = [1]
    k = 1
    assert find_kth_max_minheap(nums, k) == 1


def test_corner_cases_auto():
    nums = [1]
    k = 1
    assert find_kth_max_minheap_auto(nums, k) == 1


def test_cases():
    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 1
    assert find_kth_max_minheap(nums, k) == 30

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 2
    assert find_kth_max_minheap(nums, k) == 10

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 7
    assert find_kth_max_minheap(nums, k) == -2

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 6
    assert find_kth_max_minheap(nums, k) == -1


def test_cases_auto():
    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 6
    assert find_kth_max_minheap_auto(nums, k) == -1

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 7
    assert find_kth_max_minheap_auto(nums, k) == -2

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 2
    assert find_kth_max_minheap_auto(nums, k) == 10

    nums = [3, 4, -1, -2, 10, 8, 30]
    k = 1
    assert find_kth_max_minheap_auto(nums, k) == 30


def test_reversed_cases():
    nums = [i for i in range(100)][::-1]
    k = 50
    assert find_kth_max_minheap(nums, k) == 50

    nums = [i for i in range(100)][::-1]
    k = 50
    assert find_kth_max_minheap_auto(nums, k) == 50


if __name__ == "__main__":
    pytest.main()
