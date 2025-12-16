import pytest
from rabin_karp import rabin_karp


def test_empty_strings():
    assert rabin_karp("", "") == []
    assert rabin_karp("aaa", "") == []
    assert rabin_karp("", "aaa") == []


def test_pattern_longer_than_string():
    assert rabin_karp("abcd", "abcdef") == []
    assert rabin_karp("ab", "aaaa") == []


def test_no_match():
    assert rabin_karp("abcdef", "xxx") == []
    assert rabin_karp("qwertyuiop", "aaaaa") == []


def test_single_character_pattern():
    assert rabin_karp("aaaaa", "a") == [0, 1, 2, 3, 4]
    assert rabin_karp("abcdec", "c") == [2, 5]
    assert rabin_karp("xyzabcz", "z") == [2, 6]
    assert rabin_karp("xyz", "z") == [2]
    assert rabin_karp("abcde", "d") == [3]


def test_multiple_match():
    assert rabin_karp("ababcabc", "abc") == [2, 5]
    assert rabin_karp("aaaaaa", "aa") == [0, 1, 2, 3, 4]
    assert rabin_karp("abababab", "ab") == [0, 2, 4, 6]


def test_overlap_patterns():
    assert rabin_karp("aaaa", "aa") == [0, 1, 2]
    assert rabin_karp("abababa", "aba") == [0, 2, 4]


def test_digits_special_characters():
    assert rabin_karp("123123123", "123") == [0, 3, 6]
    assert rabin_karp("*()@*()", "*()") == [0, 4]
    assert rabin_karp("a1b2c3", "b2") == [2]


if __name__ == "__main__":
    pytest.main()
