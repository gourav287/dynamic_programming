# -*- coding: utf-8 -*-
"""
Given a list of non-negative integers, and a target value,
determine if there is a subset of the given list with sum equal to the target.
"""

# Solution with the help of dynamic programming
def solution(arr, target):
    
    n = len(arr)
    
    # Initialize the boolean matrix. First element of each row is True,
    # because 0 can be reached from any number by just not taking it.
    subset = [[False for i in range(target + 1)] for j in range(n + 1)]
    
    for i in range(n + 1):
        
        subset[i][0] = True
    
    # Iterating through the boolean matrix to update it.
    for i in range(1, n+1):
        
        for j in range(1, target+1):
            
            # If the current value is greater than the current target value j.
            if arr[i - 1] > j:
                
                subset[i][j] = subset[i-1][j]
            
            # If current value is smaller than the current target value j,
            # just check if their difference is reachable.
            else:
                
                subset[i][j] = (subset[i-1][j] or subset[i-1][j - arr[i - 1]])
    
    # Return last element of last row as it will make certain if ans is
    # True or False
    return subset[n][target]


# The driver code
if __name__ == '__main__':
    
    arr = list(map(int, input().split()))

    target = int(input())
    
    if solution(arr, target):
        
        print("The subset exists")
    
    else:
        
        print("No such subset exist")