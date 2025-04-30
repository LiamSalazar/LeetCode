class Solution(object):
    def repeatedCharacter(self, s):
        visited = []
        for letter in s:
            if letter in visited:
                return letter
            else:
                visited.append(letter)

sol = Solution()
s = "abccbaacz"
r = sol.repeatedCharacter(s)
print(r)