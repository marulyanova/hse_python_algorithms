from typing import List
import time
import sys
import os
import random

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from homework_5.tracer import trace_recursion


def calc_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время исполнения: {round((end - start) * 1000, 4)} ms")
        return result

    return wrapper


def merge(left: List[int], right: List[int]) -> List[int]:
    """Объединение двух массивов путём сравнения i-го и j-го элементов"""

    sorted_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    if i == len(left):
        sorted_arr += right[j:]
    else:
        sorted_arr += left[i:]

    return sorted_arr


# @trace_recursion
def mergesort_recursive(array: List[int]):
    """Разбиваем текущий массив на два по центральному элементу и рекурсивно сортируем две половины"""

    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergesort_recursive(array[:mid])
    right = mergesort_recursive(array[mid:])
    return merge(left, right)


@calc_execution_time
def invoke_mergesort_recursive(array: List[int]):
    return mergesort_recursive(array)


# @trace_recursion
def quicksort_recursive(array: List[int]):
    """Выбираем опорный элемент, делим массив на элементы меньше опорного, равные и больше опорного"""

    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [elem for elem in array if elem < pivot]
    middle = [elem for elem in array if elem == pivot]
    right = [elem for elem in array if elem > pivot]
    return quicksort_recursive(left) + middle + quicksort_recursive(right)


@calc_execution_time
def invoke_quicksort_recursive(array: List[int]):
    return quicksort_recursive(array)


if __name__ == "__main__":
    """Посмотрим краевые случаи для сравнения времени работы алгоритмов"""

    # Случайный массив
    print("Случайный массив:")
    array = [random.randint(-1000, 1000) for _ in range(1000)]
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Полностью отсортированный массив
    print("Полностью отсортированный массив:")
    array = [i for i in range(1000)]
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Обратно отсортированный массив
    print("Обратно отсортированный массив:")
    array = array[::-1]
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Массив с одинаковыми элементами
    print("Массив с одинаковыми элементами:")
    array = [1] * 1000
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Почти отсортированный массив
    print("Почти отсортированный массив:")
    array = [i for i in range(1000)]
    for _ in range(10):
        idx1 = random.randint(0, 99)
        idx2 = random.randint(0, 99)
        array[idx1], array[idx2] = array[idx2], array[idx1]
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Одна половина массива - одно значения, другая - другое
    print("Одна половина массива - одно значения, другая - другое:")
    array = [0] * 500 + [1] * 500
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    # Одна половина массива - одно значения, другая - другое. В обратном порядке
    print("Одна половина массива - одно значения, другая - другое:")
    array = [1] * 500 + [0] * 500
    invoke_mergesort_recursive(array)
    invoke_quicksort_recursive(array)
    print()

    """
    При запуске можно увидеть, что время работы алгоритмов примерно одинаково,
    кроме случая с почти отсортированным массивом, где quicksort работает быстрее mergesort ~ в 10 раз.

    Если сравнивать время исполнения не одного алгоритма с другим, а каждый алгоритм с самим собой на разных данных, то можно увидеть, 
    что mergesort работает примерно за одно и то же время на всех данных.
    quicksort работает быстрее в ~10 раз на массиве с одинаковыми элементами (потому что все элементы равны опорному и не происходит рекурсивного деления)
    В случае <Одна половина массива - одно значения, другая - другое> quicksort работает быстрее по той же причине, тк происходит минимальное количество рекурсивных вызовов.
    """
