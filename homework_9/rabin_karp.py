from typing import List


def rabin_karp(s: str, pattern: str) -> List[int]:
    """Возвращает список индексов вхождений pattern в s"""

    n = len(s)
    m = len(pattern)

    if m == 0:  # в этой реализации пустой паттерн - не совпадает ни с чем
        return []

    if m > n:
        return []

    if m == n:
        return [0] if s == pattern else []

    result = []
    mod = int(1e9 + 7)
    base = 37  # простое число в качестве основания для хеширования

    # хэш для паттерна
    pattern_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod

    # хэш для первых m символов текста
    text_hash = 0
    for i in range(m):
        text_hash = (text_hash * base + ord(s[i])) % mod

    multiplier = base ** (m - 1) % mod

    # идем по строке скользящим окном
    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if s[i : i + m] == pattern:  # если совпадение хэшей, првоеряем посимвольно
                result.append(i)

        # убираем первый символ из хэша и добавляем следующий
        if i < n - m:
            text_hash = text_hash - ord(s[i]) * multiplier
            text_hash = text_hash * base + ord(s[i + m])
            text_hash %= mod
            if text_hash < 0:
                text_hash += mod

    return result
