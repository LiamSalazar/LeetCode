from collections import defaultdict, deque

# Grafo dado por sus aristas
edges = [[4, 1], [5, 1], [3, 2], [5, 0], [4, 0], [3, 0], [2, 1]]

# Convertir lista de aristas en un diccionario de adyacencia
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    paths = [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            paths.extend(dfs(graph, neighbor, visited))
    return paths

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    paths = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            paths.append(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    return paths

def find_cycles(graph):
    def dfs_cycle(v, parent, visited, path):
        visited.add(v)
        path.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                if dfs_cycle(neighbor, v, visited, path):
                    return True
            elif parent != neighbor:
                path.append(neighbor)
                return True
        path.pop()
        return False
    
    visited = set()
    path = []
    for vertex in graph:
        if vertex not in visited:
            if dfs_cycle(vertex, -1, visited, path):
                cycle_start = path.index(path[-1])
                return path[cycle_start:]
    return None

# Imprimir caminos posibles usando DFS y BFS
start_vertex = 0  # Puedes elegir cualquier vértice de inicio
print("DFS path:", dfs(graph, start_vertex))
print("BFS path:", bfs(graph, start_vertex))

# Encontrar e imprimir ciclos posibles
cycle = find_cycles(graph)
if cycle:
    print("Cycle found:", cycle)
else:
    print("No cycle found")
