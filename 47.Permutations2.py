class Solution(object):
    def permuteUnique(self, nums):
        return self.permutated(nums)
    def permutated(self, lista):
        if len(lista) == 1:
            return [lista]
        result = []
        verification = []
        for i in range(len(lista)):
            currentElement = lista[i]
            left = lista[:i] + lista[i+1:]
            for perm in self.permutated(left):
                verification = [currentElement] + perm
                if verification not in result:
                    result.append(verification)
        return result
    
lista = [1,1,2]
sol = Solution()
r = sol.permuteUnique(lista)
print(r)