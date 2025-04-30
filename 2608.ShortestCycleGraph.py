class Solution(object):
    def findShortestCycle(self, n, edges):
        graph = {}
        for origin, destiny in edges:
            if origin not in graph:
                graph[origin] = []
            graph[origin].append(destiny)
            if destiny not in graph:
                graph[destiny] = []
            graph[destiny].append(origin)
        minCycle = float('inf')
        for start in graph:
            queue = [[start, -1, 0]]  
            visited = {start:0}
            while queue:
                node = queue[0][0]
                parent = queue[0][1]
                dist = queue[0][2]
                queue.pop(0)
                for neighbor in graph[node]:
                    if neighbor == parent:
                        continue
                    if neighbor in visited:
                        minCycle = min(minCycle, dist + 1 + visited[neighbor])
                    else:
                        visited[neighbor] = dist + 1
                        queue.append([neighbor, node, dist + 1])
        return minCycle if minCycle != float('inf') else -1
    
# Test Cases
n = 6
edges = [[4,1],[5,1],[3,2],[5,0],[4,0],[3,0],[2,1]]
s = Solution()
r = s.findShortestCycle(n, edges)
print(r)