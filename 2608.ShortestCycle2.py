from collections import deque

# Grafo representado como una lista de adyacencia
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

def bfs(graph, start):
    # Cola para BFS
    queue = deque([start])
    # Diccionario para rastrear si un nodo fue visitado
    visited = {node: False for node in graph}
    # Diccionario para rastrear distancias desde el nodo inicial
    distance = {node: float('inf') for node in graph}
    
    # Marcamos el nodo inicial como visitado
    visited[start] = True
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        print(f"Nodo actual: {current}, Distancia: {distance[current]}")
        
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    return distance

# Nodo inicial
start_node = 0
distances = bfs(graph, start_node)

print("\nDistancias desde el nodo inicial:")
for node, dist in distances.items():
    print(f"Nodo {node}: {dist}")
