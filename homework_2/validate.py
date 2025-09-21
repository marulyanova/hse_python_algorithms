import pytest
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

        # если i-й элемент в перестановке меньше j-го в оригинальном виде, вынимаем из стека
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


def test_provided_cases():
    assert validate([1, 2, 3], [3, 1, 2]) == False
    assert validate([1, 2, 3, 4, 5], [1, 3, 5, 4, 2])


def test_corner_cases():
    assert validate([1], [1]) == True
    assert validate([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == True
    assert validate([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == True
    assert validate([1, 2], [1, 2]) == True
    assert validate([2, 1], [2, 1]) == True


def test_true_cases():
    assert validate([1, 2, 3, 4, 5], [2, 1, 3, 4, 5]) == True
    assert validate([1, 2, 3, 4, 5], [3, 2, 1, 4, 5]) == True
    assert validate([1, 2, 3, 4, 5], [4, 3, 2, 1, 5]) == True
    assert validate([1, 2, 3, 4, 5], [3, 4, 5, 2, 1]) == True
    assert validate([1, 2, 3, 4, 5], [1, 4, 3, 2, 5]) == True
    assert validate([1, 2, 3, 4, 5], [1, 2, 5, 4, 3]) == True
    assert validate([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 4, 3, 5, 2, 7, 6]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 4, 3, 5, 2, 6, 7]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 5, 4, 6, 3, 2, 7]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 5, 4, 6, 7, 3, 2]) == True
    assert validate([1, 2, 3, 4], [3, 4, 2, 1]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 7, 6, 5, 4]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 5, 4, 7, 6]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 5, 4, 6, 7]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [6, 5, 4, 3, 2, 1, 7]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [6, 5, 4, 3, 2, 7, 1]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 5, 6, 4, 7]) == True
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 5, 7, 6, 4]) == True


def test_false_cases():
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 5, 4, 7, 3, 2, 6]) == False
    assert validate([1, 2, 3, 4], [4, 1, 3, 2]) == False
    assert validate([1, 2, 3, 4], [4, 2, 3, 1]) == False
    assert validate([1, 2, 3, 4], [4, 3, 1, 2]) == False
    assert validate([1, 2, 3, 4], [3, 1, 2, 4]) == False
    assert validate([1, 2, 3, 4], [3, 4, 1, 2]) == False
    assert validate([1, 2, 3, 4], [3, 4, 1, 2]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [7, 1, 2, 3, 4, 5, 6]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [7, 6, 2, 3, 4, 5, 6]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 2, 3, 1]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 1, 2]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 7, 6, 4, 5]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 5, 7, 4, 6]) == False
    assert validate([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 7, 4, 6, 5]) == False


if __name__ == "__main__":
    pytest.main()
