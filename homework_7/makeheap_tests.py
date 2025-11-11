import pytest
from makeheap import MinHeap
import heapq


def check_heap_property(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


def test_minheap_n_log_n():
    heap = MinHeap()
    values = [5, -100, 20, 100, 90, 34, 1, 7]
    heap.makeheap_n_log_n(values)

    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)

    heap = MinHeap()
    values = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    heap.makeheap_n_log_n(values)

    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)

    heap = MinHeap()
    values = [3, 2, 1, 5, 6, 4]
    heap.makeheap_n_log_n(values)
    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)


def test_minheap_n():
    heap = MinHeap()
    values = [5, -100, 20, 100, 90, 34, 1, 7]
    heap.makeheap(values)

    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)

    heap = MinHeap()
    values = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    heap.makeheap(values)

    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)

    heap = MinHeap()
    values = [3, 2, 1, 5, 6, 4]
    heap.makeheap(values)
    heap_target = heapq.nsmallest(len(values), values)

    assert check_heap_property(heap.arr) == True
    assert heap.arr[0] == heap_target[0]
    assert heap.arr[0] == min(values)

    while heap.arr:
        assert heap.extract_root() == heap_target.pop(0)


if __name__ == "__main__":
    pytest.main()
