import pytest
from kth import quickselect


def test_example_cases():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert quickselect(nums, k) == 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert quickselect(nums, k) == 4


def test_corner_cases():
    nums = []
    k = 1
    assert quickselect(nums, k) == 0

    nums = [1]
    k = 1
    assert quickselect(nums, k) == 1

    nums = [1, 1, 1, 1]
    k = 2
    assert quickselect(nums, k) == 1
    k = 3
    assert quickselect(nums, k) == 1

    nums = [5, 4, 3, 2, 1, 0]
    k = 1
    assert quickselect(nums, k) == 5
    k = 6
    assert quickselect(nums, k) == 0


def test_random_cases():
    nums = [1, -1, 10, 12, -10, 15]
    k = 1
    assert quickselect(nums, k) == 15
    k = 3
    assert quickselect(nums, k) == 10
    k = 6
    assert quickselect(nums, k) == -10

    nums = [-1, -1000, -20, -15, 13, 1, 200]
    k = 2
    assert quickselect(nums, k) == 13
    k = 7
    assert quickselect(nums, k) == -1000

    nums = [i for i in range(1000)]
    k = 500
    assert quickselect(nums, k) == 500
    k = 1000
    assert quickselect(nums, k) == 0
    k = 1
    assert quickselect(nums, k) == 999


if __name__ == "__main__":
    pytest.main()
