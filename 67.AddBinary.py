class Solution(object):
    def addBinary(self, a, b):
        begin = max(len(a), len(b))
        a = a.zfill(begin)  
        b = b.zfill(begin)
        aux = 0  
        result = []
        for i in range(begin - 1, -1, -1):
            sum = int(a[i]) + int(b[i]) + aux
            result.append(str(sum % 2)) 
            aux = sum // 2 
        if aux:
            result.append("1")
        return ''.join(result[::-1])

a = "1111"
b = "1111"
print(Solution().addBinary(a, b)) # Output: 10101