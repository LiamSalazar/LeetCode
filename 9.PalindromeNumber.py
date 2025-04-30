class Solution(object):
    def isPalindrome(self, x):
        cadena = str(x)
        return cadena == cadena[::-1]
x = 121
sol = Solution()
r = sol.isPalindrome(x)
print(r)