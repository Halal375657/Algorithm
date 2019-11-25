#
# Dynamic Programming.
#
# Fibonacci.
#
# Time O(n), Space O(n)

# Bottom-Up DP Algorithm.

n = 8
fib = {}
for k in range(n+1):
    if k <= 2:
        f = 1
    else:
        f = fib[k-1] + fib[k-2]

    fib[k] = f

print(fib)
