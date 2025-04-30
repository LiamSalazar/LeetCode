class Solution(object):
    def singleNumber(self, nums):
        resultVector = []
        for num in nums:
            if num not in resultVector:
                resultVector.append(num)
            else:
                resultVector.remove(num)
        return resultVector[0]