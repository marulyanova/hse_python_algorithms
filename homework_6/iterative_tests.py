import pytest
from iterative import mergesort_iterative, quicksort_iterative


def test_mergesort_correctness():
    array = [0, -100, -200, 80, 345, 125, -1, 5]
    assert mergesort_iterative(array) == sorted(array)

    array = [i for i in range(100)]
    assert mergesort_iterative(array) == sorted(array)

    array = array[::-1]
    assert mergesort_iterative(array) == sorted(array)

    array = []
    assert mergesort_iterative(array) == sorted(array)

    array = [1]
    assert mergesort_iterative(array) == sorted(array)

    array = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert mergesort_iterative(array) == sorted(array)

    array = [1, 0, 1, 0, 1, 0, 1, 0]
    assert mergesort_iterative(array) == sorted(array)


def test_quicksort_correctness():
    array = [0, -100, -200, 80, 345, 125, -1, 5]
    assert quicksort_iterative(array) == sorted(array)

    array = [i for i in range(100)]
    assert quicksort_iterative(array) == sorted(array)

    array = array[::-1]
    assert quicksort_iterative(array) == sorted(array)

    array = []
    assert quicksort_iterative(array) == sorted(array)

    array = [1]
    assert quicksort_iterative(array) == sorted(array)

    array = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert quicksort_iterative(array) == sorted(array)

    array = [1, 0, 1, 0, 1, 0, 1, 0]
    assert quicksort_iterative(array) == sorted(array)


if __name__ == "__main__":
    pytest.main()
