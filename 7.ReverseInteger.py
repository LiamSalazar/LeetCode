class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        resultado = 0
        signo = -1 if x < 0 else 1  
        x = abs(x) 
        
        while x != 0:
            digito = x % 10
            x //= 10
            resultado = resultado * 10 + digito
        resultado *= signo
        
        if resultado < INT_MIN or resultado > INT_MAX:
            return 0
        
        return resultado

x = 321
sol = Solution()
r = sol.reverse(x)
print("RESULT: ", r)
