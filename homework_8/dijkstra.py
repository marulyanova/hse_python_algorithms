from typing import List

# для графа с положительными весами ребер


def dijkstra(start_v: int, data: List[List[int]]) -> List[int | float]:

    # матрица смежности на вход, где data[i][j] - стоимость пути из i в j

    if data == []:
        return []

    if start_v >= len(data):
        return None

    n = len(data)
    min_path = [float("inf")] * n
    min_path[start_v] = 0
    used = [0] * n

    for _ in range(len(data)):

        # ищем непосещённую вершину с минимальным расстоянием до нее
        v = -1
        for j in range(n):
            if not used[j] and (v == -1 or min_path[j] < min_path[v]):
                v = j

        # если остальные вершины недостижимы, выходим
        if v == -1 or min_path[v] == float("inf"):
            break

        used[v] = True

        # проходим по вершинам, пробуем обновить стоимость пути
        for i in range(n):
            # -1 <=> отсутствие связи
            if data[v][i] != -1:
                # если путь через текущую рассматриваемую вершину короче, чем записанный, обновляем его
                # добавляем в очередь для рассмотрения обновленного соседа
                if min_path[v] + data[v][i] < min_path[i]:
                    min_path[i] = min_path[v] + data[v][i]

    return min_path
