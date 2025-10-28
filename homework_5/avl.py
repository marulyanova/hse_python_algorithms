import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from homework_4.balanced_binary_tree import (
    check_balanced,
    find_highest_disbalance,
    invoke_compute_depth,
)
from homework_4.traversal import Node, BinarySearchTree


class AVL(BinarySearchTree):
    def __init__(self):
        self.root = None

    def is_balanced(self) -> bool:
        """Переиспользование функции из прошлого ДЗ"""
        return check_balanced(self.root)

    def left_mini_rotation(self, node: Node) -> Node:
        """Малое левое вращение"""

        if node is None or node.r_child is None:
            return node
        right = node.r_child
        node.r_child = right.l_child
        right.l_child = node
        return right

    def right_mini_rotation(self, node: Node) -> Node:
        """Малое правое вращение"""

        if node is None or node.l_child is None:
            return node
        left = node.l_child
        node.l_child = left.r_child
        left.r_child = node
        return left

    def left_big_rotation(self, node: Node) -> Node:
        """Большое левое вращение"""

        if node is None or node.r_child is None:
            return node
        node.r_child = self.right_mini_rotation(node.r_child)
        return self.left_mini_rotation(node)

    def right_big_rotation(self, node: Node) -> Node:
        """Большое правое вращение"""

        if node is None or node.l_child is None:
            return node
        node.l_child = self.left_mini_rotation(node.l_child)
        return self.right_mini_rotation(node)

    def find_parent(self, root: Node, child: Node) -> Node:
        """Ищет родителя для заданной ноды child, начиная с root"""

        if root is None or child is None or root is child:
            return None
        pointer = root
        parent = None
        while pointer and pointer is not child:
            parent = pointer
            if child.val < pointer.val:
                pointer = pointer.l_child
            else:
                pointer = pointer.r_child
        if pointer is child:
            return parent
        return None

    def replace_child(self, parent: Node, old_child: Node, new_child: Node):
        """
        Заменяет у parent ссылку old_child на new_child.
        Если parent is None, это означает, что заменяем корень дерева
        """

        if parent is None:
            self.root = new_child
            return
        if parent.l_child is old_child:
            parent.l_child = new_child
        elif parent.r_child is old_child:
            parent.r_child = new_child

    def insert_node(self, value):
        """Метод вставки узла с последующей балансировкой"""

        if self.search(value):
            return f"Нода со значением {value} уже существует в дереве"

        super().insert_node(value)

        # Пока дерево не сбалансировано, ищем место для вращения и делаем его
        while not self.is_balanced():
            node_for_rotation = find_highest_disbalance(self.root)
            if not node_for_rotation:
                break

            left_depth = invoke_compute_depth(node_for_rotation.l_child)
            right_depth = invoke_compute_depth(node_for_rotation.r_child)

            parent = self.find_parent(self.root, node_for_rotation)

            if left_depth - right_depth > 1:
                left_left_depth = invoke_compute_depth(
                    node_for_rotation.l_child.l_child
                )
                left_right_depth = invoke_compute_depth(
                    node_for_rotation.l_child.r_child
                )

                if left_left_depth >= left_right_depth:
                    new_subroot = self.right_mini_rotation(node_for_rotation)
                else:
                    new_subroot = self.right_big_rotation(node_for_rotation)

                self.replace_child(parent, node_for_rotation, new_subroot)

            elif right_depth - left_depth > 1:
                right_right_depth = invoke_compute_depth(
                    node_for_rotation.r_child.r_child
                )
                right_left_depth = invoke_compute_depth(
                    node_for_rotation.r_child.l_child
                )

                if right_right_depth >= right_left_depth:
                    new_subroot = self.left_mini_rotation(node_for_rotation)
                else:
                    new_subroot = self.left_big_rotation(node_for_rotation)

                self.replace_child(parent, node_for_rotation, new_subroot)

    def delete_node(self, value):
        """Метод удаления узла с последующей балансировкой"""

        if self.root is None:
            return f"Дерево пустое"

        # Удаляемая нода и ее родитель
        parent = None
        node_pointer = self.root

        while node_pointer and node_pointer.val != value:
            parent = node_pointer
            if value < node_pointer.val:
                node_pointer = node_pointer.l_child
            else:
                node_pointer = node_pointer.r_child

        if node_pointer is None:
            return f"Нода со значением {value} не найдена в дереве"

        # Удаляемая нода - лист
        if node_pointer.l_child is None and node_pointer.r_child is None:
            self.replace_child(parent, node_pointer, None)

        # Удаляемая нода с одним ребенком
        elif node_pointer.l_child is None:
            self.replace_child(parent, node_pointer, node_pointer.r_child)
        elif node_pointer.r_child is None:
            self.replace_child(parent, node_pointer, node_pointer.l_child)

        # Удаляемая нода с двумя детьми
        else:
            next_parent = node_pointer
            next = node_pointer.r_child
            while next.l_child:
                next_parent = next
                next = next.l_child

            node_pointer.val = next.val

            # Удаление узла
            if next_parent.l_child is next:
                next_parent.l_child = next.r_child
            else:
                next_parent.r_child = next.r_child

        # Балансировка
        while True:
            if self.is_balanced():
                break
            node_for_rotation = find_highest_disbalance(self.root)
            if not node_for_rotation:
                break

            left_depth = invoke_compute_depth(node_for_rotation.l_child)
            right_depth = invoke_compute_depth(node_for_rotation.r_child)
            parent = self.find_parent(self.root, node_for_rotation)

            if left_depth - right_depth > 1:
                left_left_depth = invoke_compute_depth(
                    node_for_rotation.l_child.l_child
                )
                left_right_depth = invoke_compute_depth(
                    node_for_rotation.l_child.r_child
                )

                if left_left_depth >= left_right_depth:
                    new_subroot = self.right_mini_rotation(node_for_rotation)
                else:
                    new_subroot = self.right_big_rotation(node_for_rotation)

                self.replace_child(parent, node_for_rotation, new_subroot)

            elif right_depth - left_depth > 1:
                right_right_depth = invoke_compute_depth(
                    node_for_rotation.r_child.r_child
                )
                right_left_depth = invoke_compute_depth(
                    node_for_rotation.r_child.l_child
                )

                if right_right_depth >= right_left_depth:
                    new_subroot = self.left_mini_rotation(node_for_rotation)
                else:
                    new_subroot = self.left_big_rotation(node_for_rotation)

                self.replace_child(parent, node_for_rotation, new_subroot)

        return f"Нода со значением {value} успешно удалена"

    def search(self, value) -> bool:
        """Метод поиска узла по значению"""

        node_pointer = self.root
        while node_pointer:
            if value == node_pointer.val:
                return True
            elif value < node_pointer.val:
                node_pointer = node_pointer.l_child
            else:
                node_pointer = node_pointer.r_child
        return False
