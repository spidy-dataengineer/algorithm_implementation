# Breadth Frist Search 너비 우선탐색 O(N)
"""
BFS는 선입선출 방식인 큐 자료구조를 이용

인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하면 자연스럽게 먼저 들어온 것이 먼저 나가게 되어, 가까운 노드부터 탐색을 진행

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 함
3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복

"""
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited): # start는 시작 지점, vistied는 방문 여부
    queue = deque([start])
    print(queue)
    # 시작 노드 방문 처리
    visited[start] = True
    # 큐에 남아 있는 요소가 없을 때 까지
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end= ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            print(graph[v])
            print(i)
            if not visited[i]:
                print(visited[i])
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
bfs(graph, 1, visited)