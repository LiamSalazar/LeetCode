class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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