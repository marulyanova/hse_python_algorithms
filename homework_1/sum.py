import pytest
from typing import List


# O(N)
def max_even_sum(nums: List[int]) -> int:
    """Finds max even sum of list elems
    Iterates through list, collect sum, find the minimum odd number.
    If result sum is odd => res -= min_odd
    """

    res = 0
    min_odd = max(nums)

    for num in nums:
        if num % 2 == 1:
            min_odd = min(min_odd, num)
        res += num

    if res % 2 == 1:
        res -= min_odd

    return res


def test_test_cases():
    assert max_even_sum([5, 7, 13, 2, 14]) == 36
    assert max_even_sum([3]) == 0


def test_one_elem():
    assert max_even_sum([9]) == 0
    assert max_even_sum([2]) == 2
    assert max_even_sum([112]) == 112


def test_several_elem():
    assert max_even_sum([9, 1]) == 10
    assert max_even_sum([9, 1, 3]) == 12
    assert max_even_sum([9, 1, 3, 5]) == 18
    assert max_even_sum([9, 1, 3, 5]) == 18
    assert max_even_sum([2, 4, 6, 8, 10]) == 30
    assert max_even_sum([3, 7, 9]) == 16
    assert max_even_sum([3, 7, 9, 1]) == 20
    assert max_even_sum([112, 1]) == 112
    assert max_even_sum([112, 113]) == 112
    assert max_even_sum([112, 1, 2]) == 114


if __name__ == "__main__":
    pytest.main()
