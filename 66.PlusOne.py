class Solution(object):
    def plusOne(self, digits):
        digit = 0
        result = []
        for num in digits:
            digit *= 10
            digit += num
        digit += 1
        while digit > 0:
            result.append(digit % 10)
            digit = digit // 10
        return list(reversed(result))
sol = Solution()
print(sol.plusOne([1,2,3])) # [1,2,4]