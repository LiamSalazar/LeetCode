class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        aux = intervals[0] 
        for interval in intervals:
            if interval[0] <= aux[1]: 
                aux[1] = max(aux[1], interval[1])  
            else:
                result.append(aux)  
                aux = interval
        result.append(aux)
        return result

intervals = [[1,3],[2,6],[8,10],[15,18]]
sol = Solution()
r = sol.merge(intervals)
print(r)