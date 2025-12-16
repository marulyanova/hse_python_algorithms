import pytest
from LCS import lcs


def test_exmple():
    string_1 = "AGGTAB"
    string_2 = "GXTXAYB"
    assert lcs(string_1, string_2) == "GTAB"


def test_empty_strings():
    assert lcs("", "") == ""
    assert lcs("abc", "") == ""
    assert lcs("", "a") == ""


def test_no_common_subseq():
    assert lcs("abcd", "qwerty") == ""
    assert lcs("123456", "7890") == ""


def test_1_char_match():
    assert lcs("abcabc", "a") == "a"
    assert lcs("qwerty", "w") == "w"


def test_many_char_match():
    assert lcs("qwerty", "wty") == "wty"
    assert lcs("abacaba", "abak") == "aba"


def text_all_match():
    assert lcs("aaaa", "aaaa") == "aaaa"
    assert lcs("bbbbbb", "bbbbbb") == "bbbbbb"


def test_other():
    assert lcs("123abc567", "3Kbc7856") == "3bc56"
    assert lcs("ANCABC", "aAcCNbc") == "AC"


if __name__ == "__main__":
    pytest.main()
