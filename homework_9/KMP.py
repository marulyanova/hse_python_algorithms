def make_prefix_function(pattern: str):
    """Построение префикс-функции"""

    prefix = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            prefix[i] = j
        else:
            prefix[i] = 0

    return prefix


def kmp(s: str, pattern: str) -> int:
    """Возвращает индекс первого вхождения подстроки в строку"""

    if len(pattern) == 0:
        return 0

    if len(pattern) > len(s):
        return -1

    prefix = make_prefix_function(pattern)
    i, j = 0, 0

    while i < len(s):
        # если символы совпадают, продвигаемся дальше
        if s[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        else:
            # иначе откатываемся по паттерну назад по префикс-функции
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1
    return -1
