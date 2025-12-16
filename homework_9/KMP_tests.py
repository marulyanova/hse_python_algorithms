import pytest
from KMP import kmp, make_prefix_function


def test_prefix_function():
    assert make_prefix_function("ababc") == [0, 0, 1, 2, 0]
    assert make_prefix_function("aaaa") == [0, 1, 2, 3]
    assert make_prefix_function("abcd") == [0, 0, 0, 0]
    assert make_prefix_function("aabaaab") == [0, 1, 0, 1, 2, 2, 3]
    assert make_prefix_function("") == []
    assert make_prefix_function("a") == [0]
    assert make_prefix_function("abcdefgh") == [0, 0, 0, 0, 0, 0, 0, 0]


def test_empty_strings():
    assert kmp("", "") == 0
    assert kmp("abc", "") == 0
    assert kmp("", "a") == -1


def test_pattern_longet_string():
    assert kmp("abc", "abcdef") == -1
    assert kmp("", "aaaa") == -1


def test_no_match():
    assert kmp("abcdef", "xxx") == -1
    assert kmp("qwertyuiop", "aaaaa") == -1


def test_single_character_pattern():
    assert kmp("aaaaa", "a") == 0
    assert kmp("abcdec", "c") == 2
    assert kmp("xyzabcz", "z") == 2


def test_multiple_match():
    assert kmp("ababcabc", "abc") == 2
    assert kmp("aaaaaa", "aa") == 0
    assert kmp("abababab", "ab") == 0


def test_overlap_patterns():
    assert kmp("aaaa", "aa") == 0
    assert kmp("abababa", "aba") == 0


def test_digits_special_characters():
    assert kmp("123123123", "123") == 0
    assert kmp("*()@*()", "*()") == 0
    assert kmp("a1b2c3", "b2") == 2
    assert kmp("423123123", "123") == 3


if __name__ == "__main__":
    pytest.main()
