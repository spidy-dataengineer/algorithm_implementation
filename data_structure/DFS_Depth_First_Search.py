def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")  # 방문한 노드 출력
        visited.add(node)  # 방문 표시
        for neighbor in graph[node]:  # 인접 노드 탐색
            dfs(graph, neighbor, visited)  # 재귀 호출

# 그래프 예시
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7],
    5: [],
    6: [],
    7: []
}

dfs(graph, 1)  # 1 2 5 6 3 4 7
