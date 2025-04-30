class Solution(object):
    def isPalindrome(self, s):
        s2 = ''.join([caracter.lower() for caracter in s if caracter.isalnum()])
        return s2 == s2[::-1]


sol = Solution()
x = "A man, a plan, a canal: Panama"
r = sol.isPalindrome(x)
print(r)