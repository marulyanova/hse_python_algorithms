from typing import List


def anagrams(strs: List[str]) -> List[List[str]]:
    """Сортируем каждую строку, складываем в словарь {"канонический вид строки (сортированный)": [массив строк]}"""

    d = {}
    for string in strs:
        sort_string = "".join(sorted(string))
        if sort_string in d:
            d[sort_string].append(string)
        else:
            d[sort_string] = [string]

    return list(d.values())
