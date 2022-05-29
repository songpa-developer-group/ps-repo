# https://www.geeksforgeeks.org/binary-heap/

import queue


class MaxHeap(object):
    def __init__(self, items):
        self.queue = items

        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return index * 2

    def right_child(self, index):
        return index * 2 + 1

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def heappush(self, n):
        self.queue.append(n)
        for i in range(len(self.queue)//2, 0, -1):
            self.max_heapify(i)

    def heappop(self):
        last_index = len(self.queue) - 1
        if last_index == 0:
            return - 1

        self.swap(1, last_index)
        max_value = self.queue.pop()
        self.max_heapify(1)
        return max_value

    def max_heapify(self, i):
        queue_length = len(self.queue) - 1
        left_index = self.left_child(i)
        right_index = self.right_child(i)
        current_index = i

        if left_index <= queue_length and self.queue[current_index] < self.queue[left_index]:
            current_index = left_index
        if right_index <= queue_length and self.queue[current_index] < self.queue[right_index]:
            current_index = right_index

        if current_index != i:
            self.swap(i, current_index)
            self.max_heapify(current_index)

    def heap(self):
        print(self.queue)


max_heap = MaxHeap([1, 2])
max_heap.heappush(1)
max_heap.heappush(3)
max_heap.heappush(5)
max_heap.heap()
max_heap.heappop()
max_heap.heap()
