from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()  # deque를 이용한 큐 구현 (빠른 O(1) 연산)

    def enqueue(self, item):
        self.queue.append(item)  # 큐의 끝에 요소 추가 (O(1))

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # 큐의 앞에서 요소 제거 및 반환 (O(1))
        return None

    def is_empty(self):
        return len(self.queue) == 0  # 큐가 비었는지 확인

    def size(self):
        return len(self.queue)  # 큐 크기 반환

# 사용 예시
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1 (선입선출, FIFO)


class Queue:
    def __init__(self):
        self.queue = []  # 리스트를 이용한 큐

    def enqueue(self, item):
        """ 큐의 끝에 요소 추가 (O(1)) """
        self.queue.append(item)

    def dequeue(self):
        """ 큐의 앞 요소 제거 및 반환 (O(N)) """
        if not self.is_empty():
            return self.queue.pop(0)  # 리스트의 첫 요소 제거 (O(N))
        return None  # 큐가 비어 있으면 None 반환

    def is_empty(self):
        """ 큐가 비어있는지 확인 """
        return len(self.queue) == 0

    def size(self):
        """ 큐의 크기 반환 """
        return len(self.queue)

# 사용 예시
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.dequeue())  # 2

