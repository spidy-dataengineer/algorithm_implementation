class MinHeap:
    def __init__(self):
        self.heap = []

    def __parent(self, index):
        return (index - 1) // 2

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2

    def __heapify_up(self, index):
        while index > 0 and self.heap[self.__parent(index)] > self.heap[index]:
            # Swap with parent
            self.heap[self.__parent(index)], self.heap[index] = self.heap[index], self.heap[self.__parent(index)]
            index = self.__parent(index)

    def __heapify_down(self, index):
        left = self.__left_child(index)
        right = self.__right_child(index)
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            # Swap with smallest child
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.__heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self.__heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

# 예시
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(3)

print(min_heap.pop())  # 3 (가장 작은 값)
print(min_heap.peek())  # 5 (현재 루트 값)

class MaxHeap:
    def __init__(self):
        self.heap = []

    def __parent(self, index):
        return (index - 1) // 2

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2

    def __heapify_up(self, index):
        while index > 0 and self.heap[self.__parent(index)] < self.heap[index]:
            # Swap with parent
            self.heap[self.__parent(index)], self.heap[index] = self.heap[index], self.heap[self.__parent(index)]
            index = self.__parent(index)

    def __heapify_down(self, index):
        left = self.__left_child(index)
        right = self.__right_child(index)
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            # Swap with largest child
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__heapify_down(largest)

    def insert(self, value):
        self.heap.append(value)
        self.__heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

# 예시
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.insert(3)

print(max_heap.pop())  # 20 (가장 큰 값)
print(max_heap.peek())  # 10 (현재 루트 값)

import heapq

# 최소 힙을 사용한 예시
min_heap = []

# 요소 삽입 (heappush)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)

print("최소 힙 상태:", min_heap)  # 힙은 항상 최소값을 루트로 유지

# 가장 작은 값 꺼내기 (heappop)
print(heapq.heappop(min_heap))  # 3 (가장 작은 값)
print("힙 상태:", min_heap)  # 나머지 값들

import heapq

# 최대 힙을 사용한 예시 (부호 반전)
max_heap = []

# 요소 삽입 (heappush), 음수로 저장하여 최대 힙처럼 사용
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)

print("최대 힙 상태:", max_heap)  # 음수로 저장됨

# 가장 큰 값 꺼내기 (heappop), 다시 음수로 변환
print(-heapq.heappop(max_heap))  # 20 (가장 큰 값)
print("힙 상태:", [-x for x in max_heap])  # 원래 값들로 표시
