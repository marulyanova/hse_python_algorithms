import pytest


class Node:
    def __init__(self, node_value=None, next_node=None):
        self.node_value = node_value
        self.next_node = next_node

    # переопределяем метод __str__ для удобного отображения print'ами для отладки
    def __str__(self):
        return str(self.node_value)


class Queue:
    def __init__(self):
        # инициализируем фиктивными нодами для обозначения начала и конца очереди
        self.back_node = Node(node_value="BACK", next_node=None)
        self.start_node = Node(node_value="START", next_node=self.back_node)

    def push_back(self, value):
        new_node = Node(node_value=value, next_node=None)

        # итерируемся, пока не найдем конечную ноду перед BACK
        iterator = self.start_node
        while iterator.next_node != self.back_node:
            iterator = iterator.next_node

        # вставляем новую ноду после конечной
        iterator.next_node = new_node
        new_node.next_node = self.back_node

    def pop_front(self):
        if self.start_node.next_node == self.back_node:
            return "Очередь пуста"
        else:
            # убираем первую ноду, связываем START со второй по счету
            pop_value = self.start_node.next_node.node_value
            self.start_node.next_node = self.start_node.next_node.next_node
            return pop_value

    # переопределяем метод __len__ для тестов
    def __len__(self):
        i = 0
        iterator = self.start_node
        while iterator.next_node != self.back_node:
            i += 1
            iterator = iterator.next_node
        return i

    def see_front(self):
        """Получить первый элемент"""

        if self.start_node.next_node == self.back_node:
            return "Очередь пуста"
        return self.start_node.next_node.node_value

    def see_back(self):
        """Получить последний элемент"""

        if self.start_node.next_node == self.back_node:
            return "Очередь пуста"
        iterator = self.start_node
        while iterator.next_node != self.back_node:
            iterator = iterator.next_node
        return iterator.node_value

    def get_queue(self):
        """Получить всю очередь"""

        iterator = self.start_node
        node_vals = []
        while iterator is not None:
            if iterator.node_value != "START" and iterator.node_value != "BACK":
                node_vals.append(iterator.node_value)
            iterator = iterator.next_node
        return node_vals


class Stack:
    def __init__(self):
        # инициализируем фиктивной нодой для обозначения головы стека
        self.start_node = Node(node_value="START", next_node=None)

    def push_back(self, value):
        # новый элемент - обновляем голову
        new_node = Node(node_value=value, next_node=self.start_node)
        self.start_node = new_node

    def pop_back(self):
        if self.start_node.node_value == "START":
            return "Стек пуст"

        # переставляем голову на второй элемент сверху
        pop_val = self.start_node.node_value
        self.start_node = self.start_node.next_node
        return pop_val

    # переопределяем метод __len__ для тестов
    def __len__(self):
        i = 0
        iterator = self.start_node
        while iterator.next_node is not None:
            i += 1
            iterator = iterator.next_node
        return i

    def see_back(self):
        """Получить последний элемент"""

        return (
            self.start_node.node_value
            if self.start_node.node_value != "START"
            else "Стек пуст"
        )

    def get_stack(self):
        """Получить весь сте. Справа - элементы, которые будут выниматься при .pop() первыми, слева - последними"""

        iterator = self.start_node
        node_vals = []
        while iterator is not None:
            if iterator.node_value != "START":
                node_vals.append(iterator.node_value)
            iterator = iterator.next_node
        return node_vals[::-1]


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
