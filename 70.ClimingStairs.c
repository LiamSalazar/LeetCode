int memo[1000] = {0}; 

int fib(int n) {
    if (n == 1) {
        return 1;
    }
    if (n == 2) {
        return 2;
    }
    if (memo[n] != 0) {
        return memo[n];
    }
    memo[n] = fib(n - 1) + fib(n - 2);
    return memo[n];
}
int climbStairs(int n) {
    return fib(n);
}