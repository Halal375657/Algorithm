# Dynamic Programming.
#
# Fibonacci.
#
# Time  O(n)
#
# Memoized DP recursive Algorithm.

class Solution(object):
    def __init__(self):
        self.memo = {}
        
    def fib(self, n):
        if n in self.memo:
            return self.memo[n]

        if n <= 2:
            f = 1
        else:
            f = self.fib(n-1) + self.fib(n-2)

        self.memo[n] = f

        #print(self.memo)

        return f



if __name__ == '__main__':
    n = 8
    solve = Solution()
    res = solve.fib(n)
    print(res)
