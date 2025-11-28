import pytest
from graph import find_connectivity_components


def check_elems_comp(elems_comp_true, elems_comp):
    return sorted(elems_comp_true) == sorted(elems_comp)


def test_empty_graph():
    data = {}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 0
    assert elems_comp == []


def test_1_vertex_graph():
    data = {1: []}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[1]], elems_comp) == True


def test_1_vertex_cycle_graph():
    data = {1: [1]}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[1]], elems_comp) == True


def test_2_vertex_graph():
    data = {1: [2, 3], 2: [], 3: []}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[1, 2, 3]], elems_comp) == True


def test_2_vertex_cycle_graph():
    data = {1: [2, 3], 2: [3, 1], 3: [1, 2]}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[1, 2, 3]], elems_comp) == True


def test_2_comp_graph():
    data = {1: [2], 2: [3, 1], 3: [2], 4: [5], 5: [4]}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 2
    assert check_elems_comp([[1, 2, 3], [4, 5]], elems_comp) == True


def test_3_comp_graph():
    data = {1: [2], 2: [3, 1], 3: [2], 4: [5], 5: [4], 6: []}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 3
    assert check_elems_comp([[1, 2, 3], [4, 5], [6]], elems_comp) == True


def test_separated_vertex_graph():
    data = {1: [], 2: [], 3: []}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 3
    assert check_elems_comp([[1], [2], [3]], elems_comp) == True


def test_separated_vertex_graph_2():
    data = {1: [], 2: [], 3: [], 4: [5, 6], 5: [4], 6: [4]}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 4
    assert check_elems_comp([[1], [2], [3], [4, 5, 6]], elems_comp) == True


def test_big_cycle_graph():
    data = {1: [2, 7], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 1]}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[i for i in range(1, 8)]], elems_comp) == True


def test_big_cycle_graph_with_duplicated_edges():
    data = {
        1: [2, 7, 1, 2],
        2: [1, 3, 5, 6],
        3: [2, 4, 3, 7],
        4: [3, 5, 3, 4, 2, 7],
        5: [4, 6, 5, 7],
        6: [5, 7, 1, 6],
        7: [6, 1],
    }
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp == 1
    assert check_elems_comp([[i for i in range(1, 8)]], elems_comp) == True


def test_incorrect_answers():
    data = {1: [2], 2: [1], 3: []}
    cnt_comp, elems_comp = find_connectivity_components(data)
    assert cnt_comp != 1
    assert cnt_comp != 0
    assert check_elems_comp([[1, 2, 3]], elems_comp) == False
    assert check_elems_comp([[2, 3], [1]], elems_comp) == False


if __name__ == "__main__":
    pytest.main()
