class Solution(object):
    def permute(self, nums):
        return self.permutated(nums)
    def permutated(self, list):
        if len(list) == 1:
            return [list]
        result = []
        for i in range(len(list)):
            currentElement = list[i]
            left = list[:i] + list[i+1:]
            for perm in self.permutated(left):
                result.append([currentElement] + perm)
        return result

list = [1,2,3]
sol = Solution()
r = sol.permute(list)
print(r)