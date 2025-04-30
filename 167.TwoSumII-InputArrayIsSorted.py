class Solution(object):
    def twoSum(self, numbers, target):
        indexes = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in indexes:  
                return [indexes[complement]+1, i+1]
            indexes[numbers[i]] = i
        return None
