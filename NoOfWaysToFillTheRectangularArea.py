# -*- coding: utf-8 -*-
"""
Given a rectangle field of dimensions (n*2), find the number of ways
it can be covered with n rectangular tiles of dimensions (1*2)
"""

# Solution with the help of dynamic programming memoization
# For the starting we can place either one tile horizontally, leaving
# space for n-1 tiles to occupy the area or 2 tiles vertically
# leaving space for n-2 tiles to occupy the remaining area.
# Hence n tiles can cover area that is addition of ways n-1 and n-2 tiles
# cover the area
def NoOfWays(n, memo):
    
    if n <= 2:
        
        return n
    
    if memo[n] != 0:
        
        return memo[n]
    
    memo[n] = NoOfWays(n - 1, memo) + NoOfWays(n - 2, memo)
    
    return memo[n]


# The driver code
if __name__ == '__main__':
    
    n = int(input())
    
    memo = [0 for i in range(n+1)]
    
    print(NoOfWays(n, memo))
    
