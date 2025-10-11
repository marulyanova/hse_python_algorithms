import pytest
from two_sum import two_sum


def test_provided_cases():
    # данные в задании примеры
    assert two_sum([1, 3, 4, 10], 7) == (1, 2)
    assert two_sum([5, 5, 1, 4], 10) == (0, 1)


def test_other_cases():
    assert two_sum([1, 2, 3, 4, 5], 9) == (3, 4)
    assert two_sum([1, 2, 3, 4, 5], 8) == (2, 4)
    assert two_sum([1, 2, 3, 4, 5], 7) == (2, 3)
    assert two_sum([1, 2, 3, 4, 5], 4) == (0, 2)
    assert two_sum([1, 2, 3, 4, 5], 3) == (0, 1)

    assert two_sum([7, 3], 10) == (0, 1)
    assert two_sum([3, 7], 10) == (0, 1)
    assert two_sum([5, 5], 10) == (0, 1)

    assert two_sum([8, 2, 3, 1, 0, 9], 1) == (3, 4)
    assert two_sum([8, 2, 3, 1, 0, 9], 4) == (2, 3)
    assert two_sum([8, 2, 3, 1, 0, 9], 2) == (1, 4)

    assert two_sum([10, 6, 2, 8, 3], 13) == (0, 4)
    assert two_sum([10, 6, 2, 8, 3], 11) == (3, 4)
    assert two_sum([10, 6, 2, 8, 3], 9) == (1, 4)

    assert two_sum([-1, 0, -2, 10, -11, 3], -1) == (0, 1)
    assert two_sum([-1, 0, -2, 10, -11, 3], -3) == (0, 2)
    assert two_sum([-1, 0, -2, 10, -11, 3], -12) == (0, 4)
    assert two_sum([-1, 0, -2, 10, -11, 3], 1) == (2, 5)
    assert two_sum([-1, 0, -2, 10, -11, 3], 8) == (2, 3)

    assert two_sum([-3, -1, -2, 0, 7, 9, 0], 0) == (3, 6)
    assert two_sum([-3, -1, -2, 0, 7, 9, 0], -5) == (0, 2)


if __name__ == "__main__":
    pytest.main()
