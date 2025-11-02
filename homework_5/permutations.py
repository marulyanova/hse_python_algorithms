from typing import List, Set
from tracer import trace_recursion


def permutations(nums: List[int]) -> List[List[int]]:

    global result
    result = set()

    @trace_recursion
    def generate_premutations_recursive(n: int, arr: List[int], used_idx: Set):
        """
        Если количество элементов в текущей перестановке достигло максимального, добавляем в результат
        Если не достигло, смотрим, какие элементы (индексы) еще не включены в перестановку,
        запускаем рекурсию для них
        """

        if len(arr) == n:
            # преобразование в строку для возможности добавления в сет (чтобы избежать дубликатов)
            result.add(" ".join(map(str, arr)))
            return

        for idx, elem in enumerate(nums):

            # использование сета с индексами для оптимизации проверки вхождения элемента в текущую перестановку
            # O(1) vs O(n) если использовать list
            if idx not in used_idx:
                used_idx_copy = used_idx.copy()
                used_idx_copy.add(idx)
                generate_premutations_recursive(n, arr + [elem], used_idx_copy)

        return

    n = len(nums)
    # запускаем рекурсию для каждого элемента из списка как первого в перестановке
    for idx, elem in enumerate(nums):
        generate_premutations_recursive(n, [elem], set([idx]))

    result = [list(map(int, perm.split(" "))) for perm in result]
    return result


if __name__ == "__main__":
    nums = [1, 2, 3]

    print("Tracing Permutations of [1, 2, 3]...", end="\n\n")
    print(
        "\nPermutations of [1, 2, 3]:",
        permutations(nums),
        end="\n\n----------------\n\n",
    )
