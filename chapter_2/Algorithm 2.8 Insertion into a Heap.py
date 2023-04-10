class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete_min(self):
        if len(self.heap_list) == 1:
            return None
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return root

    def search(self, k):
        if k in self.heap_list:
            return True
        return False

    def heap_sort(self):
        result = []
        while self.current_size > 0:
            result.append(self.delete_min())
        return result


h = Heap()
h.insert(5)
h.insert(3)
h.insert(8)
h.insert(2)
h.insert(4)
h.insert(1)
print(h.heap_list)
print(h.delete_min())
print(h.heap_list)
print(h.search(5))
print(h.search(10))
print(h.heap_sort())
