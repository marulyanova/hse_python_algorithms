from typing import List


def quickselect(array: List[int], k: int) -> int:
    """Поиск k-го по величине элемента массива"""

    if len(array) == 0:
        return 0

    pivot = array[len(array) // 2]

    left = [elem for elem in array if elem < pivot]
    middle = [elem for elem in array if elem == pivot]
    right = [elem for elem in array if elem > pivot]

    if k <= len(right):
        return quickselect(right, k)
    elif k <= len(right) + len(middle):
        return pivot
    else:
        return quickselect(left, k - len(right) - len(middle))
