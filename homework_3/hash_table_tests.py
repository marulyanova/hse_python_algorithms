import pytest
from hash_table import HashTable


def test_easy_hash_table():
    ht = HashTable(capacity=2, threshold=0.5)
    assert ht.capacity == 2
    assert ht.elems == [[], []]
    assert ht.threshold == 0.5

    assert ht.get("a") is None
    ht.put("a", 1)
    assert ht.get("a") == 1
    assert ht.check_capacity_excceeding() is False
    assert ht.elems.count([]) == 1
    assert ht.elems.count([("a", 1)]) == 1

    ht.put("b", 2)
    assert ht.get("b") == 2
    assert ht.check_capacity_excceeding() is False

    ht.put("c", 3)
    assert ht.get("c") == 3

    ht.put("d", 4)
    assert ht.get("d") == 4

    assert ht.capacity > 2
    assert ht.check_capacity_excceeding() is False


def test_hash_table():
    ht = HashTable(capacity=1000, threshold=0.5)
    assert ht.capacity == 1000
    assert ht.elems == [[] for _ in range(1000)]
    assert ht.threshold == 0.5

    assert ht.get("a") is None
    ht.put("a", 1)
    assert ht.get("a") == 1
    assert ht.check_capacity_excceeding() is False
    assert ht.elems.count([]) == 999
    assert ht.elems.count([("a", 1)]) == 1

    for i in range(1, 1000):
        ht.put(f"key{i}", i + 1)
        assert ht.get(f"key{i}") == i + 1

    assert ht.check_capacity_excceeding() is False
    ht.put("key500", 501)
    assert ht.get("key500") == 501
    assert ht.capacity > 1000
    assert ht.check_capacity_excceeding() is False


if __name__ == "__main__":
    pytest.main()
