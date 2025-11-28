import pytest
from dijkstra import dijkstra


def test_empty_graph():
    data = []
    assert dijkstra(0, data) == []


def test_1_vertex_graph():
    data = [[0]]
    assert dijkstra(0, data) == [0]
    assert dijkstra(1, data) is None


def test_2_separated_vertex_graph():
    data = [[0, -1], [-1, 0]]
    assert dijkstra(0, data) == [0, float("inf")]
    assert dijkstra(1, data) == [float("inf"), 0]


def test_2_vertex_graph():
    data = [[0, 5], [5, 0]]
    assert dijkstra(0, data) == [0, 5]
    assert dijkstra(1, data) == [5, 0]


def test_3_vertex_graph():
    data = [[0, 3, 1], [3, 0, 1], [1, 1, 0]]
    assert dijkstra(0, data) == [0, 2, 1]
    assert dijkstra(1, data) == [2, 0, 1]
    assert dijkstra(2, data) == [1, 1, 0]


def test_big_graph():

    # объяснение изображено на img.png

    data = [
        [0, 2, -1, 10, 4],
        [2, 0, 1, -1, -1],
        [-1, 1, 0, -1, 7],
        [10, -1, -1, 0, 3],
        [4, -1, 7, 3, 0],
    ]

    assert dijkstra(0, data) == [0, 2, 3, 7, 4]
    assert dijkstra(1, data) == [2, 0, 1, 9, 6]
    assert dijkstra(2, data) == [3, 1, 0, 10, 7]
    assert dijkstra(3, data) == [7, 9, 10, 0, 3]
    assert dijkstra(4, data) == [4, 6, 7, 3, 0]


if __name__ == "__main__":
    pytest.main()
