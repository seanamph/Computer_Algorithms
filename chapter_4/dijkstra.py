import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node == end:
            return distances[end]
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
graph = {'A': {'B': 3, 'C': 4},
         'B': {'D': 6},
         'C': {'D': 8, 'E': 5},
         'D': {'E': 2},
         'E': {'F': 4},
         'F': {}}

# 使用上述範例圖的示例呼叫
print(dijkstra(graph, 'A', 'F')) # 输出结果为 12
