from typing import List
from stack_vs_queue import Stack


def validate(pushed: List[int], popped: List[int]) -> bool:
    stack = Stack()
    res = []
    i = 0
    j = 0
    while j < len(pushed):

        # если i-й элемент в перестановке и j-й в оригинальном виде совпадают, добавляем в результат
        if popped[i] == pushed[j]:
            res.append(popped[i])
            i += 1
            j += 1

        # если i-й элемент в перестановке больше j-го в оригинальном виде, тогда складываем в стек "пропущенные" значения, i-й добавляем в результат
        # цикл заканчивается, когда в результат положено max значение из оригинальной подстановки
        elif popped[i] > pushed[j]:
            while pushed[j] < popped[i]:
                stack.push_back(pushed[j])
                j += 1
            res.append(popped[i])
            i += 1
            j += 1

        # если i-й элемент в перестановке меньше j-го в оригинальном виде, пытаемся вынуть из стека
        else:
            pop_val = stack.pop_back()
            if pop_val != popped[i]:
                return False
            res.append(pop_val)
            i += 1

    # оставшееся действие - опустошить стек. если сложенные элементы там соответствуют порядку перестановки, True
    stack_values = stack.get_stack()
    res.extend(stack_values[::-1])

    return res == popped
