import sys
import os
import random
from typing import List

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from homework_6.compare import calc_execution_time


class MinHeap:
    def __init__(self):
        self.arr = []

    def insert(self, val: int):
        self.arr.append(val)  # добавляем новый элемент в конец массива
        ind_elem = len(self.arr) - 1
        ind_parent = (ind_elem - 1) // 2

        # начинаем поднимать элемент вверх, сравнивая с родителем
        while (
            ind_elem >= 0
            and ind_parent >= 0
            and self.arr[ind_parent] > self.arr[ind_elem]
        ):
            self.swap_elems(ind_parent, ind_elem)
            ind_elem = ind_parent
            ind_parent = (ind_elem - 1) // 2

    @calc_execution_time
    def makeheap_n_log_n(self, arr: List[int]):
        """Построение кучи, каждый элемент добавляется через insert в конец и поднимается вверх"""

        for val in arr:
            self.insert(val)

    def swap_elems(self, ind_1: int, ind_2: int):
        buf = self.arr[ind_1]
        self.arr[ind_1] = self.arr[ind_2]
        self.arr[ind_2] = buf

    def sift_down(self, i: int):
        """Просеивание эл-та с индексом i вниз"""

        n = len(self.arr)

        while True:
            new_ind = i
            ind_child_left = 2 * i + 1
            ind_child_right = 2 * i + 2

            if ind_child_left < n and self.arr[ind_child_left] < self.arr[new_ind]:
                new_ind = ind_child_left
            if ind_child_right < n and self.arr[ind_child_right] < self.arr[new_ind]:
                new_ind = ind_child_right

            if new_ind == i:
                break
            self.swap_elems(i, new_ind)
            i = new_ind

    @calc_execution_time
    def makeheap(self, arr: List[int]):
        """
        Построение кучи путем просеивания эл-ов вниз начиная с конца (снизу кучи)
        Пропускаем листья, начинаем с самого нижнего родителя
        """

        self.arr = arr
        for i in range((len(arr) - 1) // 2, -1, -1):
            self.sift_down(i)

    def extract_root(self):
        """Забирает корень, ставит на место корня последний элемент в куче, просеивает его"""

        root = self.arr[0]

        self.arr[0] = self.arr[-1]
        self.arr.pop()

        self.sift_down(0)

        return root


def compare_time(values, comment=""):
    print(comment)
    print("O (N log N)")
    heap = MinHeap()
    heap.makeheap_n_log_n(values)

    print("O (N)")
    heap = MinHeap()
    heap.makeheap(values)


if __name__ == "__main__":

    """
    При запуске можно увидеть, что второй вариант heap.makeheap через просеивание вниз на любом тест-примере
    Исполняется быстрее чем heap.makeheap_n_log_n через поднятие вверх.

    Наибольшая разница во времени на обратном отсортированном массиве.
    """

    compare_time([i for i in range(100000)], "Отсортированный массив")
    print()

    compare_time([i for i in range(100000)][::-1], "Обратный отсортированный массив")
    print()

    compare_time([random.randint(0, 1000) for _ in range(10000)], "Случайный массив")
    print()

    compare_time([random.randint(0, 10000) for _ in range(1000000)], "Случайный массив")
    print()

    almost_sorted = [i for i in range(100000)]
    for _ in range(50):
        ind_1 = random.randint(0, 99999)
        ind_2 = random.randint(0, 99999)
        buf = almost_sorted[ind_1]
        almost_sorted[ind_1] = almost_sorted[ind_2]
        almost_sorted[ind_2] = buf
    compare_time(almost_sorted, "Почти отсортированный массив")
    print()
