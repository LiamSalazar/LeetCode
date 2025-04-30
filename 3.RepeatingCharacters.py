class Solution(object):
    def lengthOfLongestSubstring(self, s):
        patrones = []
        patron = ""
        contador = 0
        result = ""
        while contador < len(s):
            if s[contador] in patron:
                patrones.append(patron)
                patron = patron[patron.index(s[contador]) + 1:] + s[contador]
            else:
                patron += s[contador]
            contador +=1
        patrones.append(patron)
        if patrones:
            result = max(patrones, key=len)
        else:
            result = ""
        return len(result)
s = "dvdf"        
sol = Solution()
r = sol.lengthOfLongestSubstring(s)
print(r)