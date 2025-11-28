from typing import Dict, List, Tuple


def find_connectivity_components(
    data: Dict[int, List[int]],
) -> Tuple[int, List[List[int]]]:

    used = set()
    elems_cur_comp = set()

    def dfs(v: int):
        used.add(v)
        elems_cur_comp.add(v)
        for n in data[v]:
            if n not in used:
                dfs(n)
        return

    cnt_comp = 0
    elems_comp = []
    for v in data.keys():

        # идем по вершинам, если вершина не в used, запускаем dfs и +1 к счетчику компонент связности
        if v not in used:
            cnt_comp += 1
            dfs(v)

            # после прохождения по текущей компоненте добавляем в результат множество её вершин
            elems_comp.append(list(elems_cur_comp))
            elems_cur_comp.clear()

    return cnt_comp, elems_comp
