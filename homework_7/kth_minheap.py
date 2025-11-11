from typing import List
from makeheap import MinHeap
import heapq


def find_kth_max_minheap(nums: List[int], k: int):
    """Строим минимальную кучу, вытаскиваем элементы пока в ней не останется меньше k элементов. Последний - искомый"""

    heap = MinHeap()
    heap.makeheap(nums)

    while len(heap.arr) >= k:
        val = heap.extract_root()

    return val


def find_kth_max_minheap_auto(nums: List[int], k: int):
    heapq.heapify(nums)

    while len(nums) >= k:
        val = heapq.heappop(nums)

    return val
