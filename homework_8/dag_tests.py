import pytest
from dag import topological_sort


def test_empty():
    data = {}
    assert topological_sort(data) == []


def test_with_cycle():
    data = {1: [2], 2: [3], 3: [1]}
    result = topological_sort(data)
    assert sorted(result) == [1, 2, 3]

    data = {1: [2], 2: [3], 3: [4], 4: [5], 5: [6], 6: [7], 7: [1]}
    result = topological_sort(data)
    assert sorted(result) == [1, 2, 3, 4, 5, 6, 7]

    data = {1: [4], 10: [3], 5: [2], 2: [1], 4: [5], 3: [7]}
    result = topological_sort(data)
    assert sorted(result) == [1, 2, 4, 5]


def test_1_vertex():
    data = {1: []}
    assert topological_sort(data) == [1]


def test_2_separated_vertex():
    data = {1: [], 2: []}
    assert topological_sort(data) == [1, 2]


def test_2_vertex():
    data = {1: [], 2: [1]}
    assert topological_sort(data) == [2, 1]

    data = {1: [2], 2: []}
    assert topological_sort(data) == [1, 2]


def test_3_vertex():
    data = {3: [], 1: [3], 2: [3], 5: [2]}
    assert topological_sort(data) == [1, 5, 2, 3]

    data = {3: [], 1: [3], 2: [3], 5: [2, 1, 3]}
    top_sort = topological_sort(data)
    assert (top_sort == [5, 1, 2, 3]) or (top_sort == [5, 2, 1, 3])


def test_big_graph():

    # граф изображен на graph.png

    data = {
        7: [11, 8],
        11: [2, 9],
        5: [11],
        3: [8, 10],
        8: [9],
        10: [],
        2: [],
        9: [],
    }

    top_sort = topological_sort(data)

    assert (top_sort == [7, 5, 11, 2, 3, 8, 10, 9]) or (
        top_sort == [7, 5, 3, 11, 8, 10, 2, 9]
    )

    # граф изображен на image.png

    data = {5: [2, 0], 4: [0, 1], 0: [], 2: [3], 3: [1], 1: []}
    top_sort = topological_sort(data)
    assert top_sort == [5, 4, 2, 0, 3, 1]


if __name__ == "__main__":
    pytest.main()
