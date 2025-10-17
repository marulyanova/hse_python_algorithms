class Node:
    def __init__(self, value=None, left_child=None, right_child=None):
        self.val = value
        self.l_child = left_child
        self.r_child = right_child


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.depth = 0

    def insert_node(self, value):
        # Если корня не было, инициализируем корень пришедшим значением
        if self.root is None:
            self.root = Node(value=value)
            return

        # Итерируемся по дереву, сравнивания значение и значения в нодах, ищем пустую ноду
        node_pointer = self.root
        while True:
            if value < node_pointer.val:
                if node_pointer.l_child is None:
                    node_pointer.l_child = Node(value)
                    return
                node_pointer = node_pointer.l_child
            else:
                if node_pointer.r_child is None:
                    node_pointer.r_child = Node(value)
                    return
                node_pointer = node_pointer.r_child

    def pre_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            res.append(node.val)
            iteration(node.l_child)
            iteration(node.r_child)

        iteration(self.root)
        return res

    def in_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            iteration(node.l_child)
            res.append(node.val)
            iteration(node.r_child)

        iteration(self.root)
        return res

    def post_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            iteration(node.l_child)
            iteration(node.r_child)
            res.append(node.val)

        iteration(self.root)
        return res

    def reverse_pre_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            res.append(node.val)
            iteration(node.r_child)
            iteration(node.l_child)

        iteration(self.root)
        return res

    def reverse_post_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            iteration(node.r_child)
            iteration(node.l_child)
            res.append(node.val)

        iteration(self.root)
        return res

    def reverse_in_order(self):
        res = []

        def iteration(node):
            if not node:
                return
            iteration(node.r_child)
            res.append(node.val)
            iteration(node.l_child)

        iteration(self.root)
        return res
