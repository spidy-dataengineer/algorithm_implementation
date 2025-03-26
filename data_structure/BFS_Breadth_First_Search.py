from collections import deque

def bfs(graph, start):
    visited = set()  # 방문한 노드 저장
    queue = deque([start])  # BFS를 위한 큐 초기화

    while queue:
        node = queue.popleft()  # 큐에서 첫 번째 요소 꺼냄
        if node not in visited:
            print(node, end=" ")  # 방문한 노드 출력
            visited.add(node)  # 방문 표시
            queue.extend(graph[node])  # 인접 노드들을 큐에 추가

# 그래프 예시 (인접 리스트 표현)
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7],
    5: [],
    6: [],
    7: []
}

bfs(graph, 1)  # 1 2 3 4 5 6 7
