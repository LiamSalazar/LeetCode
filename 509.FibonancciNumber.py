class Solution(object):
    def fib(self, n):
        memoize = [-1] * (n + 1) 
        return self.fibo(n, memoize)
    def fibo(self, n, memoize):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        if memoize[n] != -1:  
            return memoize[n]
        result = self.fibo(n-1, memoize) + self.fibo(n-2, memoize)
        memoize[n] = result  
        return result

n = 5
sol = Solution()
r = sol.fib(n)
print(r)
