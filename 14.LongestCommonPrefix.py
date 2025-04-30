class Solution(object):
    def longestCommonPrefix(self, strs):
        reference = strs[0]
        result = ""
        for i in range(len(reference)):
            for word in strs:
                if i >= len(word) or word[i] != reference[i]:
                    return result
            result += reference[i]
        return result
strs = ["flower","flow","flight"]
sol = Solution()
r = sol.longestCommonPrefix(strs)
print(r)