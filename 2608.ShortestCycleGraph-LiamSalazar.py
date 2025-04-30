class Solution(object):
    def findShortestCycle(self, n, edges):
        graph = {}
        allNodes = set()
        for origin, destiny in edges:
            allNodes.add(origin)
            allNodes.add(destiny)
            if origin not in graph:
                graph[origin] = []
            graph[origin].append(destiny)

        for node in allNodes:
            if node not in graph:
                graph[node] = []

        nodos = list(allNodes)
        infinity = 10000
        minimum = infinity

        for nodo in nodos:
            queue = [[nodo, -1, 0]]
            visited = {nodo:0}
            i = 0
            while i < len(queue):
                current = queue[i][0]
                father = queue[i][1]
                distance = queue[i][2]
                i += 1
                if current in graph:
                    neighbours = graph[current]
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            visited[neighbour] = distance + 1
                            queue.append([neighbour, distance + 1])
                        elif neighbour == nodo:
                            if distance+1 < minimum:
                                minimum = distance +1
        if minimum == infinity:
            return -1
        return minimum
        
# Falta caso donde nodo solamente este en destinos pero no en los nodos origen
# Test Cases
n = 6
edges = [[4,1],[5,1],[3,2],[5,0],[4,0],[3,0],[2,1]]
#edges = [[1,2],[2,3],[3,1]]
s = Solution()
r = s.findShortestCycle(n, edges)
print(r)