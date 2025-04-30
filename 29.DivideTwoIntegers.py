class Solution(object):
    def divide(self, dividend, divisor):
        int_min, int_max = -2**31, 2**31 - 1
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):  
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        result = -result if negative else result
        return max(min(result, int_max), int_min) 

# Ejemplo de uso
dividend = -2147483648
divisor = -1
sol = Solution()
print(sol.divide(dividend, divisor))
