from collections import deque
# deque이용해서 stack 구현은 queue.pop()을 통해서 lifo 구현 (오른쪽 요소 pop), queue구현은 queue.popleft()을 통해 fifo구현

queue = deque()

queue.append(1)
queue.popleft()
queue.append(3)
queue.append(5)
queue.popleft()
queue.popleft()
queue.append(5)
queue.append(7)


print(queue)
print(list(queue)[::-1])