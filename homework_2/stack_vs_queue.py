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
        # итерируемся до конца пока не упремся в BACK-ноду
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
        # инициализируем фиктивной нодой для обозначения головы стека (голова - элемент, который лежит сверху, при pop уйдет первый)
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
        """Получить весь стек. Справа (в конце списка) - элементы, которые будут выниматься при .pop() первыми, слева (в начале списка) - последними"""

        iterator = self.start_node
        node_vals = []
        while iterator is not None:
            if iterator.node_value != "START":
                node_vals.append(iterator.node_value)
            iterator = iterator.next_node
        return node_vals[::-1]
