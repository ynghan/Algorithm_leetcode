class Solution:
    def climbStairs(self, n: int) -> int:
        # f(3) = f(2) + f(1) = 3
        # f(4) = f(3) + f(2) = 5
        # f(5) = f(4) + f(3) = 8

        memo = {1:1, 2:2}

        def fibo(n: int) -> int:
            if n in memo:
                return memo[n]
            memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]

        return fibo(n)