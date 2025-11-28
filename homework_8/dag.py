from typing import Dict, List, Tuple
from collections import deque


def find_cycle(data: Dict[int, List[int]]) -> Tuple[bool, List[int]]:

    used = {key: 0 for key in data}
    cur_cycle = set()

    def dfs(v: int, flag: bool) -> bool:

        # взято в текущее рассмотрение
        used[v] = 1
        cur_cycle.add(v)

        for n in data[v]:
            if used[n] == 0:
                flag = dfs(n, flag)

            # если вершина-сосед есть в текущем рассмотрении
            elif used[n] == 1:
                flag = True

        # если не нашли цикл, текущую вершину оттуда удаляем
        if not flag:
            cur_cycle.discard(v)

        # окончено текущее рассмотрение
        used[v] = 2

        return flag

    is_cycle = False
    for v in data.keys():
        if used[v] == 0:
            is_cycle = dfs(v, is_cycle) or is_cycle
        if is_cycle:
            return True, list(cur_cycle)

        cur_cycle.clear()

    return False, []


def topological_sort(data: Dict[int, List[int]]) -> List[int]:
    """
    Пусть data = список смежности (словарь со списками ребер) = список исходящих ребер
    """

    is_cycle, cycle = find_cycle(data)
    if is_cycle:
        return cycle

    # Вычисляем кол-во вхоядщих ребер в каждую вершину
    input_edges = {key: 0 for key in data}
    for vertex in data:
        for neighbor in data[vertex]:
            input_edges[neighbor] += 1

    # добавляем вершины без входящих ребер в очередь
    queue = deque([vertex for vertex in data if input_edges[vertex] == 0])

    result = []
    while queue:
        cur_vertex = queue.popleft()
        result.append(cur_vertex)

        # проходим по соседям текущей вершины, убавляем кол-во входящих в них ребер
        # если у какой-то вершины кол-во входящ. = 0, добавляем ее в очередь
        for neighbor in data[cur_vertex]:
            input_edges[neighbor] -= 1
            if input_edges[neighbor] == 0:
                queue.append(neighbor)

    return result
