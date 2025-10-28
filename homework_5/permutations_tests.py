import pytest
from permutations import permutations
import itertools


def target_permutations(nums):
    """
    itertools по умолчанию генерирует все перестановки, включая дубликаты,
    поэтому дополнительно убираем дубликаты с помощью сета
    """
    permutations = sorted(list(map(list, itertools.permutations(nums))))
    permutations_unique = set()
    for perm in permutations:
        permutations_unique.add(tuple(perm))
    return sorted([list(perm) for perm in permutations_unique])


def test_permutations_example():
    nums = [1, 2, 3]
    assert sorted(permutations(nums)) == sorted(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    nums = [0, 1]
    assert sorted(permutations(nums)) == sorted([[0, 1], [1, 0]])

    assert permutations([1]) == [[1]]


def test_permutations_other():
    # пустой список
    assert permutations([]) == []

    assert sorted(permutations([1, 2, 3, 4])) == target_permutations([1, 2, 3, 4])

    assert sorted(permutations([1, 2, 3])) != target_permutations([1, 2, 2])


def test_permutations_random_lists():
    assert sorted(permutations([5, 6, 7, -1, 9, 0])) == target_permutations(
        [5, 6, 7, -1, 9, 0]
    )

    assert sorted(permutations([10, 20, 30, 40, 50])) == target_permutations(
        [10, 20, 30, 40, 50]
    )

    assert sorted(permutations([3, 3, 3, 4])) == target_permutations([3, 3, 3, 4])

    assert sorted(permutations([0, 0, 0, 0])) == target_permutations([0, 0, 0, 0])


if __name__ == "__main__":
    pytest.main()
