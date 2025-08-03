class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        s = s[::-1]
        result = ""
        for element in s:
            result += element
            result += " "
        return result[:len(result)-1]
    
parameter = "The sky is blue"
s = Solution()
print(s.reverseWords(parameter))