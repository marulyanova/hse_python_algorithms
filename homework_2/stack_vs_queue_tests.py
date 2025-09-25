import pytest
from stack_vs_queue import Queue, Stack


def test_queue_class():
    # пустая очередь
    q = Queue()
    assert len(q) == 0
    assert q.see_front() == "Очередь пуста"
    assert q.get_queue() == []
    assert q.see_back() == "Очередь пуста"

    # добавили 1 элемент
    q.push_back(1)
    assert len(q) == 1
    assert q.get_queue() == [1]
    assert q.see_back() == 1
    assert q.see_front() == 1

    # добавили 3 элемента
    q.push_back(2)
    q.push_back(3)
    q.push_back(4)
    assert len(q) == 4
    assert q.get_queue() == [1, 2, 3, 4]
    assert q.see_back() == 4
    assert q.see_front() == 1

    # удалили 2 элемента
    pop_val = q.pop_front()
    assert pop_val == 1
    pop_val = q.pop_front()
    assert pop_val == 2
    assert len(q) == 2
    assert q.see_back() == 4
    assert q.see_front() == 3
    assert q.get_queue() == [3, 4]

    # удалили еще 2 элемента
    pop_val = q.pop_front()
    assert pop_val == 3
    pop_val = q.pop_front()
    assert pop_val == 4
    pop_val = q.pop_front()
    assert pop_val == "Очередь пуста"
    assert q.see_front() == "Очередь пуста"
    assert q.get_queue() == []
    assert q.see_back() == "Очередь пуста"

    # добавили 100 элементов
    for i in range(100):
        q.push_back(i)
    assert len(q) == 100
    assert q.see_back() == 99
    pop_val = q.pop_front()
    assert pop_val == 0

    for i in range(50):
        pop_val = q.pop_front()
    assert pop_val == 50
    assert q.get_queue() == [i for i in range(51, 100)]

    # элементы других типов
    q = Queue()
    q.push_back("aaavbbb")
    q.push_back([1, -1, 4, -5])
    q.push_back({"a": "b"})
    assert len(q) == 3
    pop_val = q.pop_front()
    assert pop_val == "aaavbbb"
    pop_val = q.pop_front()
    assert pop_val == [1, -1, 4, -5]
    pop_val = q.pop_front()
    assert pop_val == {"a": "b"}


def test_stack_class():
    # пустой стек
    s = Stack()
    assert len(s) == 0
    assert s.get_stack() == []
    assert s.see_back() == "Стек пуст"
    assert s.pop_back() == "Стек пуст"

    # добавляем 1 элемент
    s.push_back(123)
    assert len(s) == 1
    assert s.get_stack() == [123]
    pop_val = s.pop_back()
    assert pop_val == 123

    # добавляем 3 элемента
    s.push_back(456)
    s.push_back("abacaba")
    s.push_back(set([1, 1, 2, 2, 3, 3, 3]))
    assert len(s) == 3
    assert s.get_stack() == [456, "abacaba", set([1, 2, 3])]

    pop_val = s.pop_back()
    assert pop_val == set([1, 2, 3])
    assert s.see_back() == "abacaba"
    assert len(s) == 2

    pop_val = s.pop_back()
    assert pop_val == "abacaba"
    assert len(s) == 1
    assert s.see_back() == 456

    pop_val = s.pop_back()
    assert pop_val == 456
    assert len(s) == 0
    assert s.see_back() == "Стек пуст"

    pop_val = s.pop_back()
    assert pop_val == "Стек пуст"
    assert len(s) == 0


if __name__ == "__main__":
    pytest.main()
