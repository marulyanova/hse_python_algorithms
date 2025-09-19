import pytest


# O(N)
def is_palindrome(x: int) -> bool:
    """Checks if passed value is a palindrome"""

    # if the number entry consists of a single digit
    if x < 10:
        return True

    i = 0
    while 10**i < x:
        i += 1
    i -= 1

    # get the first and last digits and compare them
    while x > 0:
        if x // (10**i) == x % 10:
            x %= 10**i
            x //= 10
            i -= 2

            if x < 10:
                return True

            continue
        else:
            return False
    return True


def test_single_digit():
    assert is_palindrome(1) == True
    assert is_palindrome(3) == True
    assert is_palindrome(9) == True
    assert is_palindrome(0) == True


def test_double_digit():
    assert is_palindrome(11) == True
    assert is_palindrome(33) == True
    assert is_palindrome(99) == True
    assert is_palindrome(23) == False
    assert is_palindrome(98) == False
    assert is_palindrome(55) == True
    assert is_palindrome(65) == False
    assert is_palindrome(34) == False


def test_triple_digit():
    assert is_palindrome(110) == False
    assert is_palindrome(330) == False
    assert is_palindrome(202) == True
    assert is_palindrome(230) == False
    assert is_palindrome(100) == False
    assert is_palindrome(555) == True
    assert is_palindrome(543) == False
    assert is_palindrome(909) == True


def test_other_digit():
    assert is_palindrome(1111) == True
    assert is_palindrome(3223) == True
    assert is_palindrome(20202) == True
    assert is_palindrome(23032) == True
    assert is_palindrome(10000001) == True
    assert is_palindrome(5554444555) == True
    assert is_palindrome(543213469041345561111) == False
    assert is_palindrome(90900909) == True
    assert (
        is_palindrome(11111111111111111111111111111111111111111111111111111111) == True
    )
    assert (
        is_palindrome(11111111111111101111111111111111111111111111111111111111) == False
    )
    assert (
        is_palindrome(12111111111111111111111111111111111111111111111111111121) == True
    )
    assert is_palindrome(8995210333333333333330125998) == True
    assert is_palindrome(121) == True
    assert is_palindrome(31) == False


if __name__ == "__main__":
    pytest.main()
