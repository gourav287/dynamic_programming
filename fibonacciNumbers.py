"""
This is the simplest example of dynamic programming.
The recurrsive code for Fibonacci series takes exponential time
But if we save the values beforehand, the complexity drops down to linear
"""

# Naive recurrsive method to generate n-th fibonacci number (takes O(2ⁿ) time)
# Start noticing difference from n = 30, takes almost 25 seconds to compute
# 40th fibonacci number
def Fibonacci_naive(n):

    if n <= 1:

        return n

    # Calculates values of subproblems whenever needed, so increases time
    return Fibonacci_naive(n-1) + Fibonacci_naive(n-2)


# Optimized function to generate n-th fibonacci number by DP (takes O(n) time)
def Fibonacci_fast(n):

    fib = [0, 1]

    for i in range(n-2):

        # Saving the values and using them later
        # instead of calculating them every single time
        fib.append(fib[i] + fib[i+1])

    return fib[-1]

# The driver code for this file
if __name__ == "__main__":

    # Input the number of fibonacci to generate
    n = int(input())
    
    # Optimized function to generate n fibonacci numbers
    fast_fib = Fibonacci_fast(n)

    print("Fib-Fast:", fast_fib)
    
    # Regular recurrsive function to generate n-th fibonacci number
    naive_fib = Fibonacci_naive(n - 1)

    print("Fib-naive:", naive_fib)
