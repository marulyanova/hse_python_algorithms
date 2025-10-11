import pytest
from anagrams import anagrams
from typing import List


def to_canonical(arr: List[List[str]]) -> List[List[str]]:
    # для сортировки в одном порядке эталонного ответа и получившегося

    arr = [sorted(item) for item in arr]  # сортировка внутри каждой группы анаграмм
    # сортировка всех групп анаграмм по увеличению размера групп
    # если группы одинаковые, то в лексикографическом порядке содержимого
    return sorted(sorted(arr, key=lambda x: len(x)))


def test_provided_cases():
    # данные в задании примеры
    assert to_canonical(
        anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == to_canonical(
        [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]
    )


def test_corner_cases():
    assert to_canonical(anagrams([""])) == to_canonical([[""]])
    assert to_canonical(anagrams(["", "", ""])) == to_canonical([["", "", ""]])
    assert to_canonical(anagrams(["", "a"])) == to_canonical([[""], ["a"]])
    assert to_canonical(anagrams(["a", "a"])) == to_canonical([["a", "a"]])
    assert to_canonical(anagrams(["a", "b"])) == to_canonical([["a"], ["b"]])


def test_other_cases():
    assert to_canonical(anagrams(["aba", "baa", "aab", "aac", "caa"])) == to_canonical(
        [["aba", "baa", "aab"], ["caa", "aac"]]
    )

    assert to_canonical(
        anagrams(["aba", "baa", "aab", "aac", "caa", "kaa"])
    ) == to_canonical([["aba", "baa", "aab"], ["caa", "aac"], ["kaa"]])

    assert to_canonical(
        anagrams(["aba", "baa", "aab", "aac", "caa", "kaa", "aka"])
    ) == to_canonical([["aba", "baa", "aab"], ["caa", "aac"], ["kaa", "aka"]])

    assert to_canonical(
        anagrams(["tea", "cat", "abacaba", "aet", "tac", "cabaaba", "cababaa"])
    ) == to_canonical(
        [["cat", "tac"], ["tea", "aet"], ["cabaaba", "cababaa", "abacaba"]]
    )

    assert to_canonical(anagrams(["aaa", "aaaaa", "aaaaaaa", "a"])) == to_canonical(
        [["aaa"], ["aaaaaaa"], ["a"], ["aaaaa"]]
    )


if __name__ == "__main__":
    pytest.main()
