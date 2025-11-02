import pytest
from compare import invoke_mergesort_recursive, invoke_quicksort_recursive


def test_mergesort_correctness():
    array = [0, -100, -200, 80, 345, 125, -1, 5]
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = [i for i in range(100)]
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = array[::-1]
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = []
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = [1]
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert invoke_mergesort_recursive(array) == sorted(array)

    array = [1, 0, 1, 0, 1, 0, 1, 0]
    assert invoke_mergesort_recursive(array) == sorted(array)


def test_quicksort_correctness():
    array = [0, -100, -200, 80, 345, 125, -1, 5]
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = [i for i in range(100)]
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = array[::-1]
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = []
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = [1]
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert invoke_quicksort_recursive(array) == sorted(array)

    array = [1, 0, 1, 0, 1, 0, 1, 0]
    assert invoke_quicksort_recursive(array) == sorted(array)


if __name__ == "__main__":
    pytest.main()
