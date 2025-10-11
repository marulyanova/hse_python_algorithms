from typing import List, Tuple


def two_sum(arr: List[int], k: int) -> Tuple[int, int]:
    """Идем по массиву, проверяем, есть ли в словаре элемент (k - текущий элемент)
    Если да, то возвращаем пару индексов
    Иначе складываем в словарь {"число": "текущий индекс"}"""

    d = {}
    for ind, num in enumerate(arr):
        if k - num in d:
            return (d[k - num], ind)
        d[num] = ind
