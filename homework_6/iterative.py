from typing import List
from compare import merge


def mergesort_iterative(array: List[int]):
    """
    Сначала проходим по массиву, объединяя соседние элементы в отсортированные пары,
    затем объединяем отсортированные пары в отсортированные четверки и тд
    """

    i = 1
    while i < len(array):
        j = 0
        while j < len(array):
            left = array[j : j + i]
            right = array[j + i : j + 2 * i]
            array[j : j + len(right) + len(left)] = merge(left, right)
            j += 2 * i
        i *= 2
    return array


def quicksort_iterative(array: List[int]):
    """
    Используем стек для хранения начального и конечного индексов подмассивов для сортировки,
    Выбираем опорный как центральный,
    делим массив на элементы меньше опорного, равные и больше опорного, меняем элементы на месте
    Далее сортируем следующие получившиеся подмассивы
    """

    if len(array) <= 1:
        return array

    stack = [(0, len(array) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = array[(start + end) // 2]
        l, r = start, end

        while l <= r:
            while array[l] < pivot:
                l += 1
            while array[r] > pivot:
                r -= 1
            if l <= r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1

        stack.append((start, r))
        stack.append((l, end))

    return array
