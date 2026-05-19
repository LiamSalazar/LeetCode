class Solution(object):
    def minJumps(self, arr):
        n = len(arr)
        if n <= 1:
            return 0
        same_values = {}
        for i in range(n):
            if arr[i] not in same_values:
                same_values[arr[i]] = []
            same_values[arr[i]].append(i)
        queue = [(0,0)]
        visited = {0}
        while queue:
            index, jumps = queue.pop(0)
            neighbors = []
            if index-1 >= 0:
                neighbors.append(index-1)
            if index+1 < n:
                neighbors.append(index+1)
            if arr[index] in same_values:
                neighbors.extend(same_values[arr[index]])
                del same_values[arr[index]]
            for neighbor in neighbors:
                if neighbor == n-1:
                    return jumps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, jumps + 1))
        return jumps

# test
#arr = [100,-23,-23,404,100,23,23,23,3,404]
arr = [7,7,7,7,2]
#arr = [2,1,2,1,2,4,5,8]
print(Solution().minJumps(arr))