import pytest


def is_prime(x: int) -> bool:
    """Checks if input x digit is a prime"""

    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    # it is enough to check divisors to the root
    for i in range(3, int(round((x**0.5), 0)) + 1):
        if x % i == 0:
            return False
    return True


# O(N * sqrt(N))
def prime_digits_before_n(n: int) -> int:
    """Counts the number of prime digits before input N"""

    if n < 3:
        return 0

    if n == 3:
        return 1

    cnt = 0
    for i in range(2, n):
        if is_prime(i):
            cnt += 1

    return cnt


def test_test_cases():
    assert prime_digits_before_n(10) == 4
    assert prime_digits_before_n(1) == 0


def test_easy_cases():
    assert prime_digits_before_n(2) == 0
    assert prime_digits_before_n(3) == 1
    assert prime_digits_before_n(5) == 2
    assert prime_digits_before_n(6) == 3
    assert prime_digits_before_n(7) == 3
    assert prime_digits_before_n(9) == 4
    assert prime_digits_before_n(11) == 4
    assert prime_digits_before_n(12) == 5
    assert prime_digits_before_n(13) == 5
    assert prime_digits_before_n(14) == 6
    assert prime_digits_before_n(15) == 6


def test_complex_cases():
    assert prime_digits_before_n(30) == 10
    assert prime_digits_before_n(32) == 11
    assert prime_digits_before_n(72) == 20
    assert prime_digits_before_n(69) == 19


if __name__ == "__main__":
    pytest.main()
