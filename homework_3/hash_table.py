from copy import deepcopy


class HashTable:
    def __init__(self, capacity=1000, threshold=0.7):
        self.capacity = capacity
        self.elems = [[] for _ in range(capacity)]
        self.threshold = threshold

    def hash(self, key):
        """Получаем хэш для ключа и его индекс в массиве"""
        return hash(key) % self.capacity

    def put(self, key, value):
        """Добавление/обновление элемента по ключу"""

        idx = self.hash(key)  # получаем индекс в массиве элементов
        # если ключ уже есть, обновляем значение
        # идем по всем элементам в ячейке с таким индексом, так как могут быть коллизии
        for i, (k, _) in enumerate(self.elems[idx]):
            if k == key:
                self.elems[idx][i] = (key, value)
                return

        # иначе добавляем новый элемент
        self.elems[idx].append((key, value))

        # проверяем количество элементов в таблице
        if self.check_capacity_excceeding():
            self.expand_capacity()

    def get(self, key):
        idx = self.hash(key)
        # идем по всем элементам в ячейке с таким индексом, так как могут быть коллизии
        for k, v in self.elems[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self.hash(key)
        # идем по всем элементам в ячейке с таким индексом, так как могут быть коллизии
        for i, (k, _) in enumerate(self.elems[idx]):
            if k == key:
                del self.elems[idx][i]
                return

    def check_capacity_excceeding(self):
        """Проверяем, заполнилась ли таблица больше, чем на threshold"""

        num_elems = 0
        for elem in self.elems:
            if elem != []:
                num_elems += 1
        if num_elems / self.capacity > self.threshold:
            return True
        return False

    def expand_capacity(self):
        """Увеличиваем хэш-таблицу в 2 раза, перехешируем все элементы"""

        stored_elems = deepcopy(self.elems)
        self.capacity *= 2
        self.elems = [[] for _ in range(self.capacity)]

        for elem in stored_elems:
            for key, value in elem:
                self.put(key, value)
