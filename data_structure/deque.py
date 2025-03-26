from collections import deque

dq = deque()  # 양방향 큐 생성

dq.append(1)  # 오른쪽 삽입
dq.appendleft(2)  # 왼쪽 삽입
print(dq.pop())  # 오른쪽 요소 제거 (1)
print(dq.popleft())  # 왼쪽 요소 제거 (2)
