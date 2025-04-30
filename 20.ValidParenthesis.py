class Solution(object):
    def isValid(self, s):
        stack = [] 
        parenthesis = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p in parenthesis:
                top = stack.pop() if stack else '#'
                if parenthesis[p] != top:
                    return False
            else:
                stack.append(p)
        return not stack

# Prueba
sol = Solution()
print(sol.isValid("({[()]})"))  # True 
print(sol.isValid("([)]"))      # False 
print(sol.isValid("{[]}"))      # True 
print(sol.isValid(""))      # True 
