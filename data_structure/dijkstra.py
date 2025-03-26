import heapq  # 우선순위 큐 사용

def dijkstra(graph, start):
    # 모든 노드까지의 거리를 무한대로 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드의 거리는 0
    pq = [(0, start)]  # (거리, 노드) 튜플을 힙에 추가

    while pq:
        current_distance, current_node = heapq.heappop(pq)  # 최단 거리 노드 선택

        if current_distance > distances[current_node]:
            continue  # 이미 처리된 노드면 스킵

        for neighbor, weight in graph[current_node]:  # 현재 노드의 인접 노드 탐색
            distance = current_distance + weight  # 새로운 거리 계산

            if distance < distances[neighbor]:  # 최단 거리 갱신
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))  # 우선순위 큐에 추가

    return distances

# 그래프 예시 (인접 리스트 표현)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))  # {'A': 0, 'B': 1, 'C': 3, 'D': 4}
